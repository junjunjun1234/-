from lxml import etree

# from lxml import html
# etree = html.etree

# 需要加载准备解析的数据
f = open("./day03/test.html", mode="r", encoding='utf-8')
pageSource = f.read()

# 加载数据, 返回element对象
et = etree.HTML(pageSource)

# xpath的语法
# result = et.xpath("/html")  # /html表示根节点
# result = et.xpath("/html/body")  # 表达式中间的/表示一层html节点
# result = et.xpath("/html/body/span")
# result = et.xpath("/html/body/span/text()")  # text()表示提取标签中的文本信息

# result = et.xpath("/html/body/*/li/a/text()")   # * 任意的. 通配符
# result = et.xpath("/html/body/*/li/a/@href")   # @表示属性
# result = et.xpath("//li/a/@href")   # // 表示任意位置
# result = et.xpath("//div[@class='job']/text()")  # [@xx=xxxx] 属性的限定
# print(result)


# 带循环的
result = et.xpath("/html/body/ul[1]")

for item in result:
    # href = item.xpath("./li/a/@href")[0]  # ./表示当前这个元素
    text = item.xpath("./li/a/text()")  # ./表示当前这个元素
    print(text)

#测试


# # result = et.xpath("//nav[@aria-labelledby=':Rmtm:']/div/div[@class='x5R8iMt']/div/ul[@class='FaNLQNG']")
# result = et.xpath("//ul[@class='FaNLQNG']")

# # ii = result[0]
# # print(len(result[0]))
# i=0
# for item in result:
#     i+=1
#     print('第'+str(i)+'次：')
#     href = item.xpath("./li/p/a/@href")
#     print(href)