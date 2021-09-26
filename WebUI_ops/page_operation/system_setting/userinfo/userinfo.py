'''
定义用户信息页面的操作，封装到一个类中
'''
from WebUI_ops.common import keywords
from WebUI_ops.page_location.system_setting.userinfo.userinfo import UserInfoLocation
from WebUI_ops.common.keywords import KeyWords
from WebUI_ops.page_operation.login_opt.login_opt import LoginOperation


class UserInfoOperation(KeyWords):

    def __init__(self, driver):
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

    # 输入所属用户,暂时定位不到
    def input_customer(self):
        pass

    # 输入用户名 多个同属性的元素定位方式
    def input_username(self, username):
        self.clear(*self.lct.username)
        self.locators(*self.lct.username)[1].send_keys(username)

    # 输入手机号
    def input_phone(self, phone):
        self.input_text(*self.lct.telephone, phone)

    # 输入邮箱
    def input_email(self, email):
        self.input_text(*self.lct.email, email)

    # 输入角色，暂时无法定位
    def input_role(self, role):
        # self.input_text(*self.lct.role, role)
        pass

    # 输入密码
    def input_password(self, password):
        self.clear(*self.lct.password)
        self.input_text(*self.lct.password, password)

    # 点击确定按钮
    def click_confirm_button(self):
        self.click_element(*self.lct.confirm_button)

    # 点击我知道了按钮
    def click_alert_confirm_button(self):
        self.click_element(*self.lct.success_msg)


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
    ui.wait(1)
    ui.click_new_user()
    ui.wait(1)
    ui.input_username('aaaaaa')
    ui.wait(1)
    ui.input_phone('13388889999')
    ui.wait(2)
    ui.input_email('88888@qq.com')
    ui.wait(2)
    ui.input_password('aa123456')
    ui.wait(2)
    ui.click_confirm_button()
    ui.wait(2)
    ui.click_alert_confirm_button()
    # ui.close_browser()
