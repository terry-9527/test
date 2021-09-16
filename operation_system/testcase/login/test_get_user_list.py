import unittest
import json
from ddt import data, ddt, file_data, unpack
import requests
from operation_system.common.get_data import GetData
from operation_system.common.get_token import get_token
from operation_system.common.format_response import format_response


@ddt
class GetUserList(unittest.TestCase):

    @data(*GetData().getYamlData('get_user_list.yaml'))
    def test_case01(self, args):
        self.url = args['url']
        self.params = args['params']
        self.token = "Bearer " + get_token()
        self.headers = {
            "Authorization": self.token
        }
        res = requests.get(url=self.url, params=self.params, headers=self.headers)  #get方法中params 数据类型必须为字典
        # print(res.json())
        format_response(res.text)
        self.assertEqual(args['excepted']['status_code'], res.status_code)
        if args['desc'] == "获取单个用户列表":
            self.assertEqual(args['excepted']['total'], res.json()['data']['total'])
            self.assertEqual(args['excepted']['username'], res.json()['data']['list'][0]['username'])
        else:
            self.assertTrue(res.json()['data']['list'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
