from selenium.webdriver.common.by import By


class UserInfoLocation():
    def __init__(self):
        # 系统设置xpath定位信息：//span[text()='系统设置']
        self.system_setting = ('xpath', "//span[text()='系统设置']")
        # 用户信息xpath定位信息：//span[text()='用户信息']
        self.userinfo = ('xpath', "//span[text()='用户信息']")
        # 新建用户xpath定位信息：//span[text()='新建用户']
        self.new_user = ('xpath', "//span[text()='新建用户']")
        # 所属客户下拉框 (By.XPATH, '//span[@class="ant-select-selection-item"]')
        self.customer = ('xpath', "//span[@class='ant-select-selection-item']")
        # 用户名输入框
        self.username = ('id', "name")
        # 手机号输入框
        self.telephone = ('id', "phone")
        # 邮箱输入框
        self.email = ('id', "email")
        # 角色输入框
        self.role = ('xpath', "//span[@class='ant-select-selection-item']")
        # 密码输入框
        self.password = ('xpath', "//input[@id='password']")
        # 取消按钮
        self.cancle_button = ('xpath', "//button[@class='ant-btn']")
        # 确定按钮
        self.confirm_button = ('xpath', "//button[@class='ant-btn ant-btn-primary']")
        # X按钮
        self.quit_button = ('xpath', "//span[@class='ant-modal-close-x']")
        # 新建用户成功弹窗文本内容
        self.success_msg = ('xpath','//*[contains(text(),"我知道了")]')
