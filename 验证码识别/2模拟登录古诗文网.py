import requests
from lxml import etree
from chaojiying import Chaojiying_Client  # 导入示例代码（同一目录）

parser = etree.HTMLParser(encoding='utf-8')  # 使etree不报错
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}
# 验证码图片的捕获与识别
url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
page_text = requests.get(url, headers).text
tree = etree.HTML(page_text, parser=parser)
code_img_src = "https://so.gushiwen.cn" + tree.xpath('//*[@id="imgCode"]/@src')[0]
code_img_data = requests.get(url=code_img_src, headers=headers).content
with open('./code.jpg', 'wb') as fp:
    fp.write(code_img_data)

# 调用平台的示例程序，进行验证码识别
chaojiying = Chaojiying_Client('xhj2501', '123456', '920383')  # 调用示例程序实例化对象(用户名，密码，软件ID)
im = open('./code.jpg', 'rb').read()  # 本地图片文件路径
result = chaojiying.PostPic(im, 1902)['pic_str']  # 1902 验证码类型
print(result)

# post请求的发送（模拟登录）
result = []
login_url = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
data = {
    "__VIEWSTATE": "D9Luch6enVx2a+yrJLYkM6VTTcvrL4Vt+z11857XGY2MYDM3tAAqixvSc6zfaXAzZ97Z5WwHL65HZ7jYIuK2DoGZnDKVIqr1GZRqyoI16AQ0VP9fGwYcj7i3FZ0=",
    "__VIEWSTATEGENERATOR": "C93BE1AE",
    "from": "http://so.gushiwen.cn/user/collect.aspx",
    "email": "18848497451",
    "pwd": "123456",
    "code": str(result),  # 验证码图片值
    "denglu": "登录"
}
response = requests.post(url=login_url, headers=headers, data=data)
login_page_text = response.text
print(response.status_code)  # 返回响应状态码，若为200，则post请求（模拟登录）成功
with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(login_page_text)
