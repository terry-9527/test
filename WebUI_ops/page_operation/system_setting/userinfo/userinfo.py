'''
定义用户信息页面的操作，封装到一个类中
'''
from WebUI_ops.common import keywords
from WebUI_ops.page_location.system_setting.userinfo.userinfo import UserInfoLocation
from WebUI_ops.common.keywords import KeyWords
from WebUI_ops.page_operation.login_opt.login_opt import LoginOperation

class UserInfoOperation(KeyWords):

    def __init__(self,driver):
        super(UserInfoOperation, self).__init__(driver)
        self.lct = UserInfoLocation()

    # 点击系统设置 ('xpath', "//span[text()='系统设置']")
    def click_system_setting(self):
        self.click_element(*self.lct.system_setting)

    # 点击用户信息
    def click_userinfo(self):
        self.click_element(*self.lct.userinfo)

    # 点击新建用户
    def click_new_user(self):
        self.click_element(*self.lct.new_user)



if __name__ == '__main__':
    url = "https://opstest.arsyun.com/#/"
    driver = keywords.init_driver("Chrome")
    lg = LoginOperation(driver)
    lg.open_browser(url)
    lg.input_phone("18276762767")
    lg.input_pwd('aa123456')
    lg.click_login_button()
    lg.wait(2)
    ui = UserInfoOperation(driver)
    ui.click_system_setting()
    ui.wait(2)
    ui.click_userinfo()
    ui.wait(2)
    ui.click_new_user()


