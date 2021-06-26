# 爬取电子科技大学首页的页面数据
import requests

# step_1:指定url
url = "https://www.uestc.edu.cn/"
# step_2:发起请求
response = requests.get(url=url)  # 返回一个响应对象
# step_3:获取响应数据
page_text = response.text  # 返回字符串形式的响应数据
print(page_text)
# step_4:持久化存储
with open('./uestc.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print("爬取数据结束。")
