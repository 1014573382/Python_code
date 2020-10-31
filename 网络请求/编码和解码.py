from urllib import parse, request

# 编码
data = {'name': '老王', 'age': 18, 'greet': 'hello world'}
qs = parse.urlencode(data)
print(qs)

data1 = {'wd': '薛之谦'}
qs1 = parse.urlencode(data1)
print(qs1)

# 解码
print(parse.parse_qs(qs1))

# 用上面对汉字的编码结果，访问带汉字的url，
url = 'https://www.baidu.com/s?ie=utf-8&fr=bks0000&wd='+qs1
resp = request.urlopen(url)
print(resp.read())

# 对字符串进行编码，使用 quote 函数
a = '薛之谦'
b = parse.quote(a)
print(b)

