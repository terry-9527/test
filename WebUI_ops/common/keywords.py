'''
定义一个关键字类，封装公用的关键字函数：
打开浏览器： open_browser
定位元素: locator
输入内容：input_text
点击元素: click_element
等待时间：wait
退出浏览器： close_browser
清除输入框： clear
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class KeyWords():
    def __init__(self, url, driver_type):
        self.driver = self.init_driver(driver_type)
        self.driver.implicitly_wait(10)
        self.open_browser(url)
        self.driver.maximize_window()

    # 初始化浏览器，若传入的浏览器驱动存在，则启动对应的浏览器，否则默认启动谷歌浏览器
    def init_driver(self, driver_type):
        try:
            self.driver = getattr(webdriver, driver_type)()
            return self.driver
        except Exception as e:
            print("输入的浏览器驱动不可用，正在为您启动Google浏览器", e)
            self.driver = webdriver.Chrome()
            return self.driver

    # 打开浏览器
    def open_browser(self, url):
        self.driver.get(url)

    # 定位元素: locator，传入定位方式、定位信息 self.phone = (By.XPATH, "//input[@id='phone']")
    def locator(self, locator_type, location):
        try:
            if locator_type.upper() == "ID":
                element = self.driver.find_element(By.ID, location)
                return element
            elif locator_type.upper() == "NAME":
                element = self.driver.find_element(By.NAME, location)
                return element
            elif locator_type.upper() == "CLASS_NAME":
                element = self.driver.find_element(By.CLASS_NAME, location)
                return element
            elif locator_type.upper() == "TAG_NAME":
                element = self.driver.find_element(By.TAG_NAME, location)
                return element
            elif locator_type.upper() == "LINK_TEXT":
                element = self.driver.find_element(By.LINK_TEXT, location)
                return element
            elif locator_type.upper() == "PARTIAL_LINK_TEXT":
                element = self.driver.find_element(By.PARTIAL_LINK_TEXT, location)
                return element
            elif locator_type.upper() == "XPATH":
                element = self.driver.find_element(By.XPATH, location)
                return element
            elif locator_type.upper() == "CSS_SELECTOR":
                element = self.driver.find_element(By.CSS_SELECTOR, location)
                return element
        except Exception as e:
            print(e, "定位元素失败,定位方式{},定位信息{}".format(locator_type, location))

    # 输入内容：input_text
    def input_text(self, locator_type, location, content):
        self.locator(locator_type, location).send_keys(content)

    # 清除输入框
    def clear(self, locator_type, location):
        self.locator(locator_type, location).clear()

    # 点击元素: click_element
    def click_element(self, locator_type, location):
        self.locator(locator_type, location).click()

    # 设置等待时间
    def wait(self, second):
        time.sleep(second)

    # 关闭浏览器
    def close_browser(self):
        self.driver.quit()


if __name__ == '__main__':
    url = "https://www.baidu.com"
    kd = KeyWords(url, 'Chrome')
    kd.input_text('name', 'w1d', '倚天屠龙记')
    kd.click_element('id', 'su')
    kd.wait(2)
    kd.close_browser()
