import configparser
import yaml,os


class GetData():

    #读取通用配置文件
    def getConfigData(self,section=None, option=None):
        # config = configparser.ConfigParser()
        config = configparser.RawConfigParser()
        data = config.read(r'E:\Appium_project\operation_system\config\config.ini')
        self.res = config.get(section, option)
        return self.res

    def getYamlData(self,file):
        # self.path = path
        root_dir = os.path.dirname(os.path.abspath(__file__))
        # print(root_dir)
        self.file_path = os.path.abspath(os.path.join(root_dir,'..')) + '\\data\\' + file
        # print(self.file_path)

        with open(self.file_path,'r',encoding='utf-8') as f:
            self.yaml_data = yaml.load(f,Loader=yaml.FullLoader)
            case_data = []
            for case in self.yaml_data.values():
                case_data.append(case)
            # print(case_data)
            f.close()
        return case_data

if __name__ == '__main__':
    data = GetData()
    result = data.getYamlData('login.yaml')
    print(result)
