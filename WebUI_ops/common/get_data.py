import configparser
import yaml, os
from openpyxl import load_workbook
from WebUI_ops.common.getpathInfo import getpathInfo
import pandas


class GetData():

    # 读取通用配置文件
    def getConfigData(self, section=None, option=None):
        # config = configparser.ConfigParser()
        config = configparser.RawConfigParser()
        data = config.read(r'E:\Appium_project\operation_system\config\config.ini')
        self.res = config.get(section, option)
        return self.res

    def getYamlData(self, file):
        # self.path = path
        root_dir = os.path.dirname(os.path.abspath(__file__))
        # print(root_dir)
        self.file_path = os.path.abspath(os.path.join(root_dir, '..')) + '\\data\\' + file
        # print(self.file_path)

        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.yaml_data = yaml.load(f, Loader=yaml.FullLoader)
            case_data = []
            for case in self.yaml_data.values():
                case_data.append(case)
            # print(case_data)
            f.close()
        return case_data

    def getExcel(self, file):
        root_path = getpathInfo()
        file_path = os.path.join(root_path, "testdata", file)
        workbook = load_workbook(file_path)
        sheetname = workbook.sheetnames  # 获取工作表名称
        sheet = workbook[sheetname[0]]  # 执行使用哪个工作表
        rows = sheet.rows  # 取出所有行的数据
        cases = []
        # 遍历每一行的数据
        for row in rows:
            list1 = []
            for col in row:  # 获取当前行每一个单元格，单元格的内容需要用value
                list1.append(col.value)
            cases.append(list1)
        # print(cases[1:])
        return cases[1:]


if __name__ == '__main__':
    data = GetData()
    # result = data.getYamlData('login.yaml')
    # print(result)
    cases = data.getExcel('machineroominfo.xlsx')
    print(cases)
    print(eval(cases[0][2])['check'])
    # print(type(eval(cases[2][2])))
