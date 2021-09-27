'''
机房信息页面的测试用例设计
'''

import unittest

from WebUI_ops.common import keywords
from WebUI_ops.page_operation.enginroom.machineroominfo import MachineRoomInfoOperation
from WebUI_ops.page_operation.login_opt.login_opt import LoginOperation
from WebUI_ops.page_operation.system_setting.userinfo.userinfo import UserInfoOperation
from ddt import ddt, data, unpack, file_data
from WebUI_ops.common.get_data import GetData

@ddt
class TestMachineRoomInfo(unittest.TestCase):

    def setUp(self):
        self.driver = keywords.init_driver("Chrome")
        self.lg = LoginOperation(self.driver)
        self.ui = UserInfoOperation(self.driver)
        self.opt1 = MachineRoomInfoOperation(self.driver)
        self.url = "https://opstest.arsyun.com/#/"
        self.lg.open_browser(self.url)

    def tearDown(self):
        self.opt1.wait(2)
        self.opt1.close_browser()
    cases = GetData().getExcel('machineroominfo.xlsx')
    @data(*cases)
    def test_add_machineroom(self, params):
        # print(eval(params[2]))
        # 登陆用户，输入用户名和密码
        self.lg.input_phone("18276762767")
        self.lg.input_pwd('aa123456')
        self.lg.click_login_button()
        self.lg.wait(2)
        # 点击系统信息
        self.ui.click_system_setting()
        self.ui.wait(2)
        # 点击机房信息
        self.opt1.click_engin_room_info()
        self.opt1.wait(1)
        # 点击新建机房
        self.opt1.click_new_engin_room()
        self.opt1.wait(1)
        # 输入机房名称
        self.opt1.input_engin_room_name(eval(params[2])['machineroom_name'])
        self.opt1.wait(1)
        # 输入机房所在地址
        self.opt1.input_address(eval(params[2])['address'])
        self.opt1.wait(1)
        # 输入域名
        self.opt1.input_domain(eval(params[2])['domain'])
        self.opt1.wait(1)
        # 勾选算力机调度是否可用复选框
        self.opt1.click_scheduling_checkbox(eval(params[2])['check'])
        self.opt1.wait(1)
        # 点击确定按钮
        self.opt1.click_confirm_button()
        self.opt1.wait(3)
        if eval(params[2])['machineroom_name'] and eval(params[2])['address']:
        # 点击创建后弹窗提示的我知道了按钮
            self.opt1.click_success_confirm_button()
            self.assertEqual(eval(params[3])['success_msg'],self.opt1.get_success_msg(),msg="断言成功")

if __name__ == '__main__':
    unittest.main()
