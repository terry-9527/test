import unittest

from ddt import ddt, data, unpack, file_data
from WebUI_ops.common.base_util import BaseUtil
from WebUI_ops.common.get_data import GetData
from WebUI_ops.page_operation.system_setting.userinfo.userinfo_opt import UserInfoOperation


@ddt
class UserInfo(BaseUtil):
    # 读取Excel表中的用例数据
    # cases = GetData().getExcel('adduser', 'userinfo.xlsx')
    # @data(*cases)
    # def test_add_user(self,params):
    #     self.userinfo_opt = UserInfoOperation(self.driver)
    #     # 先进行登陆，输入手机号和密码
    #     self.userinfo_opt.login("18276762767", "aa123456")
    #     # 依次点击系统设置--》用户信息--》新建用户
    #     self.userinfo_opt.click_system_setting()
    #     self.userinfo_opt.wait(2)
    #     self.userinfo_opt.click_userinfo()
    #     self.userinfo_opt.wait(2)
    #     self.userinfo_opt.click_new_user()
    #     self.userinfo_opt.wait(2)
    #     # 输入所属用户
    #     self.userinfo_opt.input_customer()
    #     self.userinfo_opt.wait(1)
    #     # 输入用户名
    #     self.userinfo_opt.input_username(params[2]['username'])
    #     self.userinfo_opt.wait(1)
    #     # 输入手机号码
    #     self.userinfo_opt.input_phone(params[2]['phone'])
    #     self.userinfo_opt.wait(1)
    #     # 输入邮箱
    #     self.userinfo_opt.input_email(params[2]['email'])
    #     self.userinfo_opt.wait(1)
    #     # 输入角色
    #     self.userinfo_opt.input_role()
    #     self.userinfo_opt.wait(1)
    #     # 输入密码
    #     self.userinfo_opt.input_password(params[2]['password'])
    #     self.userinfo_opt.wait(1)
    #     self.userinfo_opt.click_confirm_button()
    #     self.userinfo_opt.wait(1)
    #
    #     # 断言
    #     if params[0] == "adduser-001":
    #         self.userinfo_opt.click_alert_confirm_button()
    #         self.userinfo_opt.wait(2)
    #         self.assertEqual(self.userinfo_opt.get_success_msg(),params[3]['text'])
    #     if params[0] == "adduser-002":
    #         self.assertEqual(self.userinfo_opt.get_noname_errmsg(),params[3]['text'])
    #     if params[0] == "adduser-003":
    #         self.assertEqual(self.userinfo_opt.get_nophone_errmsg(),params[3]['text'])
    #     if params[0] == "adduser-004":
    #         self.assertEqual(self.userinfo_opt.get_noemail_errmsg(),params[3]['text'])
    #     if params[0] == "adduser-005":
    #         self.assertEqual(self.userinfo_opt.get_nopassword_errmsg(),params[3]['text'])

    cases = GetData().getExcel('edituser', 'userinfo.xlsx')

    @data(*cases)
    def test_edit_userinfo(self, params):
        caseinfo = "测试用例ID："+params[0] + " ：" + params[1]
        print(caseinfo)
        self.userinfo_opt = UserInfoOperation(self.driver)
        # 先进行登陆，输入手机号和密码
        self.userinfo_opt.login("18276762767", "aa123456")
        # 依次点击系统设置--》用户信息--》点击编辑按钮
        self.userinfo_opt.click_system_setting()
        self.userinfo_opt.wait(1)
        self.userinfo_opt.click_userinfo()
        self.userinfo_opt.wait(1)
        self.userinfo_opt.click_edit_button()
        self.userinfo_opt.wait(1)
        if params[0] == "edituser-001":
            # 输入新的用户名
            self.userinfo_opt.input_username(params[2]['username'])
            self.userinfo_opt.wait(1)
        if params[0] == "edituser-002":
            # 输入新的手机号码
            self.userinfo_opt.input_phone(params[2]['phone'])
            self.userinfo_opt.wait(1)
        if params[0] == "edituser-003":
            # 输入新的email地址
            self.userinfo_opt.input_email(params[2]['email'])
            self.userinfo_opt.wait(1)
        if params[0] == "edituser-004":
            # 输入新的密码
            self.userinfo_opt.input_password(params[2]['password'])
            self.userinfo_opt.wait(1)
        self.userinfo_opt.click_confirm_button()
        self.userinfo_opt.wait(1)


if __name__ == '__main__':
    unittest.main()
