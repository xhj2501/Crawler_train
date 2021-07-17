"""
post请求（携带了参数）
响应数据是一组json数据
"""
import requests
import json

# 指定url
post_url = "https://fanyi.baidu.com/sug"

# 进行UA伪装
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

# post请求参数处理（同get请求一致）
word=input("enter a word:")
data = {
    "kw": word
}

# 请求发送
response = requests.post(post_url, data=data, headers=headers)

# 获取响应数据：json()方法返回的是对象(obj)（如果确认响应数据是json类型的，才可以使用json()）
dic_obj = response.json()  # 字典对象
print(dic_obj)

# 进行持久化存储：存储为json文件
filename=word+'.json'
with open(filename,"w",encoding="utf-8") as fp:
    json.dump(dic_obj, fp=fp, ensure_ascii=False) # 中文不能使用asc码

print("over")
