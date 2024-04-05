from concurrent.futures import ThreadPoolExecutor
import requests
import re
import json


def download(imgsrc):
    name = imgsrc.split("/")[-1]
    print(f"准备开始下载{name}")
    # 1. 发送网络请求.
    resp_img = requests.get(imgsrc)
    # 2. 此时拿不到resp.text
    # resp.content -> 拿到文件的字节
    with open(f"img/{name}", mode="wb") as f:
        f.write(resp_img.content)
    print(f"{name}下载完毕!")


def main():
    url = "https://desk.zol.com.cn/bizhi/9374_114228_2.html"
    resp = requests.get(url)
    obj = re.compile(r"var deskPicArr.*?=(?P<deskPicArr>.*?);", re.S)
    result = obj.search(resp.text)
    deskPicStr = result.group("deskPicArr")  # 从正则.*?提取的内容一定是字符串

    # 把类似字典的字符串真的变成字典
    deskPic = json.loads(deskPicStr)

    with ThreadPoolExecutor(10) as t:
        for item in deskPic['list']:
            oriSize = item.get("oriSize")
            imgsrc = item.get("imgsrc")
            imgsrc = imgsrc.replace("##SIZE##", oriSize)
            t.submit(download, imgsrc)
    print("all over!")


if __name__ == '__main__':
    main()








