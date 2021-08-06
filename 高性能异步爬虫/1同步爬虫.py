import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

urls = [
    "https://www.uestc.edu.cn/",
    "https://cn.bing.com/",
    "https://www.csdn.net/"
]


def get_content(url):
    print("正在爬取：", url)
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.content


def parse_content(content):
    print("响应数据的长度为：", len(content))

for url in urls:
    content=get_content(url)
    parse_content(content)