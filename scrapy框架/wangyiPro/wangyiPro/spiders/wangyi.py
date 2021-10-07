# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    model_urls = []  # 存储五个板块对应详情页的url

    # 实例化一个浏览器对象
    def __init__(self):
        self.bro = webdriver.Chrome(
            executable_path='D:\study file\python project\Crawler_train\scrapy框架\wangyiPro\chromedriver.exe')

    # 解析五大板块对应详情页的url
    def parse(self, response):
        # 若运行报错，则根据网站情况更新下面的xpath地址格式
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        a_list = [2, 3, 5, 6, 7]
        for index in a_list:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)

        # 依次对每一个板块对应的页面进行请求
        for url in self.model_urls:
            yield scrapy.Request(url=url, callback=self.parse_model)

    # 解析每一个板块页面中对应新闻的标题和新闻详情页的url
    # 每一个板块对应的新闻标题相关的内容都是动态加载
    def parse_model(self, response):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath("./div/div[1]/h3/a/text()").extract_first()
            news_detail_url = div.xpath("./div/div[1]/h3/a/@href").extract_first()

            item = WangyiproItem()
            item['title'] = title

            # 对新闻详情页的url发起请求(使用请求传参)
            yield scrapy.Request(url=news_detail_url, callback=self.parse_detail, meta={'item': item})

    # 解析新闻内容
    def parse_detail(self, response):
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        item['content'] = content

        yield item

    # 爬虫结束后关闭浏览器
    def closed(self, spider):
        self.bro.quit()
