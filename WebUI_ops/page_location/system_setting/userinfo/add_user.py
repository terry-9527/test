from selenium.webdriver.common.by import By


class UserInfoLocation():
    def __init__(self):
        # 系统设置xpath定位信息：//span[text()='系统设置']
        self.system_setting = (By.XPATH, "//span[text()='系统设置']")
        # 用户信息xpath定位信息：//span[text()='用户信息']
        self.userinfo = (By.XPATH, "//span[text()='用户信息']")
        # 新建用户xpath定位信息：//span[text()='新建用户']
        self.new_user = (By.XPATH, "//span[text()='新建用户']")

