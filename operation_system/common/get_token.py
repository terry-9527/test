'''
封装登陆接口，返回token
'''
import yaml
import os


def get_token():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    file_dir = os.path.dirname(root_dir) + "/config/api.yaml"
    # print(file_dir)
    with open(file_dir, "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        file.close()
    return data['token']

if __name__ == '__main__':
    token = get_token()
    print(token)