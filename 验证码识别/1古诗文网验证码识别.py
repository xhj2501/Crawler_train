import requests
from lxml import etree
from chaojiying import Chaojiying_Client  # 导入示例代码（同一目录）

parser = etree.HTMLParser(encoding='utf-8')  # 使etree不报错
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
page_text = requests.get(url, headers).text
# 解析验证码图片img中src属性值
tree = etree.HTML(page_text, parser=parser)
code_img_src ="https://so.gushiwen.org"+ tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = requests.get(url=code_img_src, headers=headers).content
img_path = './code.jpg'
with open(img_path, 'wb') as fp:
    # 将验证码图片下载到本地
    fp.write(img_data)

# 调用平台的示例程序，进行验证码识别
chaojiying = Chaojiying_Client('xhj2501', '123456', '920383')  # 调用示例程序实例化对象(用户名，密码，软件ID)
im = open(img_path, 'rb').read()  # 本地图片文件路径
print("识别结果为："+chaojiying.PostPic(im, 1902)['pic_str'])  # 1902 验证码类型
