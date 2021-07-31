import requests
from lxml import etree
import os

parser = etree.HTMLParser(encoding='utf-8')  # 使etree不报错
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

# 创建一个文件夹
if not os.path.exists('./picLibs'):
    os.mkdir('./picLibs')

url = "https://pic.netbian.com/4kdongman/"
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text, parser=parser)  # 数据解析：src的属性值和alt的属性值
li_list = tree.xpath('//div[@class="slist"]//li')  # 一个图片信息存储在一个li标签中，解析提取所有的li标签
for li in li_list:
    img_src = "http://pic.netbian.com" + li.xpath('.//img/@src')[0]  # 拼接后得到图片的完整src
    img_name = li.xpath('.//img/@alt')[0] + '.jpg'  # 拼接后得到图片的完整名称
    img_name = img_name.encode('iso-8859-1').decode('gbk')  # 通用处理中文乱码的解决方案
    img_data = requests.get(url=img_src, headers=headers).content  # 请求图片进行持久化存储
    img_path = 'picLibs/' + img_name
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_name,'下载成功！！')
