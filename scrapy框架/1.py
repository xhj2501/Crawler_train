import requests
from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')  # 使etree不报错

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

# 爬取页面源码数据
url = 'http://www.qiushibaike.com/text/'
page_text = requests.get(url=url, headers=headers).text

# 数据解析
tree = etree.HTML(page_text, parser=parser)
div_list = tree.xpath('//*[@id="content"]/div/div[2]')
print(div_list)
for div in div_list:
    # xpath返回的是列表，但是列表元素一定是Selector类型的对象
    # extract可以将Selector对象中data参数存储的字符串提取出来
    print(div)
    author = div.xpath('./div[1]/a[2]/h2/text()')
    # 列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来
    content = div.xpath('./a[1]/div/span//text()')
    print(author, content)

