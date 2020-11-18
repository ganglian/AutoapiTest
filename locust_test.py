'''
性能测试
'''
import math
from locust import HttpUser, TaskSet, task, constant, between
from locust import LoadTestShape

'''
1.为要模拟的用户定义一个类
'''
class CarRental(HttpUser):
    # between 是User类中定义的一个方法
    # wait_time是User类定义的一个属性，表示等待时间
    wait_time = between(3,8) # 任务和任务的等待时间在3~8之间取随机数
    @task
    def loadAllRent(self):
        #
        self.client.get("/carRental/rent/loadAllRent.action?page=1&limit=10")
    @task
    def loadAllMenu(self):
        self.client.get("/carRental/rent/loadAllRent.action?page=1&limit=10")
# -f 要执行的文件
# --host 被测系统
# --web-host  locust web页面的访问地址
# --web-port  locust web页面的访问端口
# locust -f locust_test.py --host=http://127.0.0.1:8080 #--web-host=127.0.0.1 --web-port=8089
# locust -f locust_test.py --host=http://127.0.0.1:8080 --web-host=127.0.0.1  # 在terminal运行

# 加压的三种方法
# 方法一
# class UserTasks(TaskSet):
#     @task
#     def get_root(self):
#         self.client.get("/")
#
#
# class WebsiteUser(HttpUser):
#     wait_time = constant(0.5)
#     tasks = [UserTasks]
#
#
# class StepLoadShape(LoadTestShape):
#     """
#     A step load shape
#
#
#     Keyword arguments:
#
#         step_time -- Time between steps
#         step_load -- User increase amount at each step
#         spawn_rate -- Users to stop/start per second at every step
#         time_limit -- Time limit in seconds
#
#     """
#
#     step_time = 30
#     step_load = 10
#     spawn_rate = 10
#     time_limit = 600
#
#     def tick(self):
#         run_time = self.get_run_time()
#
#         if run_time > self.time_limit:
#             return None
#
#         current_step = math.floor(run_time / self.step_time) + 1
#         return (current_step * self.step_load, self.spawn_rate)

# 方法二
# class UserTasks(TaskSet):
#     @task
#     def get_root(self):
#         self.client.get("/")
#
#
# class WebsiteUser(HttpUser):
#     wait_time = constant(0.5)
#     tasks = [UserTasks]
#
#
# class DoubleWave(LoadTestShape):
#     """
#     A shape to immitate some specific user behaviour. In this example, midday
#     and evening meal times.
#
#     Settings:
#         min_users -- minimum users
#         peak_one_users -- users in first peak
#         peak_two_users -- users in second peak
#         time_limit -- total length of test
#     """
#
#     min_users = 20
#     peak_one_users = 60
#     peak_two_users = 40
#     time_limit = 600
#
#     def tick(self):
#         run_time = round(self.get_run_time())
#
#         if run_time < self.time_limit:
#             user_count = (
#                 (self.peak_one_users - self.min_users)
#                 * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 5) ** 2)
#                 + (self.peak_two_users - self.min_users)
#                 * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 10) ** 2)
#                 + self.min_users
#             )
#             return (round(user_count), round(user_count))
#         else:
#             return None

# 方法三
class UserTasks(TaskSet):
    @task
    def get_root(self):
        self.client.get("/")


class WebsiteUser(HttpUser):
    wait_time = constant(0.5)
    tasks = [UserTasks]


class StagesShape(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.

    Keyword arguments:

        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage

        stop_at_end -- Can be set to stop once all stages have run.
    """

    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 10},
        {"duration": 100, "users": 50, "spawn_rate": 10},
        {"duration": 180, "users": 100, "spawn_rate": 10},
        {"duration": 220, "users": 30, "spawn_rate": 10},
        {"duration": 230, "users": 10, "spawn_rate": 10},
        {"duration": 240, "users": 1, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None
