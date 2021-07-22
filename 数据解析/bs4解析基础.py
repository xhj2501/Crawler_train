from bs4 import BeautifulSoup

# 将本地的html文档中的数据加载到该对象中
with open('./uestc.html', 'r', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup.a)  # soup.tagName返回的是html中第一次出现的tagName标签
    # print(soup.div)
    # print(soup.find('div'))  # find('tagName')等同于soup.div
    # print(soup.find('div', class_="title-l hide-line-tag"))  # 属性定位(class_/id/attr=)
    # print(soup.find_all('a'))  # find('tagName')返回符合要求的所有标签(列表)
    # print(soup.select('.outter'))  #select ('某种选择器(id/class/标签...选择器)'),返回的是一个列表。
    # print(soup.select('.outter > .content')[0])  # 层级选择器,'>'表示一个层级,' '表示多个层级
    # 获取标签中文本数据,soup.a.text/string/get_text()
    # text/get_text():可以获取某一个标签中所有的文本内容
    # string:只可以获取该标签下面直系的文本内容
    # print(soup.select('.outter > .content')[0].text)
    # print(soup.a['href'])  # 获取标签中属性值:soup.a['href']
