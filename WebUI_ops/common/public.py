from random import random
from selenium import webdriver
from WebUI_ops.common.get_data import GetData
from WebUI_ops.page_operation.login_opt.login_opt import LoginOperation


class Public():
    phone = GetData().getConfigData('test_env', 'phone')
    password = GetData().getConfigData('test_env', 'password')

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def login(self, phone=phone, password=password):
        self.url = "https://opstest.arsyun.com/#/"
        # 打开首页登录界面
        self.driver.get(url=self.url)
        self.driver.maximize_window()
        self.opt = LoginOperation(self.driver)
        self.opt.login(phone, password)

    def random_phone(self):
        list1 = ["135", "182", "147"]
        a = [random.choice("0123456789") for i in range(8)]
        print(a)
        phone = random.choice(list1) + "".join(a)
        print("-".join(a))
        return phone


if __name__ == '__main__':
    driver = webdriver.Chrome()
    public = Public(driver)
    print(public.password, public.phone)
    public.login()
