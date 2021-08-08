"""爬取梨视频的视频数据"""
import requests
from lxml import etree
import random
import os
from multiprocessing.dummy import Pool

if not os.path.exists('./video'):
    # 创建文件夹存储视频
    os.mkdir('./video')

parser = etree.HTMLParser(encoding='utf-8')  # 使etree不报错
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3823.400 QQBrowser/10.7.4307.400'
}

# 请求访问，解析出视频详情页url以及视频名称
url = 'https://www.pearvideo.com/category_5'
response = requests.get(url=url, headers=headers)
page_text = response.text

tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li')

urls = []  # 储存所有视频的连接和名字
for li in li_list:
    new_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    # new_name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    # 这个方法行不通。因为mp4是动态加载出来的，因此需要抓包ajax请求中的url，不知道怎么用python抓包，用浏览器的抓包工具
    new_page_text = requests.get(url=new_url, headers=headers).text
    new_tree = etree.HTML(new_page_text)
    name = new_tree.xpath('//*[@id="detailsbd"]/div[1]/div[2]/div/div[1]/h1/text()')[0]+'.mp4'
    # print(name)

    # 通过抓包ajax得到一个可以发送的url和请求伪装的视频的url，
    id_ = str(li.xpath('./div/a/@href')[0]).split('_')[1]
    # 可发送请求的url
    ajax_url = 'https://www.pearvideo.com/videoStatus.jsp?'
    params = {
        'contId': id_,
        'mrd': str(random.random())
    }
    ajax_headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3823.400 QQBrowser/10.7.4307.400',
        'Referer': 'https://www.pearvideo.com/video_' + id_
    }
    # 加了'Referer': 'https://www.pearvideo.com/video_1708144'后就不会显示该视频已下架了
    dic_obj = requests.get(url=ajax_url, params=params, headers=ajax_headers).json()
    video_url = dic_obj["videoInfo"]['videos']["srcUrl"]

    # 此处视频地址做了加密即ajax中得到的地址需要加上cont-,并且修改一段数字为id才是真地址
    # 真地址："https://video.pearvideo.com/mp4/third/20201120/cont-1708144-10305425-222728-hd.mp4"
    # 伪地址："https://video.pearvideo.com/mp4/third/20201120/1606132035863-10305425-222728-hd.mp4"

    # 对获取的伪url进行处理，得到真url
    video_true_url = ''
    s_list = str(video_url).split('/')
    # print(s_list)
    for i in range(0, len(s_list)):
        if i < len(s_list) - 1:
            video_true_url += s_list[i] + '/'
        else:
            ss_list = s_list[i].split('-')
            # print(ss_list)
            for j in range(0, len(ss_list)):
                if j == 0:
                    video_true_url += 'cont-' + id_ + '-'
                elif j == len(ss_list) - 1:
                    video_true_url += ss_list[j]
                else:
                    video_true_url += ss_list[j] + '-'

    dic = {
        'name': name,
        'url': video_true_url
    }
    urls.append(dic)


# 使用线程池对视频数据进行请求(较为耗时的阻塞操作)
def get_video_data(dic_):
    url_ = dic_['url']
    print(dic_['name'], '正在下载.....')
    video_data = requests.get(url=url_, headers=headers).content
    video_path = './video/' + dic_['name']
    with open(video_path, 'wb') as fp:
        fp.write(video_data)
        print(dic_['name'], '下载成功!!!!!')


pool = Pool(4)
pool.map(get_video_data, urls)

pool.close()
pool.join()
