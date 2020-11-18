import requests
import pytest

@pytest.fixture(params=[{"realdata":{"mobilephone": 19812345678, "pwd": 123456, "regname": "小小怪"},
                        "expect":{"status": 0, "code": "10001", "data": None, "msg": "注册成功"}}
                        ])
def data(request):
    return request.param

def test_register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data['realdata'])
    assert r.json()['code'] == data['expect']['code']
    print(r)



