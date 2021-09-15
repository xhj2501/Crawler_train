"""12306改版，放弃"""
import requests
from lxml import etree
from chaojiying import Chaojiying_Client  # 导入示例代码（同一目录）

# 调用平台的示例程序，进行验证码识别
chaojiying = Chaojiying_Client('xhj2501', 'xhj29752009.', '920383')  # 调用示例程序实例化对象(用户名，密码，软件ID)
im = open("./屏幕截图 2021-09-07 221700.png", 'rb').read()  # 本地图片文件路径
print(chaojiying.PostPic(im, 9004)['pic_str'])  # 9004验证码类型

