# import unittest
# from operation_system.common.login import login
#
# # login("18276762767","aa123456")
# testcase = unittest.defaultTestLoader.discover(r"E:\Appium_project\operation_system\testcase\login",pattern='*.py')
# suite = unittest.TestSuite()
# suite.addTest(testcase)
#
# runner = unittest.TextTestRunner()
# runner.run(testcase)

from HTMLTestRunner import HTMLTestRunner
import unittest
import time
from operation_system.testcase.login.test_login import Login
from operation_system.testcase.login.test_creat_user import CreatUser
from operation_system.testcase.login import test_modify_user_info,test_login



#discover方法搜索测试用例
case_path = "E:\\Appium_project\\operation_system\\testcase\\login"
discover = unittest.defaultTestLoader.discover(case_path,pattern="test_login.py")
case1 = unittest.defaultTestLoader.loadTestsFromTestCase(CreatUser)
case2 = unittest.defaultTestLoader.loadTestsFromTestCase(Login)
testcases = [case1,case2]

#测试套件
testsuite = unittest.TestSuite(discover)
# testsuite.addTest(discover)
# testsuite.addTest(case1)
# testsuite.addTest(case2)
# testsuite.addTests(testcases)
#html测试报告路径
report_path = "E:\\Appium_project\\operation_system\\report\\"
now = time.strftime("%Y-%m-%d_%H-%M-%S")
report_file = report_path + now + ".html"
print(report_file)
file = open(report_file,"wb")
html_runner = HTMLTestRunner(
    stream = file,
    title = "运维系统接口自动化测试报告",
    description = "测试接口"
)
html_runner.run(testsuite)
file.close()












#用HTMLTestRunner生成HTML测试报告
# from HTMLTestRunner import HTMLTestRunner
# import unittest
# import time
#
# if __name__ == "__main__":
#     #调用discovery方法，查找目录下所有以test开头的方法
#     search_path = "E:\Appium_project\operation_system\\testcase"
#     testcase = unittest.defaultTestLoader.discover(search_path,pattern="*.py")
#     report_path = "E:\Appium_project\operation_system\\report\\"
#     now = time.strftime("%Y-%m-%d_%H_%M_%S")
#     report_file = report_path + now +".html"
#     file = open(report_file,"wb")
#     html_runner = HTMLTestRunner(
#         stream=file,
#         title="系统登陆自动化测试报告",
#         description="我的自动化测试报告"
#     )
#     html_runner.run(testcase)
#     file.close()