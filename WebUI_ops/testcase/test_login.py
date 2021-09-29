"""
    测试首页的登陆功能
"""
import unittest

from WebUI_ops.common import keywords
from WebUI_ops.page_operation.login_opt.login_opt import LoginOperation
from WebUI_ops.common.get_data import GetData
from ddt import ddt, data, unpack


@ddt
class Login(unittest.TestCase):

    def setUp(self):
        url = "https://opstest.arsyun.com/#/"
        self.driver = keywords.init_driver('Chrome')
        self.login_opt = LoginOperation(self.driver)
        self.login_opt.open_browser(url)

    def tearDown(self):
        # 登陆成功后等待3秒退出浏览器
        self.login_opt.wait(2)
        self.login_opt.close_browser()

    # 读取Excel表中的用例数据
    cases = GetData().getExcel('logincase.xlsx')

    @data(*cases)
    def test01_loggin(self, args):


        # 输入手机号码
        print("开始执行用例：" + args[0] + ":" + str(args[1]))
        self.login_opt.input_phone(args[2]['phone'])
        # 输入密码
        self.login_opt.input_pwd(args[2]['password'])
        # 点击登陆按钮
        self.login_opt.wait(2)
        self.login_opt.click_login_button()
        self.login_opt.wait(2)

        if args[0] == 'login-001':
            # 检查登录成功的消息提示框
            success_msg = self.login_opt.locator('xpath', "//span[contains(text(),'登录成功')]").text
            self.assertEqual(success_msg, "登录成功", msg="登陆失败")
            # 断言 查看登陆成功后显示的用户名username
            actual = self.login_opt.locator('xpath', "//div[@class='username']/span").text
            self.assertEqual(actual, "Terry2", msg="用户登陆失败")
        elif args[0] == 'login-002':
            # 错误文字提示元素XPATH定位://div[text()='手机号不能为空']
            err_msg = self.login_opt.locator('xpath', "//div[text()='手机号不能为空']").text
            self.assertEqual(args[3], err_msg, msg="断言失败")
        elif args[0] == 'login-003':
            # 错误文字提示元素XPATH定位://div[text()='密码不能为空']
            err_msg = self.login_opt.locator('xpath', "//div[text()='密码不能为空']").text
            self.assertEqual(args[3], err_msg, msg="断言失败")
        elif args[0] == 'login-004':
            # 错误文字提示元素XPATH定位://div[text()='手机号不能为空']
            err_msg = self.login_opt.locator('xpath', "//div[text()='手机号不能为空']").text
            self.assertEqual(args[3]['err_msg1'], err_msg, msg="断言失败")
            # 错误文字提示元素XPATH定位://div[text()='密码不能为空']
            err_msg = self.login_opt.locator('xpath', "//div[text()='密码不能为空']").text
            self.assertEqual(args[3]['err_msg2'], err_msg, msg="断言失败")


if __name__ == '__main__':
    unittest.main()
