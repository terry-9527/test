import random
import unittest

from selenium.webdriver.common.by import By

from WebUI_ops.page_operation.login_opt.login_opt import LoginOperation
from WebUI_ops.page_operation.system_setting.userinfo.userinfo_opt import UserInfoOperation
from WebUI_ops.common import keywords


class UserInfo(unittest.TestCase):

    def setUp(self):
        self.url = "https://opstest.arsyun.com/#/"
        self.driver = keywords.init_driver("Chrome")
        self.login_opt = LoginOperation(self.driver)
        self.userinfo_opt = UserInfoOperation(self.driver)
        self.login_opt.open_browser(self.url)

    def tearDown(self):
        self.userinfo_opt.close_browser()

    def test_add_user(self):
        # 登陆流程，输入手机号和密码
        self.login_opt.input_phone("18276762767")
        self.login_opt.input_pwd("aa123456")
        self.login_opt.click_login_button()
        self.login_opt.wait(2)
        # 依次点击系统设置--》用户信息--》新建用户
        self.userinfo_opt.click_system_setting()
        self.userinfo_opt.wait(2)
        self.userinfo_opt.click_userinfo()
        self.userinfo_opt.wait(2)
        self.userinfo_opt.click_new_user()
        self.userinfo_opt.wait(2)
        el1 = self.driver.find_elements(By.XPATH, '//span[@class="ant-select-selection-item"]')[1]
        el1.click()
<<<<<<< HEAD
        self.userinfo_opt.wait(2)
        self.driver.find_elements_by_css_selector(".ant-select-item")[random.randint(1,8)].click()
        self.userinfo_opt.wait(2)
        self.driver.find_elements(By.XPATH, '//span[@class="ant-select-selection-item"]')[2].click()
        self.userinfo_opt.wait(2)
        self.driver.find_elements_by_css_selector(".ant-select-item")[random.randint(9,13)].click()
        self.userinfo_opt.wait(2)
=======
        self.userinfo_opt.wait(1)
        el1.click()


>>>>>>> tmp

if __name__ == '__main__':
    unittest.main()
