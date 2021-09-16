import unittest
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestContactManager(unittest.TestCase):
    def setUp(self):
        desired_capabilities = {}
        desired_capabilities['automationName'] = 'Uiautomator2'
        desired_capabilities['platformName'] = 'Android'
        desired_capabilities['platformVersion'] = '8.0'
        desired_capabilities['deviceName'] = 'Android Emulator'
        desired_capabilities['appPackage'] = 'com.example.android.contactmanager'
        desired_capabilities['appActivity'] = '.ContactManager'
        desired_capabilities['unicodeKeyboard'] = True
        desired_capabilities['resetKeyboard'] = True
        desired_capabilities['newCommandTimeout'] = 180
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)

    def tearDown(self):
        sleep(2)
        self.driver.quit()
    def is_element_present(self,how,what):
        try:
            self.driver.find_element(how,what)
        except NoSuchElementException as e:
            print(e)
            return False
        return True
    def test_001(self):
        e1 = self.is_element_present(MobileBy.XPATH,'//android.widget.TextView[@text="测试账号001paoshou602"]')
        self.assertEqual(e1,True,msg="无此账号，添加失败！")
    def test_002(self):
        e1 = self.driver.find_element_by_id('showInvisible')
        e1.click()
        r_actual = e1.get_attribute("checked")
        self.assertEqual(r_actual,"true",msg="勾选失败！")
if __name__ == '__main__':
    unittest.main()