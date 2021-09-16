"""
接口地址：http://v.juhe.cn/postcode/query
返回格式：json/xml
请求方式：http get/post
请求示例：http://v.juhe.cn/postcode/query?postcode=215001&key=申请的KEY
接口备注：通过邮编查询对应的地名
"""
import json
import jsonpath
import pytest
import requests
from android_connect.get_exceldata import get_excel_data

# def test_001():
#     list1 = get_excel_data("./testpost.xlsx")
#     for case in list1:
#         id = case.get('id')
#         url = case.get("url")
#         data = case.get("data")
#         excepted = json.loads(case.get("excepted"))
#         print(id,url,data,excepted)
#         res = requests.get(url,params=json.loads(data)) #get()方法中的params参数必须是字典类型
#         print(res.text)
#         if id == 1:
#             assert excepted.get("reason") == res.json()["reason"]
#             assert excepted.get("error_code") == res.json()["error_code"]
#         elif id == 2:
#             assert excepted.get("list") == None
#         else:
#             # assert excepted.get("excepted") == "错误的请求KEY!!"
#             assert "错误的请求KEY!!" in res.text
def test_001():
    list1 = get_excel_data("./testpost.xlsx")
    for case in list1:
        id = case[0]
        url = case[1]
        data = case[2]
        code = case[3]
        excepted = json.loads(case[4])
        # id = case.get('id')
        # url = case.get("url")
        # data = case.get("data")
        # excepted = json.loads(case.get("excepted"))
        print(id,url,data,code,excepted)
        res = requests.get(url,params=json.loads(data)) #get()方法中的params参数必须是字典类型
        print(res.text)
        print(jsonpath.jsonpath(res.json(),'$.reason'))
        # if id == 1:
        #     assert excepted.get("reason") == res.json()["reason"]
        #     assert excepted.get("error_code") == res.json()["error_code"]
        # elif id == 2:
        #     assert excepted.get("list") == None
        # else:
        #     # assert excepted.get("excepted") == "错误的请求KEY!!"
        #     assert "错误的请求KEY!!" in res.text
if __name__ == '__main__':
    pytest.main(["-s","./testpost.py"])