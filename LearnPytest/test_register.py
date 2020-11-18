'''
pytest命名规则
1.测试文件以test_开头或结尾
2.测试类以Test开头
3.测试方法以test_开头
'''

import requests

def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data)
    return r

# 手机号码格式不正确
def test_register_001():
    # 测试数据
    data = {"mobilephone": 131123456789, "pwd": 123456, "regname": "小丸子"}
    # 预期结果
    expect = {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}
    # 测试步骤
    real = register(data)
    # 检查结果
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']

def test_register_002():
    data = {"mobilephone": 13112345678, "pwd": 1234, "regname": "小丸子"}
    expect = {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}
    real = register(data)
    assert real.json()['code'] == expect['code']
    assert real.json()['msg'] == expect['msg']

def test_register_003():
    data = {"mobilephone": 13112345678, "pwd": 123456, "regname": ""}
    expect = {"status": 0, "code": "20103", "data": None, "msg": "参数错误：参数不能为空"}
    real = register(data)
    assert real.json()['code'] == expect['code']
    assert real.json()['msg'] == expect['msg']

def test_register_004():
    data = {"mobilephone": 13112345677, "pwd": 123456, "regname": "helloc"}
    expect = {"status": 0, "code": "10001", "data": None, "msg": "注册成功"}
    real = register(data)
    assert real.json()['code'] == expect['code']
    assert real.json()['msg'] == expect['msg']