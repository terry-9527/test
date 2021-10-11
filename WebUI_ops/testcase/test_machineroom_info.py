'''
机房信息页面的测试用例设计
'''
import unittest

from WebUI_ops.common import keywords
from WebUI_ops.page_operation.enginroom.machineroominfo_opt import MachineRoomInfoOperation
from WebUI_ops.page_operation.login_opt.login_opt import LoginOperation
from WebUI_ops.page_operation.system_setting.userinfo.userinfo_opt import UserInfoOperation
from ddt import ddt, data, unpack, file_data
from WebUI_ops.common.get_data import GetData

filename = 'machineroominfo.xlsx'


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

    cases = GetData().getExcel('新建机房信息', filename)

    @data(*cases)
    def test_add_machineroom(self, params):
        # 登陆用户，输入用户名和密码
        self.lg.login("18276762767", "aa123456")
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
        self.opt1.input_engin_room_name(params[2]['machineroom_name'])
        self.opt1.wait(1)
        # 输入机房所在地址
        self.opt1.input_address(params[2]['address'])
        self.opt1.wait(1)
        # 输入域名
        self.opt1.input_domain(params[2]['domain'])
        self.opt1.wait(1)
        # 勾选算力机调度是否可用复选框
        self.opt1.click_scheduling_checkbox(params[2]['check'])
        self.opt1.wait(1)
        # 点击确定按钮
        self.opt1.click_confirm_button()
        self.opt1.wait(2)
    #     # 断言
    #     if params[0] == "add-machineroom-001":
    #         try:
    #             self.assertEqual(params[3]['success_msg'], self.opt1.get_success_msg())
    #             self.opt1.click_success_confirm_button()
    #             GetData().writeExcel(filename, params[0], testresult="PASS")
    #         except Exception as e:
    #             GetData().writeExcel(filename, params[0], testresult="FAILED")
    #             raise e
    #     elif params[0] == "add-machineroom-002":
    #         try:
    #             self.assertEqual(params[3]['success_msg'], self.opt1.get_success_msg())
    #             self.opt1.click_success_confirm_button()
    #             GetData().writeExcel(filename, params[0], testresult="PASS")
    #         except Exception as e:
    #             GetData().writeExcel(filename, params[0], testresult="FAILED")
    #             raise e
    #
    #     elif params[0] == "add-machineroom-003":
    #         try:
    #             self.assertEqual(params[3]['success_msg'], self.opt1.get_success_msg())
    #             self.opt1.click_success_confirm_button()
    #             GetData().writeExcel(filename, params[0], testresult="PASS")
    #         except Exception as e:
    #             GetData().writeExcel(filename, params[0], testresult="FAILED")
    #             raise e
    #
    #     elif params[0] == "add-machineroom-004":
    #         try:
    #             self.assertEqual(params[3]['error_msg'], self.opt1.get_machineroom_noname_msg())
    #             GetData().writeExcel(filename, params[0], testresult="PASS")
    #         except Exception as e:
    #             GetData().writeExcel(filename, params[0], testresult="FAILED")
    #             raise e
    #
    #     elif params[0] == "add-machineroom-005":
    #         try:
    #             self.assertEqual(params[3]['error_msg'], self.opt1.get_machineroom_noaddress_msg())
    #             GetData().writeExcel(filename, params[0], testresult="PASS")
    #         except Exception as e:
    #             GetData().writeExcel(filename, params[0], testresult="FAILED")
    #             raise e
    #
    #     elif params[0] == "add-machineroom-006":
    #         try:
    #             self.assertEqual(params[3]['error_msg1'], self.opt1.get_machineroom_noname_msg())
    #             self.assertEqual(params[3]['error_msg2'], self.opt1.get_machineroom_noaddress_msg())
    #             GetData().writeExcel(filename, params[0], testresult="PASS")
    #         except Exception as e:
    #             GetData().writeExcel(filename, params[0], testresult="FAILED")
    #             raise e
    #
    #     elif params[0] == "add-machineroom-007":
    #         try:
    #             self.assertIn(params[3]['error_msg'], self.opt1.get_duplicatename_error_msg())
    #             self.opt1.click_success_confirm_button()
    #             GetData().writeExcel(filename, params[0], testresult="PASS")
    #         except Exception as e:
    #             GetData().writeExcel(filename, params[0], testresult="FAILED")
    #             raise e
    #
    #     elif params[0] == "add-machineroom-008":
    #         try:
    #             self.assertEqual(params[3]['success_msg'], self.opt1.get_success_msg())
    #             self.opt1.click_success_confirm_button()
    #             GetData().writeExcel(filename, params[0], testresult="PASS")
    #         except Exception as e:
    #             GetData().writeExcel(filename, params[0], testresult="FAILED")
    #             raise e
    #
    # # 编辑机房信息
    cases = GetData().getExcel('编辑机房信息', filename)
    @data(*cases)
    def test_edit_machineroom(self, params):
        self.lg.login("18276762767", "aa123456")
        self.lg.wait(2)
        # 点击系统信息
        self.ui.click_system_setting()
        self.ui.wait(2)
        # 点击机房信息
        self.opt1.click_engin_room_info()
        self.opt1.wait(1)
        # 点击编辑按钮
        self.opt1.click_edit_button()
        self.opt1.wait(1)
        # 重新输入机房名称
        self.opt1.input_engin_room_name(params[2]['machineroom_name'])
        self.opt1.wait(1)
        # 重新输入地址
        self.opt1.input_address("阿富汗王国")
        self.opt1.wait(1)
        # 重新输入域名
        self.opt1.input_domain("http://baidu.com")
        self.opt1.wait(1)
        # 点击确定按钮
        self.opt1.click_confirm_button()


if __name__ == '__main__':
    unittest.main()
