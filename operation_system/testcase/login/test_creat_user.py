import json
import unittest, requests
from operation_system.common.get_data import GetData
from ddt import data, ddt, file_data, unpack
from operation_system.common.get_token import get_token
from operation_system.common.format_response import format_response
from operation_system.common.connect_database import *


@ddt
class CreatUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 1、连接数据库
        start_server()
        cls.conn = connect_database()
        cls.cursor = cls.conn.cursor()
        # 2、创建游标
        cls.cursor = cls.conn.cursor()
        # 3、sql语句
        cls.sql = "delete from users where phone='15522223333'"
        # 4、执行sql语句
        cls.cursor.execute(cls.sql)
        # 5、提交数据
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        # 6、关闭数据库
        cls.conn.close()
        stop_server()

    @data(*GetData().getYamlData('creat_user.yaml'))
    def test_case01(self, args):
        self.url = args['url']
        self.params = json.dumps(args['params'])
        self.token = "Bearer " + get_token()
        self.headers = {
            "Authorization": self.token
        }
        # print(self.url, self.params, self.token)
        res = requests.post(url=self.url, data=self.params, headers=self.headers)
        # print(res.text)
        format_response(res.text)

        self.assertEqual(args['excepted']['status_code'], res.status_code)
        if args['case_name'] == "新建用户":
            self.assertEqual(args['excepted']['username'], res.json()['data']['username'])
        else:
            self.assertEqual(args['excepted']['description'], res.json()['description'])
            if res.json()['data']:
                sql = "delete from users where phone={}".format(res.json()['data']['phone'])
                self.cursor.execute(sql)
                self.conn.commit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
