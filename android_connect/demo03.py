import unittest

import ddt
import jsonpath
import requests
import configparser
import json

import yaml, os


class Conf(object):
    def __init__(self, file):
        self.file = file

    def readYaml(self, sec, key):
        with open(self.file, encoding='utf-8') as  fp:
            result = yaml.load(fp, Loader=yaml.FullLoader)
            return result[sec][key]

if __name__ == '__main__':
    conf = Conf('./yaml_test.yaml')
    result = conf.readYaml('Server','person')
    print(result)





# if __name__ == "__main__":
#     unittest.main()


















# conf = configparser.ConfigParser()
# #读取配置文件内容
# data = conf.read(r'E:\Appium_project\android_connect\config\config.ini')
# # sections = conf.sections()
# # options = conf.options('Default')
# # print(sections,options)
# url = conf.get('Default', 'url') + 'login'
# apikey = conf.get('Default','X-Api-Key')
# heards = {
#     'X-Api-Key': apikey
# }
# res = requests.get(url=url, headers=heards)
# js = res.json()
# print(js)
# print(res.headers['Content-Type'])
# print(res.status_code)
# js = res.json()
# out_json = json.dumps(js,indent=2)
# print(type(out_json))
# # print(out_json['login'])
# aa = json.loads(out_json,)
# print(aa)

# dict1 = {
#     "name": "paoshou602",
#     "ag2": 20,
#     "sex": "male",
#     "address": {
#         "city":"上海",
#         "street":"中山街"
#     }
# }
# a1 = json.dumps(dict1,ensure_ascii=False)
# print(a1)
# print(type(a1))
#
# js = json.dumps(dict1)
# print(js)
# print(dict1)
# res1 = res.json()
# print(res1)
# print(res1['login'][0]['name'])
# print(jsonpath.jsonpath(res1,'$..login[0]'))
# print(jsonpath.jsonpath(res1,'$..login[*].id'))