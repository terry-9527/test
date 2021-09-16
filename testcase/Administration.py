from selenium import webdriver
import time,unittest
from public import login
from public import add_user_action

#    '''登录'''
class user_test(unittest.TestCase):
    def setUp(self):
        self .dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.implicitly_wait(10)
        login(driver=self.dr,username='15170195695',password='123456')
        self.dr.find_element_by_xpath('//*[@id="root"]/nav/div/ul/a[4]/li/div').click()
        self.dr.find_element_by_css_selector('.add-staff-button').click()

    def tearDown(self):
        self.dr.quit()
    def test01(self):
        '''新建用户成功'''
        add_user_action(driver=self.dr,username='xh{0}'.format(int(time.time())),phone='{0}2'.format(int(time.time())),email='{0}@qq.com'.format(int(time.time())))
        msg=self.dr.find_element_by_css_selector('[style="width: 242px; padding-right: 40px;"]').text
        self.assertIn('系统运维',msg)

    def test02(self):
        '''姓名为空'''
        add_user_action(driver=self.dr,username='',phone='{0}2'.format(int(time.time())),email='{0}@qq.com'.format(int(time.time())))
        msg=self.dr.find_element_by_css_selector('.ant-message-notice').text
        self.assertIn('员工姓名不能为空',msg)

    def test03(self):
        '''手机号码为空'''
        add_user_action(driver=self.dr,username='xh{0}'.format(int(time.time())),phone='',email='{0}@qq.c om'.format(int(time.time())))
        msg=self.dr.find_element_by_css_selector('.ant-message-notice').text
        self.assertIn('手机号校验格式错误',msg)

    def test04(self):
        '''手机格式不正确'''
        add_user_action(driver=self.dr,username='xh{0}'.format(int(time.time())),phone='12345678911',emali='{0}@qq.com'.format(int(time.time())))
        msg=self.dr.find_element_by_css_selector('.ant-message-notice').text
        self.assertIn('手机号校验格式错误',msg)

    def test05(self):
        '''邮箱为空'''
        add_user_action(driver=self.dr,username='xh{0}'.format(int(time.time())),phone='{0}2'.format(int(time.time())),email='')
        msg=self.dr.find_element_by_css_selector('[style="width: 242px; padding-right: 40px;"]').text
        self.assertIn('系统运维',msg)

#    def test06(self):


if __name__=='__main__':
    unittest.main()