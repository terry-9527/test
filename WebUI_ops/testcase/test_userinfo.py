import unittest
from WebUI_ops.page_operation.login_opt.login_opt import LoginOperation
from WebUI_ops.page_operation.system_setting.userinfo.userinfo import UserInfoOperation
from WebUI_ops.common import keywords


class UserInfo(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(10)
    #     self.login = Public(self.driver).login()
    #     self.lct_userinfo = UserInfoLocation()
    #
    # def tearDown(self):
    #     sleep(2)
    #     self.driver.quit()

    def setUp(self):
        self.url = "https://opstest.arsyun.com/#/"
        self.driver = keywords.init_driver("Chrome")
        self.login_opt = LoginOperation(self.driver)
        self.userinfo_opt = UserInfoOperation(self.driver)
        self.login_opt.open_browser(self.url)

    def tearDown(self):
        self.userinfo_opt.close_browser()

    def test_add_user(self):
        self.login_opt.input_phone("18276762767")
        self.login_opt.input_pwd("aa123456")
        self.login_opt.click_login_button()
        self.login_opt.wait(2)
        self.userinfo_opt.click_system_setting()
        self.userinfo_opt.wait(2)
        self.userinfo_opt.click_userinfo()
        self.userinfo_opt.wait(2)
        self.userinfo_opt.click_new_user()
        self.userinfo_opt.wait(2)


if __name__ == '__main__':
    unittest.main()
