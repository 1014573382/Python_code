import urllib  #请求http
import urllib.request
import re    #正则匹配

def load_page(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data

def get_image(html):
    regx = r'http://[\S]*jpg'
    #正则表达式，获取所有以http开头、以jpg结尾的图片
    pattern = re.compile(regx)
    get_image = re.findall(pattern, repr(html))
    #根据正则表达式，抓取所有图片存在一个数组中

    num = 1
    for img in get_image:
        image = load_page(img)
        with open('D:\\Python\\photo\\%s.jpg' %num, 'wb') as fb:
            fb.write(image)
            print("正在下载第%s张图片" %num)
            num = num+1
    print("下载完成！")

url='http://www.tupianzj.com/'
html = load_page(url)
get_image(html)
