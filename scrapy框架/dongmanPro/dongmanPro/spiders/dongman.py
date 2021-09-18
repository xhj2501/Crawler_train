# -*- coding: utf-8 -*-
import scrapy


class DongmanSpider(scrapy.Spider):
    name = 'dongman'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://pic.netbian.com/4kdongman/']

    # 生成一个通用的url模板
    url = 'https://pic.netbian.com/4kdongman/index_'+'%d'+'.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            img_name = li.xpath('./a/b/text()').extract_first()
            print(img_name+".jpg-----下载成功！")
        if self.page_num<=11:
            new_url = format(self.url%self.page_num)
            self.page_num+=1
            # 手动请求发送(callback回调函数专门用作于数据解析)
            yield scrapy.Request(url=new_url, callback=self.parse)
