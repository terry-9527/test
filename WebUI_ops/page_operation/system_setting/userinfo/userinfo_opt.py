'''
定义用户信息页面的操作，封装到一个类中
'''
import random

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from WebUI_ops.common import keywords
from WebUI_ops.page_location.system_setting.userinfo.userinfo_lct import UserInfoLocation
from WebUI_ops.common.keywords import KeyWords
from WebUI_ops.page_operation.login_opt.login_opt import LoginOperation


class UserInfoOperation(KeyWords):

    lct = UserInfoLocation()
    def click_new_user_button(self):
        # 点击系统设置 ('xpath', "//span[text()='系统设置']")
        self.click_element(*self.lct.system_setting)
        self.wait(1)
        # 点击用户信息
        self.click_element(*self.lct.userinfo)
        self.wait(1)
        # 点击新建用户
        self.click_element(*self.lct.new_user)
        self.wait(1)


    # 点击系统设置 ('xpath', "//span[text()='系统设置']")
    def click_system_setting(self):
        self.click_element(*self.lct.system_setting)

    # 点击用户信息
    def click_userinfo(self):
        self.click_element(*self.lct.userinfo)

    # 点击新建用户
    def click_new_user(self):
        self.click_element(*self.lct.new_user)

    # 输入所属用户
    def input_customer(self):
        self.click_elements(*self.lct.customer,list_number=1)
        self.wait(1)
        self.click_elements(*self.lct.select_customer,list_number=random.randint(0,7))

    # 输入用户名 多个同属性的元素定位方式
    def input_username(self, username):
        self.locators(*self.lct.username)[1].send_keys(Keys.CONTROL, 'a')
        self.locators(*self.lct.username)[1].send_keys(Keys.DELETE)
        self.locators(*self.lct.username)[1].send_keys(username)

    # 输入手机号
    def input_phone(self, phone):
        self.force_clear(*self.lct.telephone)
        self.input_text(*self.lct.telephone, phone)

    # 输入邮箱
    def input_email(self, email):
        self.force_clear(*self.lct.email)
        self.input_text(*self.lct.email, email)

    # 输入角色
    def input_role(self):
        self.click_elements(*self.lct.role,list_number=2)
        self.wait(1)
        self.click_elements(*self.lct.select_role,list_number=random.randint(8,12))

    # 输入密码
    def input_password(self, password):
        self.force_clear(*self.lct.password)
        self.input_text(*self.lct.password, password)

    # 点击确定按钮
    def click_confirm_button(self):
        self.click_element(*self.lct.confirm_button)

    # 点击我知道了按钮
    def click_alert_confirm_button(self):
        self.click_element(*self.lct.success_msg)

    # 获取创建成功提示文本信息
    def get_success_msg(self):
        return self.locator(*self.lct.success_msg).get_attribute("textContent")

    # 获取用户名为空提示语
    def get_noname_errmsg(self):
        return self.locator(*self.lct.noname_errmsg).get_attribute("textContent")

    # 获取手机号为空提示语
    def get_nophone_errmsg(self):
        return self.locator(*self.lct.nophone_errmsg).get_attribute("textContent")

    # 获取邮箱为空提示语
    def get_noemail_errmsg(self):
        return self.locator(*self.lct.noemail_errmsg).get_attribute("textContent")

    # 获取密码为空提示语
    def get_nopassword_errmsg(self):
        return self.locator(*self.lct.nopassword_errmsg).get_attribute("textContent")

    # 点击用户信息编辑按钮
    def click_edit_button(self):
        self.locator(*self.lct.edit_user_button).click()

if __name__ == '__main__':
    url = "https://opstest.arsyun.com/#/"
    driver = keywords.init_driver("Chrome")
    driver.get(url)
    lg = LoginOperation(driver)
    lg.login("18276762767","aa123456")
    ui = UserInfoOperation(driver)
    ui.click_system_setting()
    ui.wait(2)
    ui.click_userinfo()
    ui.wait(1)
    ui.click_edit_button()
    ui.wait(1)
    element = driver.find_elements_by_css_selector('#name')
    ui.wait(1)
    # ui.input_username("BeJson001")
    ui.wait(2)
    ui.input_phone("18299997777")
    ui.wait(2)
    # ui.click_new_user()
    # ui.wait(1)
    # ui.input_username('aaaaaa')
    # ui.wait(1)
    # ui.input_phone('13388881111')
    # ui.wait(2)
    # ui.input_email('88888@qq.com')
    # ui.wait(2)
    # ui.input_password('aa123456')
    # ui.wait(2)
    # ui.click_confirm_button()
    # ui.wait(2)

    # ui.click_alert_confirm_button()
    ui.close_browser()
