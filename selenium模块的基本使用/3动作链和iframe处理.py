from selenium import webdriver
from selenium.webdriver import ActionChains  # 导入动作链对应的类
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver.exe')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# 如果定位的标签是存在于iframe标签之中，则需要使用如下方法进行标签定位
bro.switch_to.frame('iframeResult')  # 切换浏览器标签定位的作用域
div = bro.find_element_by_id('draggable')

# 利用动作链实现拖动滑块的操作
action = ActionChains(bro)  # 实例化一个动作链对象
action.click_and_hold(div)  # 点击长按指定的标签
for i in range(5):
    # 拖拽移动标签
    # move_by_offset(x,y)，x水平方向，y竖直方向
    action.move_by_offset(17,0).perform()  # perform()表示让动作链立即执行
    sleep(0.3)
action.release()  # 释放动作链

bro.quit()
