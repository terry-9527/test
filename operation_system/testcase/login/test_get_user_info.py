import unittest, requests
from operation_system.common.get_data import GetData
from ddt import data, ddt, file_data, unpack
from operation_system.common.get_token import get_token
from operation_system.common.format_response import format_response


@ddt
class GetUserInfo(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*GetData().getYamlData('get_user_info.yaml'))
    def test_case01(self, args):
        print(args)
        self.url = args['url']
        # self.params = args['params']
        self.token = "Bearer " + get_token()
        # print(self.Authorization)
        self.headers = {
            "Authorization": self.token
        }
        # print(self.token)
        # print(self.url, self.params, self.headers)
        res = requests.get(url=self.url, headers=self.headers)
        # print(res.json())
        format_response(res.text)
        self.assertEqual(args['excepted']['username'],res.json()['data']['username'])
        self.assertEqual(args['excepted']['phone'],res.json()['data']['phone'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
