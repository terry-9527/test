import os, logging
import logging.handlers
import datetime

# pwd = os.getcwd()
# logfile = os.path.join(os.path.dirname(pwd), "log", "out.log")
# print(logfile)
# # logging.basicConfig(level=50)
# # LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# # logging.basicConfig(filename=logfile, filemode='w', level=logging.INFO, format=LOG_FORMAT)  # 配置日志级别
# # logging.debug("this is a debug log")
# # logging.info("this is a info log")
# # logging.warning("this is a warning log")
# # logging.error("this is a error log")
# # logging.critical("this is a debug log")
#
# print(logging.getLogger())
import sys

"""
现在有以下几个日志记录的需求：

1）要求将所有级别的所有日志都写入磁盘文件中
2）all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
3）error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
4）要求all.log在每天凌晨进行日志切割
"""

logger = logging.getLogger("mylogger")  # 实例化一个自定义名为mylogger日志器
logger.setLevel(logging.DEBUG)  # 设置日志级别

all_handler = logging.handlers.TimedRotatingFileHandler("all.log", when="midnight", interval=1, backupCount=7,
                                                        atTime=datetime.time(0, 0, 0, 0))
all_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

err_handler = logging.FileHandler("err.log")
err_handler.setLevel(logging.ERROR)
err_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

# std_handler = logging.StreamHandler(sys.stdout)
# email_handler = logging.handlers.SMTPHandler(("smtphz.qiye.163.com", 25), 'terry.wei@arsyun.com', ['525155126@qq.com','morgan.chen@arsyun.com'],
#                                              'testing email', credentials=('terry.wei@arsyun.com', 'kV5YjQNaWfAn4Tt2'),timeout=30)
# email_handler.setLevel(logging.ERROR)
logger.addHandler(all_handler)
logger.addHandler(err_handler)
# logger.addHandler(std_handler)
# logger.addHandler(email_handler)

logger.debug('this is a DEBUG log')
logger.info('this is a INFO log')
logger.warning('this is a WARNING log')
logger.error('this is a ERROR log')
logger.critical('this is a CRITICAL log')
