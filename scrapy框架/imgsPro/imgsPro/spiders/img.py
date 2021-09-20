# -*- coding: utf-8 -*-
import scrapy


class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
