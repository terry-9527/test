'''
创建一个新用户
'''
import json
import requests
from operation_system.common.get_token import get_token


def creat_user(email, name, owned_customer, phone, role, password="aa123456"):
    url = "https://opstest.arsyun.com/api/v1/user"
    params = {
        "email": email,
        "name": name,
        "owned_customer": owned_customer,
        "password": password,
        "phone": phone,
        "role": role
    }
    token = "Bearer " + get_token()
    headers = {
        "Authorization": token
    }
    res = requests.post(url=url, data=json.dumps(params), headers=headers)
    return res.json()


if __name__ == '__main__':
    res = creat_user("aaaa@qq.com", "testxxx", 1, "13211113333", 2)
    print(res)