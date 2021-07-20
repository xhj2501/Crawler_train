# 如何爬取一张图片
import requests

url = 'https://pic.qiushibaike.com/system/pictures/12454/124549585/medium/6JHGUIAMHAOXVODH.jpg'
# content返回的是二进制形式的图片数据
# text (字符串) content (二进制) json() (对象)
img_data = requests.get(url=url).content

with open('./1.jpg', 'wb') as fp:  # 'wb'以二进制形式写入
    fp.write(img_data)
