import yaml

import requests
import unittest
from operation_system.common.get_data import GetData
from ddt import ddt, unpack, data, file_data
from operation_system.common.login import login
from operation_system.common.format_response import format_response

@ddt
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # login("18276762767","aa123456")
        pass

    @data(*GetData().getYamlData('login.yaml'))
    # @unpack
    def test_case01(self, args):
        self.url = args['url']
        self.params = args['params']
        res = requests.post(url=self.url, json=self.params)
        #判断登陆是否成功，如果登陆成功则更新token保存到yaml文件
        if res.json()['data']:
            self.token = {"token": res.json()['data']['token']}
            with open(r"E:\Appium_project\operation_system\config\api.yaml", "w", encoding="utf-8") as file:
                yaml.dump(self.token, file)

        # print(res.json())
        format_response(res.text)
        self.assertEqual(res.status_code, args['excepted']['status_code'], msg="请求响应异常")
        self.assertEqual(res.json()['description'], args['excepted']['description'], msg="登录失败")

if __name__ == '__main__':
    unittest.main(verbosity=2)
