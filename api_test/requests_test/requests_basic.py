import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import json
from jsonpath import jsonpath

base_url = 'http://httpbin.org'

r = requests.get(base_url + '/get')
print(r.status_code)
res = r.json()  # 对于响应值r先进行json编码
print(res)
assert res['headers']['Host'] == 'httpbin.org'


# r = requests.post(base_url + '/post')
# print(r.status_code)
#
r = requests.put(base_url + '/put')
print(type(r))
# print(r.content)  # HTTP响应内容的二进制形式
# print(r.encoding)  # 从HTTP header中猜测的响应内容编码方式
print(r.text)    # 把Response对象的内容以字符串的形式返回
# print(r.raw)    # 获得原始响应内容
# print(r.json())

# res = r.json()
# print(type(res))
# print((res['headers']['User-Agent']))
#
# r = requests.delete(base_url + '/delete')
# print(r.status_code)


# #get参数传递
# param_data = {'user':'guoxl','password':'888888'}
# r = requests.get(base_url + '/get', params=param_data)
# print(r.url)
# print(r.status_code)  #打印响应状态码


# r = requests.get(base_url + '/get?username=guoxl&password=88888')
# print(r.url)
# print(r.headers)
# print(r.status_code)  #打印响应状态码

# # post参数传递，Post请求中，一般参数都在body中传递
# from_data = {'user':'guonian','password':'66666'}
# r = requests.post(base_url + '/post', data=from_data)
# print(r.text)  #获取响应内容
# print(r.headers)  #获取响应头信息

# post参数传递，用data关键字发送json请求，使用json.dumps对传入的变量进行转码
from_data = {'user':'guonian','password':'66666'}
r = requests.post(base_url + '/post', data=json.dumps(from_data))
# 使用json关键字参数，，Content-Type自动变为“application/json”
# r = requests.post(base_url + '/post', json=from_data)
print(r.text)  #获取响应内容
# print(r.headers)  #获取响应头信息
resjson = r.json()
assert jsonpath(resjson, "$.headers.Host")[0] == 'httpbin.org'
assert jsonpath(resjson, "$.url")[0] == 'http://httpbin.org/post'
assert jsonpath(resjson, "$['json']['password']")[0] == '66666'


# # 请求头定制
# from_data = {'user':'guoxl', 'password':'gxl1512'}
# # print(type(from_data))
# header = {'user-agent':'Mozilla/8.0'}
# r = requests.post(base_url + '/post', data=from_data, headers=header)
# print(r.text)
# # print(r.json())  #以json格式展示响应内容


# # 访问知乎，设置请求头信息，否则会被反爬虫拒绝
# header = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# r = requests.get('https://www.zhihu.com/explore', headers=header)
# # print(r.text)
# print(r.headers)  #获取响应头信息

# # 设置cookie
# cookie = {'user':'guoxl'}
# r = requests.get(base_url + '/cookies', cookies=cookie)
# print(r.text)

# # # 获取cookie
# r =requests.get('https://www.baidu.com')
# print(r.cookies)
# print(type(r.cookies))
# for key,value in r.cookies.items():
#     print(key + ':' + value)


# # 设置超时时间,单位秒
# r = requests.get(base_url + '/get', timeout = 0.005)
# print(r.text)
#
# # 上传文件
# file = {'file':open(r'E:\Picture\petimg\10.png','rb')}
# r = requests.post(base_url + '/post',files=file)
# print(r.text)


# # 设置cookie
# r = requests.get(base_url + '/cookies/set/user/guoxl')
# print(r.text)

# # 获取cookie,在没有session保存机制的情况下，第二个接口无法获取上面第一个接口设置的Cookie值
# r = requests.get(base_url + '/cookies')
# print(r.text)

#
# # 生成会话对象,Request的会话对象让你能够跨请求保持某些参数。它也会在同一个Session实例发出的所有请求之间保持cookie
# s = requests.Session()
#
# # 设置cookie
# r = s.get(base_url + '/cookies/set/user/guoxl')
# print(r.text)
#
# # 获取cookie
# r = s.get(base_url + '/cookies')
# print(r.text)


# # 证书验证
# # r = requests.get('https://www.12306.cn')
# # 关闭SSL证书验证。SSL证书验证默认开启
# r = requests.get('https://www.12306.cn', verify=False)
# print(r.text)


# # 代理设置，如翻墙，VPN
# # origin参数为设置的代理ip(未成功)
# proxies = {'http':'http://121.13.252.58:41564'}
# r = requests.get(base_url + '/get', proxies=proxies)
# print(r.text)


# # 身份认证BasicAuth,前面的请求用户名和密码必须和后面授权的一致
# r =requests.get(base_url + '/basic-auth/guoxl/8888', auth=HTTPBasicAuth('guoxl','8888'))
# print(r.status_code)
# print(r.text)
# # # 身份认证DigestAuth
# r = requests.get(base_url + '/digest-auth/auth/guonian/6666',auth=HTTPDigestAuth('guonian','6666'))
# print(r.text)


# # 流式请求
# r = requests.get(base_url + '/stream/10',stream=True)
# print(r.text)
#
# # 如果响应内容没有设置编码，则默认设置为utf-8
# if r.encoding is None:
#     r.encoding = 'utf-8'
#
# # 对结果进行迭代处理
# for line in r.iter_lines(decode_unicode=True):
#     if line:
#         # 将json数据类型转为python数据类型
#         data = json.loads(line)
#         print(data['id'])
#         print(data['url'])