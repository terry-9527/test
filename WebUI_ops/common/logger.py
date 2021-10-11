'''
定义一个log日志器函数
logger
handler
formatter
filter
'''
import datetime
import logging.handlers
import os
import sys

from WebUI_ops.common.get_data import GetData
from WebUI_ops.common.getpathInfo import getpathInfo

def getLogger():
    # 定义一个日志器
    logger = logging.Logger('ARS')
    # 获取config.ini配置文件中的日志器等级
    level = GetData().getConfigData('log','level')
    formatter = GetData().getConfigData('log', 'formatter')
    # 设置日志等级
    logger.setLevel(level)
    # 创建一个标准输出的日志处理器
    std_handler = logging.StreamHandler(sys.stdout)
    std_handler.setLevel(logging.DEBUG)
    std_handler.setFormatter(logging.Formatter(formatter))
    # 创建一个保存所有日志的处理器
    alllog = os.path.join(getpathInfo(), 'log', "all.log")
    time_rotating_handler = logging.handlers.TimedRotatingFileHandler(alllog, when="midnight", interval=1, backupCount=7,
                                              atTime=datetime.time(0, 0, 0, 0))
    time_rotating_handler.setLevel(logging.INFO)
    time_rotating_handler.setFormatter(logging.Formatter(formatter))
    # 创建一个错误日志处理器，保存到文件中
    errorlog = os.path.join(getpathInfo(),'log',"error.log")
    err_handler = logging.FileHandler(errorlog)
    err_handler.setLevel(logging.ERROR)
    err_handler.setFormatter(logging.Formatter(formatter))

    # logger.addHandler(err_handler)
    # logger.addHandler(time_rotating_handler)
    logger.addHandler(std_handler)
    return logger



if __name__ == '__main__':
    logger = getLogger()
    logger.debug("this is a debug log")
    logger.info("this is a info log")
    logger.warning("this is a warning log")
    logger.error("this is a error log")
    logger.critical("this is a critical log")


