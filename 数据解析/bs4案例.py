# 爬取三国演义小说的所有的章节标题和章节内容
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}
# 对首页的页面数据进行爬取
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
page_text = requests.get(url=url, headers=headers).text.encode('ISO-8859-1')  # 防止乱码
# 在首页中解析出章节的标题和详情页的url
soup = BeautifulSoup(page_text, 'lxml')  # 实例化BeautifulSoup对象
li_list = soup.select('.book-mulu > ul > li')
with open('./sanguo.txt', 'w', encoding='utf-8') as fp:
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        # 对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url, headers=headers).text.encode('ISO-8859-1')
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        content = div_tag.text  # 解析到章节的内容
        fp.write(title + ':' + content + '\n')
        print(title, '爬取成功')
