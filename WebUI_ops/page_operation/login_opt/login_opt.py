from WebUI_ops.common import keywords
from WebUI_ops.page_location.login_location.login_lct import LoginLocation
from WebUI_ops.common.keywords import KeyWords

class LoginOperation(KeyWords):
    lct = LoginLocation()
    # 登陆操作流程封装成一个方法
    def login(self,phone, password):
        # 输入手机号码
        self.clear(*self.lct.phone)
        self.input_text(*self.lct.phone, phone)
        self.wait(1)
        # 输入密码
        self.clear(*self.lct.password)
        self.input_text(*self.lct.password, password)
        self.wait(1)
        # 点击登陆按钮
        self.click_element(*self.lct.login_button)
        self.wait(2)
    # 检查登录成功的消息提示框
    def login_success(self):
        success_msg = self.locator('xpath', "//span[contains(text(),'登录成功')]").text
        return success_msg
    # 查看登陆成功后显示的用户名username
    def login_username(self):
        success_msg = self.locator('xpath', "//div[@class='username']/span").text
        return success_msg
    # 错误文字提示元素XPATH定位://div[text()='手机号不能为空']
    def nophone_errormsg(self):
        return self.locator('xpath', "//div[text()='手机号不能为空']").text
    # 错误文字提示元素XPATH定位://div[text()='密码不能为空']
    def nopassword_errormsg(self):
        return self.locator('xpath', "//div[text()='密码不能为空']").text

if __name__ == '__main__':
    url = "https://opstest.arsyun.com/#/"
    driver = keywords.init_driver("Chrome")
    opt = LoginOperation(driver)
    opt.open_browser(url)
    opt.login("18276762767", "aa123456")
    opt.wait(1)
    opt.close_browser()
