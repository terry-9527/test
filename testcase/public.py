from selenium import webdriver
from time import sleep
import random
import sys
for i in range(1,2):
    x=random.randint(1,2)
    y=random.randint(1,2)


def setup(self):
    self.d = webdriver.Chrome()
    self.d.maximize_window()
    self.d.implicitly_wait(10)
    return self.d



def login(driver,username,password):
    '''登录'''
    driver.get('https://devppool.arsyun.com')
    sleep(1)
    driver.find_element_by_class_name("ant-input").send_keys(username)
    sleep(1)
    driver.find_element_by_css_selector('[type="password"]').send_keys(password)
    sleep(1)
    driver.find_element_by_css_selector('[type="button"]').click()


def open_index(self):
    '''登录'''
    self.d.get('https://devppool.arsyun.com')
    sleep(0.1)
    self.d.find_element_by_css_selector('.ant-input').send_keys('15170195695')
    sleep(0.1)
    self.d.find_element_by_css_selector('[type="password"]').send_keys('123456')
    sleep(0.1)
    self.d.find_element_by_css_selector('[type="button"]').click()
    sleep(3)


def add_user_action(driver,username,phone,email,):


    driver.find_element_by_css_selector('[maxlength="40"]').send_keys(username)
    sleep(1)
    driver.find_element_by_css_selector('[maxlength="11"]').send_keys(phone)
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/input').send_keys(email)
    sleep(1)
    driver.find_element_by_css_selector('.ant-select-selection-search-input').click()
    sleep(3)
    driver.find_elements_by_xpath('//div[@class="ant-select-item-option-content"]')[1].click()
    sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[5]/input').send_keys('123456')
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[6]/input').send_keys('123456')
    sleep(1)
    driver.find_element_by_css_selector('.ant-btn ant-btn-primary').click()
    sleep(1)


def Manage_this(self):
    '''管理'''
    self.d.find_elements_by_xpath('//*[@id="root"]/nav/div/ul/a[4]/li/div').click()
    sleep(2)
    self.d.find_element_by_css_selector('.add-staff-button').click()
