from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from WebUI_ops.page_operation.login_opt.login_opt import LoginOperation

driver = webdriver.Chrome()
login = LoginOperation(driver)
url = "https://opstest.arsyun.com/#/"  # 登陆首页的URL地址
driver.implicitly_wait(10)  # 设置隐士等待时间
driver.get(url=url)  # 打开首页
driver.maximize_window()
login.input_phone('18276762767')
login.input_pwd('aa123456')
login.click_login_button()
# sleep(2)
# els = driver.find_element('xpath','//span[contains(text(),"1027")]/../..//button')
# els.click()
sleep(2)

system_setting = driver.find_element("xpath", "//span[text()='系统设置']")
system_setting.click()
sleep(2)
userinfo = driver.find_element("xpath", "//span[text()='用户信息']")

userinfo.click()
sleep(2)
new_user = driver.find_element("xpath", "//span[text()='新建用户']")
new_user.click()
sleep(2)

driver.quit()
