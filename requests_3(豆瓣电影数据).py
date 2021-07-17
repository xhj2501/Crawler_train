import requests
import json

url = "https://movie.douban.com/j/chart/top_list"
param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '1',  # 从库中第几部电影取出
    'limit': '20'  # 一次请求取出的个数
}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}
response=requests.get(url=url,params=param,headers=headers)

list_data=response.json()

with open("./douban.json","w",encoding="utf-8") as fp:
    json.dump(list_data, fp=fp, ensure_ascii=False)

print("over!")
