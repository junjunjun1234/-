import requests
from lxml import etree
import re
import json
from concurrent.futures import ThreadPoolExecutor

domain = "https://desk.zol.com.cn"


def get_detail_href(url):
    """
    该函数负责获取到每一个详情页的href的值
    """
    resp = requests.get(url)
    resp.encoding = "gbk"
    et = etree.HTML(resp.text)
    hrefs = et.xpath("//ul[@class='pic-list2  clearfix']/li/a/@href")
    # 处理一下href. 需要添加域名
    new_hrefs = []
    for href in hrefs:
        new_hrefs.append(domain + href)
    return new_hrefs


def get_img_srcs(href):
    """
    访问每一个详情页. 得到每个详情页背后对应的一组图片的下载路径
    """
    resp = requests.get(href)
    resp.encoding = "gbk"
    obj = re.compile(r"var deskPicArr.*?=(?P<desk_str>.*?);", re.S)
    # 提取页面中关于图片路径的信息
    result = obj.search(resp.text).group("desk_str")
    desk_dict = json.loads(result)  # 把页面中提取到的字符串处理成字典
    img_src_list = []
    for item in desk_dict['list']:
        ori = item.get("oriSize")
        img_src = item.get("imgsrc")
        img_src = img_src.replace("##SIZE##", ori)
        img_src_list.append(img_src)
    return img_src_list


def download_img(img_src):
    """
    下载图片
    :param img_src:  xxxx
    """
    name = img_src.split("/")[-1]
    print(f"开始下载{name}")
    resp = requests.get(img_src)
    with open(f"img/{name}", mode="wb") as f:
        f.write(resp.content)
    print(f"{name}下载完毕!")


def main():
    for i in range(1, 10):
        url = "https://desk.zol.com.cn/pc/"
        if i !=1 :
            url = url + f"{i}.html"
        print(url)

        # 1. 抓取到首页中每个详情页的href
        print("抓取到首页中每个详情页的href......")
        hrefs = get_detail_href(url)
        print("抓取到首页中每个详情页的href......搞定!")

        print("访问每一个详情页. 得到每个详情页背后对应的一组图片的下载路径")
        img_list = []  # 装着所有的图片下载地址
        for href in hrefs:
            # 2. 访问每一个详情页. 得到每个详情页背后对应的一组图片的下载路径
            img_src_list = get_img_srcs(href)
            for img in img_src_list:
                img_list.append(img)
        print("访问每一个详情页. 得到每个详情页背后对应的一组图片的下载路径....搞定!!!")

        # 3. 开始下载图片
        with ThreadPoolExecutor(20) as t:
            for img in img_list:  # img: 图片下载路径
                t.submit(download_img, img)

        print("all over!!!")


if __name__ == '__main__':
    main()
