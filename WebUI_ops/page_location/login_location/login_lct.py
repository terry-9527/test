"""
    首页登陆界面元素的定位信息
"""
from selenium.webdriver.common.by import By


class LoginLocation():
    # 定义构造函数__init__
    def __init__(self):
        # 手机号码输入框
        self.phone = ('xpath', "//input[@id='phone']")
        #密码输入框
        self.password = ('xpath',"//input[@id='password']")
        #登陆按钮
        self.login_button = ('xpath',"//button[@type='submit']")
