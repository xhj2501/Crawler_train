# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class QiubaiproPipeline(object):
    fp = None

    # 重写父类一个方法：该方法只在开始爬虫的时候被调用一次
    def open_spider(self, spider):
        print("开始爬虫......")
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')

    # 专门用来处理item对象
    # 改方法可以接收爬虫文件提交过来的item对象
    # 该方法每接收到一个item就会被调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ":" + content + '\n')
        return item

    def close_spider(self, spider):
        print('结束爬虫！')
        self.fp.close()

"""未完待续"""
# 管道文件中一个管道类对应将一组数据存储到一个平台或者载体中(数据库）
class mysqlPileLine(object):
    conn = None
    cursor=None
    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', db='qiubai')

    def process_item(self, item, spider):
        self.cursor=self.conn.cursor()
        self.cursor.execute('')
        return item
