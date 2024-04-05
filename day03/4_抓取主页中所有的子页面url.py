import requests
from lxml import etree

domain = "https://desk.zol.com.cn"
# 1. 拿到页面源代码
url = "https://desk.zol.com.cn/dongman/"
resp = requests.get(url)
resp.encoding = "gbk"

et = etree.HTML(resp.text)

result = et.xpath("//ul[@class='pic-list2  clearfix']/li/a/@href")
for item in result:
    url = domain + item
    print(url)
