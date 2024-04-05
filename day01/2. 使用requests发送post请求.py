import requests

url = "https://fanyi.baidu.com/sug"

周杰伦 = {
    "kw": input("请输入一个你想搜索的单词")
}
resp = requests.post(url, data=周杰伦)

# print(resp.text)
# 如果返回的数据是json. 可以直接resp.json()
print(resp.json())
