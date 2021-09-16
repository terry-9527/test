from selenium import webdriver
import unittest,time
from public import login

class login_test(unittest.TestCase):
    def setUp(self):
        self.d = webdriver.Chrome()
        self.d.maximize_window()
        self.d.implicitly_wait(6)

    def tearDown(self):
        self.d.close()
        self.d.quit()
    #登录成功
    def test_login_success(self):
        login(driver=self.d,username='15170195695',password='123456')
        msg = self.d.find_element_by_css_selector(".choose").text
        self.assertIn('首页',msg)
    #用户名为空
    def test_login_username_empty(self):
        login(driver=self.d,username='',password='123456')
        msg = self.d.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/p').text
        self.assertIn('账号输入有误',msg)
    #密码为空
    def test_login_password_empty(self):
        login(driver=self.d,username='15170195695',password='')
        msg = self.d.find_element_by_css_selector(".error-tips").text
        self.assertIn('密码不能为空',msg)
    #用户名错误
    def test_login_fail(self):
        login(driver=self.d,username='15111111111',password='123456')
        msg = self.d.find_element_by_css_selector(".error-tips").text
        self.assertIn('找不到相关用户', msg)
    #密码错误
    def test_login_fali(self):
        login(driver=self.d,username='15170195695',password='12345678')
        msg = self.d.find_element_by_css_selector(".error-tips").text
        self.assertIn('手机号或密码错误',msg)


if __name__=='__main__':
    unittest.main()