import unittest

from selenium import webdriver

from WebUI_ops.common import keywords
from WebUI_ops.common.get_data import GetData
from WebUI_ops.common.public import start_sshtunnel, connect_database, stop_sshtunnel, init_database


class BaseUtil(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_database('initsqls.txt')
        # # 获取数据库初始化sql语句
        # sqls = GetData().read_sqls('initsqls.txt')
        # start_sshtunnel()
        # conn = connect_database()
        # cursor = conn.cursor()
        # for sql in sqls:
        #     cursor.execute(sql)
        # conn.commit()
        # conn.close()
        # stop_sshtunnel()

    def setUp(self):
        login_url = "https://opstest.arsyun.com/#/"
        self.driver = keywords.init_driver("Chrome")
        self.driver.get(login_url)


    def tearDown(self):
        # 退出浏览器
        self.driver.quit()
