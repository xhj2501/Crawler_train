"""未找到可用IP，待续"""
import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

url="http://www.baidu.com/s?wd=ip"

page_text=requests.get(url=url, headers=headers,proxies={"http":"40.91.94.165"}).text

with open('ip.html','w',encoding='utf-8')as fp:
    fp.write(page_text)
