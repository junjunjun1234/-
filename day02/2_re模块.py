import re

# result = re.findall(r"\d+", "今天我有100块, 买了2个蛋糕")  # 拿到的是列表
# result = re.search(r"\d+", "今天我有100块, 买了2个蛋糕")  # 只拿到第一个结果就返回
# result = re.finditer(r"\d+", "今天我有100块, 买了2个蛋糕")  # 把所有的结果放在迭代器里
# for item in result:
#     print(item.group())  # 从match对象中拿到数据. 需要group()


# # 预加载
# obj = re.compile(r"\d+")
#
# result = obj.findall("今天我有100块, 买了2个蛋糕")
# print(result)

s = """
<div class="abc">
    <div><a href="baidu.com">我是百度</a></div>
    <div><a href="qq.com">我是腾讯</a></div>
    <div><a href="163.com">我是网易</a></div>
</div>
"""

obj = re.compile(r'<div><a href="(?P<url>.*?)">(?P<txt>.*?)</a></div>')
result = obj.finditer(s)
for item in result:
    # url = item.group("url")
    # txt = item.group("txt")
    # print(txt, url)
    print(item.groupdict())
