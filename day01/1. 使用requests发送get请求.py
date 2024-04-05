import requests

# 爬百度的信息
url = "http://www.baidu.com"  # 这里不要用https

# 发送请求
resp = requests.get(url)
# 设置字符集
resp.encoding = 'utf-8'
# print(resp.text)  # 拿到页面源代码

# 把页面源代码写入到文件中
with open("mybaidu.html", mode="w", encoding='utf-8') as f:
    f.write(resp.text)
print("over!!")
