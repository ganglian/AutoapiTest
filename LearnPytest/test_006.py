'''
mark标记
1、skip：这个版本有缺陷，导致某个用例不通过，可以跳过这个用例的执行，等缺陷修复后，再放开执行
2、自定义标记，
    随着代码规模增大，包含功能测试，接口测试，性能测试，冒烟测试，只想执行接口测试的用例，怎么测
'''
import pytest


def test_case1():
    print("测试用例1")

@pytest.mark.skip(reason="有缺陷，缺陷号为23457856482，待解决缺陷后再执行")
def test_case2():
    print("测试用例2")
@pytest.mark.maoyan
def test_case3():
    print("测试用例3")

# 放到类上面，对类的每个方法生效
@pytest.mark.api
class TestUsermark:
    @pytest.mark.maoyan
    def test_case4(self):
        print("测试用例4")

    def test_case5(self):
        print("测试用例5")

    def test_case6(self):
        print("测试用例6")
