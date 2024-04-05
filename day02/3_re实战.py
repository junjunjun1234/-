"""
目标: 豆瓣top250电影信息
    名称, 发布年限, 评分, 评价人数

思路:
    1. 拿到页面源代码
    2. 使用re正则去提取数据
    3. 存储到文件中....???
"""
import requests
import re

url = "https://movie.douban.com/top250"

head = {
    # UA, 服务器对当前的网络设备进行检测
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

resp = requests.get(url, headers=head)  # 处理一个小小的反爬
resp.encoding = 'utf-8'
# print(resp.text)


obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<br>(?P<year>.*?)&nbsp;.*?<span class="rating_num" '
                 r'property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)人评价</span>', re.S)  # re.S可以让re匹配到换行符

result = obj.finditer(resp.text)
for item in result:
    dic = item.groupdict()
    dic['year'] = dic['year'].strip()  # 去掉年份左右两端的空白(空格, 换行符, 制表符)
    print(dic)
