'''
任务集合:简单的分层管理
'''
from locust import TaskSet, HttpUser, between, task


# 租车系统
# 系统管理模块
class SystemManage(TaskSet):
    @task
    def task1(self):
        self.client.get("/carRental/sys/toUserManager.action")

    @task
    def task2(self):
        self.client.get("/carRental/sys/toRoleManager.action")

    @task
    def task3(self):
        self.client.get("/carRental/sys/toLogInfoManager.action")

class BasicManage(TaskSet):
    @task(7)
    def task1(self):
        self.client.get("/carRental/bus/toCustomerManager.action")

    @task(3)
    def task2(self):
        self.client.get("/carRental/bus/toCarManager.action")

class CarRentalTest(HttpUser):
    wait_time = between(1, 3)  # 任务之间的间隔时间
    # tasks = [BasicManage, SystemManage]  # 任务集合，tasks是User中定义的属性，不能写错
    tasks = {BasicManage: 4, SystemManage: 1}
    # 任务集合(分配不均匀)，后面数字表示权重，比如访问基础管理模块的人会比访问系统配置的人多四倍
    # 或者访问基础管理模块的频率比访问系统配置的频率高3倍

    def on_start(self):#测试前置，登录，在开始运行时每个用户调用一次
        user = {"loginname":"admin","pwd":"123456"}
        self.client.post("/carRental/login/login.action",data=user)

    def on_stop(self):#测试后置，退出登录，在结束运行时每个用户调用一次
        self.client.post("/carRental/logout/logout.action")

# locust -f locust_test2.py --host=http://127.0.0.1:8080 --web-host=127.0.0.1