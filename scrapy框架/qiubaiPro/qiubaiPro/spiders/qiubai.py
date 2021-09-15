# -*- coding: utf-8 -*-
import scrapy
from qiubaiPro.items import QiubaiproItem  # 导入item类

"""xpath存在问题"""


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qiushibaike.com/text/']

    """基于终端指令的数据持久化存储"""
    # def parse(self, response):
    #     # 解析内容:作者+段子内容
    #     div_list = response.xpath('//*[@id="content"]/div/div[2]')
    #     all_data = []  # 存储所有解析到的数据
    #     for div in div_list:
    #         # xpath返回的是列表，但是列表元素一定是Selector类型的对象
    #         # extract可以将Selector对象中data参数存储的字符串提取出来
    #         author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         # 列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #         dic = {
    #             'author': author,
    #             'content': content
    #         }
    #         all_data.append(dic)
    #
    #     return all_data

    """基于管道的数据持久化存储"""

    def parse(self, response):
        # 解析内容:作者+段子内容
        div_list = response.xpath('//*[@id="content"]/div/div[2]')
        all_data = []  # 存储所有解析到的数据
        for div in div_list:
            # xpath返回的是列表，但是列表元素一定是Selector类型的对象
            # extract可以将Selector对象中data参数存储的字符串提取出来
            author = div.xpath('./div[1]/a[2]/h2/text()|./div[1]/span/h2/text()')[0].extract()
            # 列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)

            # 将解析数据封装到item对象中
            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            yield item  # 将item提交给了管道
