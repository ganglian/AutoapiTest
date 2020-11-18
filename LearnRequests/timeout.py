'''
timeout:
1.接口性能测试，比较某个接口在500ms返回；
2.耗时比较久的操作，默认的超时时间执行不完，比如上传超大的文件，可以设置大一点的超时时间
'''
import requests

url = 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=13112345678'
# 0.1表示100ms
for i in range(10):
    try:
        r = requests.get(url, timeout=0.1)
        print(r.text)
        print(r.text)
    except Exception as e:
        print(e)

'''
proxies 代理
1.通过代理抓包，用fiddle抓自动化发的报文分析，为了定位问题。
2.服务器把IP地址禁掉，可以通过代理换个IP访问。
'''

proxy = {
    "http":"http://127.0.0.1:8888", # http代理
    "https":"http://127.0.0.1:8888" # https代理
}
# 设置proxies参数时，需要打开代理服务器，比如Fiddler
r = requests.get("http://www.baidu.com", proxies=proxy)
print(r.text)
# 不加verify=False时，会校验证书，发送请求报错，certificate verify failed，可以设置verify=False，不校验证书
r = requests.get("https://www.baidu.com", proxies=proxy, verify=False)
print(r.text)