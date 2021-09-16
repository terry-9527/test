'''
登陆之后返回token
'''
import requests, yaml


def login(phone, password):
    url = "https://opstest.arsyun.com/api/v1/auth/login"
    data = {
        "phone": phone,
        "password": password
    }
    res = requests.post(url=url, json=data).json()
    if res['data']:
        # print(res['data'])
        token = {"token":res['data']['token']}
        # print(token)
        with open(r"E:\Appium_project\operation_system\config\api.yaml", "w", encoding="utf-8") as file:
            yaml_data = yaml.dump(token, file)

    else:
        print("login failed!")
    return res

#
if __name__ == '__main__':
    qqq = login("18276762767", "aa123456")
    print(qqq)