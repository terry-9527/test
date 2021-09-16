from selenium import webdriver

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url)
