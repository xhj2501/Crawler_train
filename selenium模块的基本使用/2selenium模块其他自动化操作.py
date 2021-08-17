from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver.exe')

bro.get('https://www.taobao.com/')

# 找到搜索框输入搜索内容
serach_input = bro.find_element_by_id('q')  # 标签定位
serach_input.send_keys('iphone')  # 标签交互

# 执行一组json程序，实现滚轮向下拖动的效果
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)

# 点击搜索按钮
btn = bro.find_elements_by_css_selector('.btn-search')  # 选择器
btn[0].click()

bro.get('https://www.baidu.com')
sleep(2)
bro.back()  # 回退操作
sleep(2)
bro.forward()  # 前进操作

sleep(5)

bro.quit()
