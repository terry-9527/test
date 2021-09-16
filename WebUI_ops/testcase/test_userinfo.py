from selenium import webdriver
import unittest
from WebUI_ops.page_location.system_setting.userinfo.add_user import UserInfoLocation
from WebUI_ops.common.public import Public
from time import sleep


class UserInfo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.login = Public(self.driver).login()
        self.lct_userinfo = UserInfoLocation()

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    def test_add_user(self):
        self.system_setting = self.driver.find_element("xpath", "//span[text()='系统设置']")
        self.system_setting.click()
        self.userinfo = self.driver.find_element("xpath", "//span[text()='用户信息']")
        self.userinfo.click()
        self.new_user = self.driver.find_element("xpath", "//span[text()='新建用户']")
        self.new_user.click()
        # el = self.driver.find_elements("xpath","//span[@class='ant-select-selection-item']")[1]
        el = self.driver.find_elements("xpath","//span[@class='ant-select-selection-item']")[1]
        el.click()
        sleep(2)
        el.send_keys('ARS')
        sleep(2)
        # el.send_keys("测试人员")
        # sleep(2)
        # el2 = self.driver.find_element('xpath', "//*[@aria-activedescendant='owned_customer_list_5']")
        # el2.click()
        # sleep(2)


if __name__ == '__main__':
    unittest.main()
