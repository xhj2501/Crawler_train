import requests
import re
import os

# 创建一个文件夹保存所有的图片
if not os.path.exists('./1'):
    os.mkdir('./1')

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}
url = 'https://www.qiushibaike.com/imgrank/'
# 使用通用爬虫对url对应的一整张页面进行爬取
page_text = requests.get(url=url, headers=headers).text

# 使用聚焦爬虫将页面中所有的图片进行解析/提取
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'  # 使用正则表达式匹配图片数据所在标签(.*?)非贪婪匹配
img_src_list = re.findall(ex, page_text, re.S)  # 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表(re.S单行匹配，re.M多行匹配)
for src in img_src_list:
    src = "https:" + src  # 拼接出一个完整的图片url
    img_data = requests.get(url=src, headers=headers).content  # 请求到了图片的二进制数据
    img_name = src.split('/')[-1]  # 生成图片名称(使用原始名称)
    img_path = './1/' + img_name  # 图片存储路径
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_name, 'download successfully!!')
