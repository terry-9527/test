import random

import pymysql
from selenium import webdriver
from sshtunnel import SSHTunnelForwarder

from WebUI_ops.common.get_data import GetData
from WebUI_ops.page_operation.login_opt.login_opt import LoginOperation

# 获取config.ini文件中数据库相关配置
conf = GetData()
host = conf.getConfigData("PublicCloud", "host")
port = conf.getConfigData("PublicCloud", "ssh_port")
user = conf.getConfigData("PublicCloud", "ssh_user")
password = conf.getConfigData("PublicCloud", "ssh_pwd")
dbuser = conf.getConfigData("PublicCloud", "dbuser")
dbpwd = conf.getConfigData("PublicCloud", "dbpwd")
dbname = conf.getConfigData("PublicCloud", "dbname")


class Public():
    phone = GetData().getConfigData('test_env', 'phone')
    password = GetData().getConfigData('test_env', 'password')

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def login(self, phone=phone, password=password):
        self.url = "https://opstest.arsyun.com/#/"
        # 打开首页登录界面
        self.driver.get(url=self.url)
        self.driver.maximize_window()
        self.opt = LoginOperation(self.driver)
        self.opt.login(phone, password)


def random_phone():
    list1 = ["135", "182", "147"]
    a = [random.choice("0123456789") for i in range(8)]
    phone = random.choice(list1) + "".join(a)
    return phone

# 创建SSH tunnel通道
def creat_sshtunnel():
    sshtunnel = SSHTunnelForwarder(
        ssh_address_or_host=host,  # 跳板机B地址
        ssh_port=port,  # 跳板机B端口
        ssh_username=user,  # 跳板机B账号
        ssh_password=password,  # 跳板机B密码
        local_bind_address=('127.0.0.1', 22),  # 这里必须填127.0.0.1
        remote_bind_address=('127.0.0.1', 3306)  # 目标机器A地址，端口
    )
    return sshtunnel


# 开启ssh tunnel服务通道
def start_sshtunnel():
    global sshtunnel
    sshtunnel = creat_sshtunnel()
    sshtunnel.start()
    # print("ssh tunnel start success!")


# 停止ssh tunnel服务通道
def stop_sshtunnel():
    sshtunnel.stop()
    # print("ssh tunnel stop success!")


# 连接数据库
def connect_database():
    conn = pymysql.connect(
        host='127.0.0.1',  # 这里必须填127.0.0.1
        port=22,  # 本地映射端口
        user=dbuser,  # 目标机器A账号
        password=dbpwd,  # 目标机器A密码
        db=dbname  # 目标机器A要连的库
    )
    return conn


def init_database(filename):
    # 获取数据库初始化sql语句
    sqls = GetData().read_sqls(filename)
    start_sshtunnel()
    conn = connect_database()
    cursor = conn.cursor()
    for sql in sqls:
        cursor.execute(sql)
    conn.commit()
    conn.close()
    stop_sshtunnel()

if __name__ == '__main__':
    # driver = webdriver.Chrome()
    # public = Public(driver)
    # print(public.password, public.phone)
    # public.login()
    # print(random_phone())
    start_sshtunnel()
    conn = connect_database()
    cursor = conn.cursor()
    sql = "SELECT miner_id FROM miners WHERE id >10"
    sql1 = "select count(username) from users where username='18276762767'"
    cursor.execute(sql1)
    # print(cursor.fetchone())
    # print(cursor.fetchone())
    # print(cursor.fetchone())
    result = cursor.fetchone()
    # for row in result:
    #     print(row)
    print(result[0])
    stop_sshtunnel()
