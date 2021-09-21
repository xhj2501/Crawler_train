# -*- coding: utf-8 -*-
import scrapy

"""缺少可靠ip，暂时无法成功"""
class MiddleSpider(scrapy.Spider):
    #爬取百度
    name = 'middle'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.baidu.com/s?wd=ip']

    def parse(self, response):
        page_text=response.text

        with open("./ip.html",'w',encoding='utf-8') as fp:
            fp.write(page_text)

