'''
接口地址：http://apis.juhe.cn/fapig/football/query
返回格式：json
请求方式：http get/post
请求示例：http://apis.juhe.cn/fapig/football/query?key=&type=xijia
接口备注：根据联赛类型,查询近期赛程赛果。数据来源于网络整理，可能会有一定误差和延时。
'''
import openpyxl
import pytest
import requests


# def test_001():
#     url = "http://apis.juhe.cn/fapig/football/query"
#     test_data = {
#         "key":"3c9dc74d6574ea97ff33551aeb770dd1",
#         "type":"xijia"
#     }
#     result = requests.get(url,test_data)
# print(result.text)
# print(type(result.json()))

# print(type(result.json()["result"]))
# data = result.json()
# print(type(data))
# for key in data.keys():
#     print(key)
# for value in data.values():
#     print(value)
# print(list)
# assert result.json()["error_code"] == 0
# assert result.json()["reason"] == "查询成功!"
# assert result.json()["result"]["title"] == "西班牙足球甲级联赛"


# # 封装删除用户sql
# def delete_user(user):
#     sql = "delete from user where mobile = '%s'" % user
#     print("删除用户sql:%s" % sql)
# # 测试数据
# mobile_data = ["18200000000", "18300000000"]
#
# @pytest.fixture(scope="function", params=mobile_data)
# def users(request):
#     '''注册用户参数化'''
#     # 前置操作
#     delete_user(request.param)
#     yield request.param
#     # 后置操作
#     delete_user(request.param)
#
# def test_register(users):
#     print("注册用户：%s" % users)
#
# if __name__ == '__main__':
#     pytest.main(["-s","./test_football_league.py"])
def test_001():
    data = "dog"
    strings = "this is a '%s' " % data
    print(strings)

