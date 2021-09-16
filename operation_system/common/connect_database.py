import pymysql
from sshtunnel import SSHTunnelForwarder
from operation_system.common.get_data import GetData

# 读取配置文件数据
conf = GetData()
host = conf.getConfigData("PublicCloud", "host")
port = conf.getConfigData("PublicCloud", "ssh_port")
user = conf.getConfigData("PublicCloud", "ssh_user")
password = conf.getConfigData("PublicCloud", "ssh_pwd")
dbuser = conf.getConfigData("PublicCloud", "dbuser")
dbpwd = conf.getConfigData("PublicCloud", "dbpwd")
dbname = conf.getConfigData("PublicCloud", "dbname")


# 创建ssh tunell 通道
def creat_server():
    server = SSHTunnelForwarder(
        ssh_address_or_host=host,  # 跳板机B地址
        ssh_port=port,  # 跳板机B端口
        ssh_username=user,  # 跳板机B账号
        ssh_password=password,  # 跳板机B密码
        local_bind_address=('127.0.0.1', 22),  # 这里必须填127.0.0.1
        remote_bind_address=('127.0.0.1', 3306)  # 目标机器A地址，端口
    )
    return server


# 开启ssh tunnel服务通道
def start_server():
    global server
    server = creat_server()
    server.start()
    # print("ssh tunnel start success!")


# 停止ssh tunnel服务通道
def stop_server():
    server.stop()
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


if __name__ == '__main__':
    start_server()
    conn = connect_database()
    cursor = conn.cursor()
    sql = "select * from users where phone='15522223333'"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    conn.close()
    # server.stop()  # 这里要填stop,停止服务
    stop_server()  # 这里要填stop,停止服务
