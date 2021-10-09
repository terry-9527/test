import unittest


from WebUI_ops.common.base_util import BaseUtil
from WebUI_ops.page_operation.login_opt.login_opt_v2 import LoginOperation
from WebUI_ops.page_operation.system_setting.userinfo.userinfo_opt import UserInfoOperation


class UserInfo(BaseUtil):


    def test_add_user(self):
        # 登陆流程，输入手机号和密码
        self.login_opt = LoginOperation(self.driver)
        self.login_opt.login("18276762767", "aa123456")

        # 依次点击系统设置--》用户信息--》新建用户
        self.userinfo_opt = UserInfoOperation(self.driver)
        self.userinfo_opt.click_system_setting()
        self.userinfo_opt.wait(2)
        self.userinfo_opt.click_userinfo()
        self.userinfo_opt.wait(2)
        self.userinfo_opt.click_new_user()
        self.userinfo_opt.wait(2)
        # 输入所属用户
        self.userinfo_opt.input_customer()
        self.userinfo_opt.wait(1)
        # 输入用户名
        self.userinfo_opt.input_username("terry001")
        self.userinfo_opt.wait(1)
        # 输入手机号码
        self.userinfo_opt.input_phone("18899991111")
        self.userinfo_opt.wait(1)
        # 输入邮箱
        self.userinfo_opt.input_email("arsyunxxx@163.com")
        self.userinfo_opt.wait(1)
        # 输入角色
        self.userinfo_opt.input_role()
        self.userinfo_opt.wait(1)
        # 输入密码
        self.userinfo_opt.input_password("aa123456")
        self.userinfo_opt.wait(1)
        self.userinfo_opt.click_confirm_button()
        self.userinfo_opt.wait(1)
        self.userinfo_opt.click_alert_confirm_button()
        self.userinfo_opt.wait(2)




if __name__ == '__main__':
    unittest.main()
