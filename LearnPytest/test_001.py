'''
测试前置和后置
函数和方法，放在类里的叫方法，类外的叫函数
模块级（每个模块执行一次）和函数级（每个函数执行一次）通常一起使用
'''

def setup_module():
    print("测试前置：登陆系统")

def setup_function():#函数级别的，名字使用setup一样的效果
    print("测试前置：每个函数执行一次")

def teardown_function():#函数级别的，名字使用teardown一样的效果
    print("测试后置：每个函数执行一次")

def teardown_module():
    print("测试后置：退出登录系统")

def test_001():
    print("测试充值功能的用例1")

def test_002():
    print("测试充值功能的用例2")

def test_003():
    print("测试充值功能的用例3")