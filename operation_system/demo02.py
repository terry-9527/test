import openpyxl
from operation_system.common.connect_database import connect_database,stop_server,start_server
from operation_system.common.login import login
#初始化一个工作簿，选择打开对应的文件
# workbook = openpyxl.load_workbook('testcase1.xlsx')
# sheetname = workbook.sheetnames     #获取工作表名称
# sheet = workbook[sheetname[0]]      #执行使用哪个工作表
# rows = sheet.rows   #取出所有行的数据
# cases = []
# #遍历每一行的数据
# for row in rows:
#     list1 = []
#     for col in row: #获取当前行每一个单元格，单元格的内容需要用value
#         list1.append(col.value)
#     cases.append(list1)
# print(cases)

# sqlfile = open('opsmysql.txt','r',encoding='utf-8')
# start_server()
# conn = connect_database()
# cursor = conn.cursor()
# for sql in sqlfile:
#     if not sql.startswith('--') and len(sql.strip()) >0:
#
#         cursor.execute(sql)
#         conn.commit()
#
# conn.close()
# stop_server()
#
# res = login('15522223333','aa123456')
# print(res)
import requests
import json
import unittest
from ddt import data,unpack,ddt
from operation_system.common.connect_database import *

jsonfile = open('testjson.json','r',encoding='utf-8')
cases = json.load(jsonfile)
jsonfile.close()

@ddt
class Demo01(unittest.TestCase):
    @data(*cases['testcase'])
    @unpack
    def test_demo01(self,args,expected):
        url = "https://opstest.arsyun.com/api/v1/auth/login"
        argument = json.dumps(args)
        res = requests.post(url=url, data=argument,)
        print(res.text)

        self.assertEqual(expected['expected'],res.json()['description'])
        if expected['expected'] == '登录成功':
            start_server()
            conn = connect_database()
            cursor = conn.cursor()
            sql = "select * from users where phone='18276762767'"
            cursor.execute(sql)
            user_id = cursor.fetchone()[0]
            print(user_id)
            if user_id == res.json()['data']['user_id']:
                print("落库检查成功，登陆的用户ID是："+ str(user_id))
            conn.close()
            stop_server()





