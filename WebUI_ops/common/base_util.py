import unittest

from selenium import webdriver

from WebUI_ops.common import keywords


class BaseUtil(unittest.TestCase):
    def setUp(self):
        login_url = "https://opstest.arsyun.com/#/"
        self.driver = keywords.init_driver("Chrome")
        self.driver.get(login_url)


    def tearDown(self):
        # 退出浏览器
        self.driver.quit()
