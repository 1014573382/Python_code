import hashlib

'''用户名和密码经过MD5加密的结果'''
def getsign(user, passwd):
    str = user + passwd
    md5 = hashlib.md5()
    md5.update(str.encode(encoding = 'utf-8'))
    sign = md5.hexdigest()
    return sign

print(getsign('guoxl', '8888'))