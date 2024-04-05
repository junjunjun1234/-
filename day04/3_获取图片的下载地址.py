"""
1. 访问到详情页, 提取到var deskPicArr = "xxxxx"
2. 分析xxxxxx. 提取两个内容, imgsrc, orisize
3. 将orisize怼到imgsrc中. 直接就能够拿到图片的下载路径
"""
import requests
import re
import json

# url = "https://desk.zol.com.cn/bizhi/9374_114228_2.html"
# resp = requests.get(url)

# obj = re.compile(r"var deskPicArr.*?=(?P<deskPicArr>.*?);", re.S)

# result = obj.search(resp.text)
# deskPicStr = result.group("deskPicArr")  # 从正则.*?提取的内容一定是字符串

# 把类似字典的字符串真的变成字典
# deskPic = json.loads(deskPicStr)
# for item in deskPic['list']:
#     oriSize = item.get("oriSize")
#     imgsrc = item.get("imgsrc")
#     imgsrc = imgsrc.replace("##SIZE##", oriSize)
#     print(imgsrc)



#测试开发的代码
# # import re

# # url = "https://www.canva.cn/learn/classic-mobile-phone-wallpaper/"
# # resp = requests.get(url)
# f = open(r"./day04/test.txt", mode="r", encoding='utf-8')
# pageSource = f.read()
# # 定义两个字符串
# start_str = "<link rel=\"preload\" href=\""
# end_str = "\""

# # 编写正则表达式
# regex_pattern = rf"{start_str}(.*?){end_str}"
# # 使用re.search方法进行搜索
# result = re.findall(regex_pattern, pageSource)
# # 如果找到匹配，提取子串
# if result:
#     content = result
#     print(content)
# else:
#     print("No content found between the strings.")

# # import os
# # current_path = os.getcwd()
# # print(current_path)
