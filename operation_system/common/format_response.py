"""
处理请求接口返回的数据，进行格式化处理
"""
import json
import requests


def login(phone, password):
    url = "https://opstest.arsyun.com/api/v1/auth/login"
    data = {
        "phone": phone,
        "password": password
    }
    res = requests.post(url=url, json=data)
    return res.text


def format_response(res):
    json_data = json.loads(res)
    json_data = json.dumps(json_data, indent=4, ensure_ascii=False)
    print(json_data)


if __name__ == '__main__':
    data = login("18276762767", "aa123456")
    format_response(data)
