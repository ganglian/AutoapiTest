'''
上传文件，一般都是post接口，用files参数上传文件
'''

import requests

url = "http://www.httpbin.org/post"

'''
files参数，字典的格式，'name':file-tuple
file-tuple可以是2-tuple ('filename', fileobj)、3-tuple('filename', fileobj, 'content_type')、4-tuple('filename', fileobj, 'content_type', custom_headers)
'''
with open("d:/test.txt", encoding='utf-8') as f:
    # , "text/plain" 如果上传的是一个文本文件，可以去掉content_type，默认文件类型是文本文件。
    file = {"file1":("test.txt", f, "text/plain")}  # MIME类型：text/plain、image/png、image/gif、application/json
    r = requests.post(url, files=file)
    print(r.text)
    # \u4e0a\u5c71\u6253 unicode编码，网上由Unicode转中文/中文转Unicode的小工具，可以在线转。

# 上传一个图片文件，10k以内
with open("C:/Users/ASUS/Desktop/pic/h9.png", mode='rb') as f:
    image = {"file2": ("h9.png", f, "image/png")}
    r = requests.post(url, files=image)
    print(r.text)

# 可以一次上传多个文件。
# with open("'d:/test.txt', encoding='utf-8'", "'C:/Users/ASUS/Desktop/pic/h9.png', mode='rb'") as f:
#     s = {"file1": ("test.txt", f, "text/plain"), "file2": ("h9.png", f, "image/png")}
#     r = requests.post(url, files=s)
#     print(r.text)     # 错误

with open("d:/test.txt", encoding='utf-8') as f1:
    with open("C:/Users/ASUS/Desktop/pic/h9.png", mode='rb') as f2:
        file = {
            "file1":("test.txt", f1, "text/plain"),
            "file2": ("h9.png", f2, "image/png")
        }
        r = requests.post(url, files=file)
        print(r.text)