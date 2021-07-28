import requests
from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')  # 使etree不报错

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

# 爬取页面源码数据
url = "https://cd.58.com/ershoufang/"
page_text = requests.get(url=url, headers=headers).text

# 数据解析
tree = etree.HTML(page_text, parser=parser)
div_list = tree.xpath('//section[@class="list"]/div')  # 存储的是a标签对象
with open('58.txt', 'w', encoding='utf-8') as fp:
    for div in div_list:
        # 局部解析
        title = div.xpath('./a//div[@class="property-content-title"]/h3/text()')[0]  # './'相对地址
        price = str(div.xpath('./a//p[@class="property-price-total"]/span[1]/text()')[0]) + str(
             div.xpath('./a//p[@class="property-price-total"]/span[2]/text()')[0])
        print(title)
        print(price)
        print()
        fp.write(title)
        fp.write(price)
