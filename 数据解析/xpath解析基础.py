from lxml import etree

"""xpath路径可以网站直接复制"""
parser = etree.HTMLParser(encoding='utf-8')  # 使etree不报错
tree = etree.parse('cosmetic.html', parser=parser)  # 实例化etree对象，且将被解析的源码加载到了该对象中
# r = tree.xpath('/html/body/div')  # '/’：表示的是从根节点开始定位，表示的是一个层级。
# r = tree.xpath('/html//div')  # '//’：表示的是多个层级。
# r = tree.xpath('//div')  # '//’：可以表示从任意位置开始定位。
# r = tree.xpath('//div[@class="dzpzmain"]')  # 属性定位，tag[@attrName="attrValue"]
# r = tree.xpath('//div[@class="hzbtabs"]/span[1]')  # 索引定位，索引从1开始
# r = tree.xpath('//div[@class="hzbtabs"]/span[1]/text()')[0]  # 取文本：/text()标签中直系文本内容
# r = tree.xpath('//span[1]//text()')  # 取文本：//text()标签中非直系文本内容
r = tree.xpath('//div[@class="hzbtabs"]/input/@id')  # 去属性：/@attrName
print(r)
