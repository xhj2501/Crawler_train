import requests
from lxml import etree
import os

parser = etree.HTMLParser(encoding='utf-8')  # 使etree不报错
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

# 创建一个文件夹
if not os.path.exists('./CVs'):
    os.mkdir('./CVs')

N = 5  # 爬取页数
url = "https://sc.chinaz.com/jianli/free.html"
for i in range(1, N + 1):
    # 爬取多个页面中的简历
    if i == 1:
        url0 = url
    else:
        url0 = "https://sc.chinaz.com/jianli/free_" + str(i) + ".html"
    #解析页面，获取每个简历详情页地址
    page_text0 = requests.get(url=url0, headers=headers).text
    tree0 = etree.HTML(page_text0, parser=parser)
    url_list = tree0.xpath('//div[@id="main"]//a/@href')  # 解析出每一个模板的下载详情页
    url_list = list(set(url_list))  # 去除重复的网站
    for url1 in url_list:
        #获取每个简历详情页中的下载地址，下载简历并保寸
        url1 = "http:" + url1
        page_text1 = requests.get(url=url1, headers=headers).text
        tree1 = etree.HTML(page_text1, parser=parser)
        url_download = tree1.xpath('//ul[@class="clearfix"]/li[1]/a/@href')[0]
        document = requests.get(url=url_download, headers=headers).content
        document_name = tree1.xpath("//div[@class='bgwhite']//h1/text()")[0].strip() + '.rar'  # 简历文件格式为rar;去除空格
        document_name = document_name.encode('iso-8859-1').decode('utf-8')  # 通用处理中文乱码的解决方案(解码可修改)
        document_path = 'CVs/' + document_name
        with open(document_path, 'wb') as fp:
            fp.write(document)

        print(document_name, "下载成功!")
