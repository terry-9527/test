"""
    测试首页的登陆功能
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from WebUI_ops.page_operation.login_opt.login_opt import LoginOperation
from WebUI_ops.common.get_data import GetData
from ddt import ddt, data, unpack


@ddt
class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://opstest.arsyun.com/#/"  #登陆首页的URL地址
        self.driver.implicitly_wait(10)     #设置隐士等待时间
        self.driver.get(url=self.url)       #打开首页
        self.opt = LoginOperation(self.driver)
        self.driver.maximize_window()   #网页窗口最大化

    def tearDown(self):
        # 登陆成功后等待3秒退出浏览器
        sleep(2)
        self.driver.quit()

    #读取Excel表中的用例数据
    cases = GetData().getExcel('logincase.xlsx')

    @data(*cases)
    def test01_loggin(self, args):
        # 输入手机号码
        print("开始执行用例：" + str(args[0]) + ":" + str(args[1]))
        self.opt.input_phone(eval(args[2])['phone'])
        # 输入密码
        self.opt.input_pwd(eval(args[2])['password'])
        # 点击登陆按钮
        sleep(2)
        self.opt.click_login_button()
        sleep(2)

        if str(args[0]) == 'login-001':
            # 检查登录成功的消息提示框
            success_msg = self.driver.find_element(By.XPATH, "//span[contains(text(),'登录成功')]").text
            self.assertEqual(success_msg,"登录成功",msg="登陆失败")
            # 断言 查看登陆成功后显示的用户名username
            username = self.driver.find_element(By.XPATH, "//div[@class='username']/span")
            actual = username.text
            self.assertEqual(actual, "Terry2", msg="用户登陆失败")
        elif str(args[0]) == 'login-002':
            # 错误文字提示元素XPATH定位://div[text()='手机号不能为空']
            err_msg = self.driver.find_element(By.XPATH, "//div[text()='手机号不能为空']").text
            self.assertEqual(args[3], err_msg, msg="断言失败")
        elif str(args[0]) == 'login-003':
            # 错误文字提示元素XPATH定位://div[text()='密码不能为空']
            err_msg = self.driver.find_element(By.XPATH, "//div[text()='密码不能为空']").text
            self.assertEqual(args[3], err_msg, msg="断言失败")
        elif str(args[0]) == 'login-004':
            # 错误文字提示元素XPATH定位://div[text()='手机号不能为空']
            err_msg = self.driver.find_element(By.XPATH, "//div[text()='手机号不能为空']").text
            self.assertEqual(eval(args[3])['err_msg1'], err_msg, msg="断言失败")
            # 错误文字提示元素XPATH定位://div[text()='密码不能为空']
            err_msg = self.driver.find_element(By.XPATH, "//div[text()='密码不能为空']").text
            self.assertEqual(eval(args[3])['err_msg2'], err_msg, msg="断言失败")

if __name__ == '__main__':
    unittest.main()
