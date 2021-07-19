import requests
import json

"""
动态加载数据
首页中对应的企业信息数据是通过ajax动态请求到的
"""
"""
http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=()
通过对详情页url的观察，发现url域名都是一样的，只有携带的参数(id)不一样
id值可以从首页对应的ajax请求到的json串中获取
域名和id值拼接出一个完整的企业对应的详情页的url
"""
"""
详情页的企业详情数据也是动态加载出来的
http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
所有post请求的url都是一样的，只有参数id值是不同的
如果我们可以批量获取多家企业的id后，就可以将id和url形成一个完整的详情页对应详情数据的ajax请求的url
"""

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}
# 批量获取不同企业的id值
url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
id_list = []  # 存储企业的id
all_data_list = []  # 存储所有的企业详情数据
# 参数的封装
for page in range(1, 6):
    page = str(page)
    data = {
        'on': 'true',
        'page': page,  # 爬取页数
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': ''
    }
    # 构建企业id列表
    json_ids = requests.post(url=url, headers=headers, data=data).json()  # 返回一个字典，字典中list是以字典为元素的列表，每个字典代表一家企业
    for dic in json_ids['list']:
        # 遍历列表中字典，将每个字典中企业id加入到列表中
        id_list.append(dic['ID'])

# 获取企业详情数据
post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for id in id_list:
    # 将每个id列表中的id作为参数发起ajax请求
    post_data = {
        'id': id
    }
    detail_json = requests.post(url=post_url, headers=headers, data=post_data).json()
    all_data_list.append(detail_json)

# 持久化存储
with open("allData.json", "w", encoding="utf-8") as fp:
    json.dump(all_data_list, fp=fp, ensure_ascii=False, indent=True)  # 利用indent自动换行
print("over!!")
