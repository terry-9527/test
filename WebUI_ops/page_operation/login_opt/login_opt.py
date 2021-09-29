from WebUI_ops.common import keywords
from WebUI_ops.page_location.login_location.login_lct import LoginLocation
from WebUI_ops.common.keywords import KeyWords

class LoginOperation(KeyWords):

    def __init__(self,driver):
        super(LoginOperation, self).__init__(driver)
        self.lct = LoginLocation()

    # 输入手机号码
    def input_phone(self, phone):
        self.clear(*self.lct.phone)
        self.input_text(*self.lct.phone, phone)
        # self.driver.find_element(*self.lct.phone).clear()
        # self.driver.find_element(*self.lct.phone).send_keys(phone)

    # 输入密码
    def input_pwd(self, pwd):
        self.clear(*self.lct.password)
        self.input_text(*self.lct.password, pwd)
        # self.driver.find_element(*self.lct.password).clear()
        # self.driver.find_element(*self.lct.password).send_keys(pwd)

    def click_login_button(self):
        self.click_element(*self.lct.login_button)
        # self.driver.find_element(*self.lct.login_button).click()


if __name__ == '__main__':
    url = "https://opstest.arsyun.com/#/"
    driver = keywords.init_driver("Firefox")
    login_opt = LoginOperation(driver)
    login_opt.open_browser(url)
    login_opt.wait(2)
    login_opt.input_phone("18276762767")
    login_opt.input_pwd("aa123456")
    login_opt.click_login_button()
    login_opt.wait(2)
    login_opt.close_browser()
