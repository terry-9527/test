import json
import unittest, requests
from operation_system.common.get_data import GetData
from ddt import data, ddt, file_data, unpack
from operation_system.common.get_token import get_token
import yaml
from operation_system.common.login import login

@ddt
class ModifyUserInfo(unittest.TestCase):

    def setUp(self):
        # login("18276762767","aa123456")
        pass

    def tearDown(self):
        pass

    def set_info(self,username):
        with open(r'E:\Appium_project\operation_system\data\get_user_info.yaml','r',encoding="utf-8") as stream:
            file = yaml.load(stream,Loader=yaml.FullLoader)
            file['case01']['excepted']['username'] = username
            stream.close()
            # print(file)
        with open(r'E:\Appium_project\operation_system\data\get_user_info.yaml', 'w+', encoding="utf-8") as stream:
            yaml.dump(file,stream)
            stream.close()

    @data(*GetData().getYamlData('modify_user_info.yaml'))
    def test_case01(self, args):
        # print(args)
        self.url = args['url']
        self.params = args['params']
        self.Authorization = "Bearer " + get_token()
        self.headers = {
            "Authorization": self.Authorization,
            "Content-Type": "application/json"
        }
        res = requests.put(url=self.url, data=json.dumps(self.params), headers=self.headers)
        print(res.json())
        self.assertEqual(args['excepted']['status_code'],res.status_code)
        if args['case_name'] == "修改用户email信息":
            self.assertEqual(args['excepted']['email'], res.json()['data']['email'])
        elif args['case_name'] == "修改用户username信息":
            self.assertEqual(args['excepted']['username'], res.json()['data']['username'])
            username = res.json()['data']['username']
            self.set_info(username)
            print(username)
        else:
            self.assertEqual(args['excepted']['phone'], res.json()['data']['phone'])



if __name__ == '__main__':
    unittest.main(verbosity=2)
