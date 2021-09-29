from selenium.webdriver.common.by import By


class UserInfoLocation():
    def __init__(self):
        # 系统设置xpath定位信息：//span[text()='系统设置']
        self.system_setting = ('xpath', "//span[text()='系统设置']")
        # 用户信息xpath定位信息：//span[text()='用户信息']
        self.userinfo = ('xpath', "//span[text()='用户信息']")
        # 新建用户xpath定位信息：//span[text()='新建用户']
        self.new_user = ('xpath', "//span[text()='新建用户']")
        # 所属客户下拉框
        self.customer = ('xpath', "")
        # 用户名输入框
        self.username = ('xpath', "")
        # 手机号输入框
        self.telephone = ('xpath', "")
        # 邮箱输入框
        self.email = ('xpath', "")
        # 角色输入框
        self.role = ('xpath', "")
        # 密码输入框
        self.password = ('xpath', "")
        # 取消按钮
        self.cancle_button = ('xpath', "")
        # 确定按钮
        self.confirm_button = ('xpath', "")
