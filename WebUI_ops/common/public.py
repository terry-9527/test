from selenium.webdriver.common.by import By
from selenium import webdriver
from WebUI_ops.page_operation.login_opt.login_opt import LoginOperation
from time import sleep


class Public():

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def login(self, phone='18276762767', password='aa123456'):
        self.url = "https://opstest.arsyun.com/#/"
        # 打开首页登录界面
        self.driver.get(url=self.url)
        self.driver.maximize_window()
        self.opt = LoginOperation(self.driver)
        # 输入手机号码
        self.opt.input_phone(phone)
        # 输入密码
        self.opt.input_pwd(password)
        # 点击登陆按钮
        sleep(1)
        self.opt.click_login_button()


if __name__ == '__main__':
    public = Public()
    public.login()
    public.driver.find_element()
