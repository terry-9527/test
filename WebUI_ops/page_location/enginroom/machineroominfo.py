'''
机房信息页面相关元素定位信息
'''
from WebUI_ops.common.keywords import KeyWords


class MachineRoomInfoLocation():

    def __init__(self):
        # 机房信息
        self.engin_room_info = ('xpath', '//span[@class="ant-menu-title-content" and text()="机房信息"]')

        # 新建机房
        self.new_engin_room = ('xpath', '//span[text()="新建机房"]')

        # 机房名称输入框
        self.roomname = ('xpath', '//input[@id="machine_name"]')

        # 机房所在地输入框
        self.address = ('xpath', '//input[@id="machine_site"]')

        # 域名输入框
        self.domain = ('xpath', '//input[@id="domain"]')

        # 算力机是否可调度复选框
        self.scheduling_checkbox = ('xpath', '//input[@id="scheduling"]')

        # 取消按钮
        self.cancle_button = ('xpath', '//span[text()="取 消"]')

        # 确定按钮
        self.confirm_button = ('xpath', '//span[text()="确 定"]')

        # 退出X按钮
        self.quit_button = ('xpath', '//span[@class="ant-modal-close-x"]')

        # 新建机房成功提示信息 //span[text()="新建机房成功"]
        self.success_msg = ('xpath', '//span[text()="新建机房成功"]')

        # "我知道了"按钮
        self.success_confirm_button = ('xpath', '//span[text()="我知道了"]')

        # 用户名为空错误提示信息 //div[text()="请输入机房名称"]
        self.machineroom_null = ('xpath', '//div[text()="请输入机房名称"]')

        # 机房所在地为空错误提示信息 //div[text()="请输入机房名称"]
        self.machineroom_null = ('xpath', '//div[text()="请输入机房所在地"]')
