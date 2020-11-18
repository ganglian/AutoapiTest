'''
发送get请求
'''

import requests
# 接口地址 "http://www.baidu.com"
# 发送的一个get请求,r收到了响应
r = requests.get("http://www.baidu.com")
# 文本格式的响应内容
print(r.text)
# 响应码   200
print(r.status_code)
assert r.status_code == 200     # 断言响应码是不是200
# ok
print(r.reason)
assert r.reason == 'OK'


# http://主机地址:端口号/futureloan/mvc/api/模块/接口名
# 发送请求
# r = requests.get("http://jy001:8081/futureloan/mvc/api/member/list")
# print(r.text)
# print(r.reason)
# print(r.json()['status'])
# print(r.json()['code'])
# 检查结果
# assert r.status_code == 200
# assert r.reason == 'OK'
# assert r.json()['status'] == 1
# assert r.json()['code'] == '10001'


# get请求带参数
# 方法一：拼接到url后面（金融项目注册接口）
# 方法二：使用params传参数
# url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=18220306410&pwd=123456&regname=小丑"
# r = requests.get(url)
# print(r.text)
# print(r.reason)
# print(r.json()['status'])
# print(r.json()['code'])
# assert r.status_code == 200
# assert r.reason == 'OK'
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20110'
# print(" ")

# 方法二
# url = "http://jy001:8081/futureloan/mvc/api/member/register"
# canshu = {"mobilephone": "18220306410", "pwd": "123456", "regname": "小丑"}
# r = requests.get(url, params=canshu)
# print(r.text)

# 登录信息
# url = "http://jy001:8081/futureloan/mvc/api/member/login"
# canshu = {"mobilephone": "13112345678", "pwd": "123456", "regname": "小丸子"}
# r = requests.get(url, params=canshu)
# print(r.text)

# get带请求头,User-Agent伪装成浏览器发送的请求，避免服务器屏蔽自动化发送的请求。
url = "http://www.httpbin.org/get"  # 一个测试网站，get是接口名字，发送的请求，原封的返回回来
r = requests.get(url) # "User-Agent": "python-requests/2.24.0",
print(r.text)
# User-agent包含浏览器的版本号、操作系统的版本号等信息。
tou = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
r = requests.get(url, headers=tou)
print(r.text)
#
url = "https://wenku.baidu.com/view/027d607deff9aef8941e06c0.html"
r = requests.get(url, headers=tou)
print(r.text)
print("蜂群算法源代码" in r.text)
