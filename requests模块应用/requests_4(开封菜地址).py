import requests
import json

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx"
city_name = input("Please enter a city name:")
param = {
    'op': 'keyword',
    'keyword': city_name,
    'cname': '',
    'pid': '',
    'pageIndex': '1',  # 查找结果第几页
    'pageSize': '10'  # 一页显示多少个
}  # 所有参数都要有
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}
response = requests.post(url=url, params=param, headers=headers)

list_data = response.json()

with open(city_name + ".json", "w", encoding="utf-8") as fp:
    json.dump(list_data, fp=fp, ensure_ascii=False)

print("over!")
