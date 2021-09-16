from WebUI_ops.page_location.login_location.login_location import LoginLocation


class LoginOperation():

    def __init__(self, driver):
        self.driver = driver
        self.lct = LoginLocation()

    # 打开浏览器
    def open_broswer(self, url):
        self.driver.get(url)

    # 关闭浏览器
    def close_broswer(self):
        self.driver.quit()

    # 输入手机号码
    def input_phone(self, phone):
        self.driver.find_element(*self.lct.phone).clear()
        self.driver.find_element(*self.lct.phone).send_keys(phone)

    # 输入密码
    def input_pwd(self, pwd):
        self.driver.find_element(*self.lct.password).clear()
        self.driver.find_element(*self.lct.password).send_keys(pwd)

    def click_login_button(self):
        self.driver.find_element(*self.lct.login_button).click()
