'''
测试充值功能
'''
import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.readyaml(r"ZongHe/data_case/recharge_data.yaml"))
def recharge_data(request):
    return request.param

@pytest.fixture(params=DataRead.readyaml(r"ZongHe/data_case/recharge_setup.yaml"))
def setup_data(request):
    return request.param

# 测试前置和后置
@pytest.fixture()
def register(setup_data, url, baserequests, db):
    # 注册
    phone = setup_data['casedata']['mobilephone']
    DbOp.deleteUser(db, phone)
    Member.register(url, baserequests, setup_data['casedata'])
    yield
    # 删除注册用户
    DbOp.deleteUser(db, phone)



def test_recharge(register, recharge_data,url, baserequests):
    # 充值
    # 检查登录结果
    r = Member.recharge(url, baserequests, recharge_data['casedata'])
    assert r.json()['msg'] == recharge_data['expect']['msg']