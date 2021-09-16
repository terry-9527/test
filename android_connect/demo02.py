from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
#启动计算器
desired_capabilities = {}
desired_capabilities['automationName'] = 'Uiautomator2'
desired_capabilities['platformName'] = 'Android'
desired_capabilities['platformVersion'] = '8.0'
desired_capabilities['deviceName'] = 'Android Emulator'
desired_capabilities['appPackage'] = 'com.android.calculator2'
desired_capabilities['appActivity'] = '.Calculator'
desired_capabilities['unicodeKeyboard'] = True
desired_capabilities['resetKeyboard'] = True
desired_capabilities['newCommandTimeout'] = 180
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities)
#操作
# n3 = driver.find_element(MobileBy.XPATH,'//android.view.ViewGroup[1]/android.widget.Button[8]')
n3 = driver.find_element_by_id('digit_3')
n3.click()





sleep(3)

driver.quit()