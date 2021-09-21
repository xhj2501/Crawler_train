# -*- coding: utf-8 -*-
import scrapy
from imgsPro.items import ImgsproItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="container"]/div')
        for div in div_list:
            # 注意：使用伪属性(src2)
            src = "https://" + div.xpath('./div/a/img/@src2').extract_first()

            item = ImgsproItem()  # 实例化item对象
            item['src'] = src

            yield item  # 提交item到管道
