from urllib import request

resp = request.urlopen('https://www.sogou.com')

print(resp.read())