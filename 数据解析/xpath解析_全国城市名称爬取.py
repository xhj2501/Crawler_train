import requests
from lxml import etree
import os

parser = etree.HTMLParser(encoding='utf-8')  # 使etree不报错
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

url = "https://www.aqistudy.cn/historydata/"
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text, parser=parser)

# # 解析热门城市名称
# hot_li_list = tree.xpath('//div[@class="hot"]//div[@class="bottom"]/ul/li')
# hot_city_names = []
# for li in hot_li_list:
#     hot_city_name = li.xpath('./a/text()')[0]
#     hot_city_names.append(hot_city_name)
#
# # 解析全部城市
# all_li_list=tree.xpath('//div[@class="all"]//div[@class="bottom"]/ul/div[2]/li')
# all_city_names = []
# for li in all_li_list:
#     city_name=li.xpath('./a/text()')[0]
#     all_city_names.append(city_name)
#
# print(hot_city_names,len(hot_city_names))
# print(all_city_names,len(all_city_names))

# 解析到热门城市和所有城市对应的a标签
# div/ul/li/a            热门城市a标签的层级关系
# div/ul/div[2]/li/a     全部城市a标签的层级关系
all_city_names = []
a_list = tree.xpath(
    '//div[@class="bottom"]/ul/li/a | //div[@class="all"]//div[@class="bottom"]/ul/div[2]/li/a')  # 使用逻辑货运算符
for a in a_list:
    city_name = a.xpath('./text()')[0]
    all_city_names.append(city_name)

print(all_city_names, len(all_city_names))
