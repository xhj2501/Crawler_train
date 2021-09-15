from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='./chromedriver.exe')

bro.get("https://mail.qq.com/")

#找到账号密码登录按钮并点击（在iframe中）
bro.switch_to.frame('login_frame')  # 切换浏览器标签定位的作用域
a_tag=bro.find_element_by_id('switcher_plogin')
a_tag.click()

#账号密码输入
userName_tag=bro.find_element_by_id('u')
password_tag=bro.find_element_by_id('p')
sleep(1)
userName_tag.send_keys('1746114767@qq.com')
password_tag.send_keys('123456')
sleep(1)
btn=bro.find_element_by_id('login_button')
btn.click()

sleep(3)

bro.quit()


