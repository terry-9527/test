from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

desired_capabilities={
    "platformName":"Android",
    "platformVersion":"8.0",
    "deviceName":"Android Emulator",
    "appPackage":"com.android.contacts",
    "appActivity":"activities.PeopleActivity",
    "automationName":"UiAutomator2",#测试自动化引擎
    "unicodeKeyboard":True,
    "resetKeyboard":True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities)
#操作
TouchAction(driver).tap(x=676, y=1091).perform()
sleep(2)
el2 = driver.find_element_by_id("com.android.contacts:id/left_button")
el2.click()
sleep(2)
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]")
el3.send_keys("测试账号001")
sleep(2)
el4 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[2]")
el4.send_keys("paoshou602")
sleep(2)
el5 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText")
el5.send_keys("18276762767")
sleep(2)
el6 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText")
el6.send_keys("4522155@qq.com")
sleep(2)
TouchAction(driver).press(x=550, y=804).move_to(x=541, y=454).release().perform()
sleep(2)
TouchAction(driver).press(x=463, y=988).move_to(x=476, y=622).release().perform()
sleep(2)
el7 = driver.find_element_by_xpath("(//android.widget.Spinner[@content-desc=\"电话\"])[2]")
el7.click()
sleep(2)
el8 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]")
el8.click()
sleep(2)
el9 = driver.find_element_by_id("com.android.contacts:id/editor_menu_save_button")
el9.click()
sleep(2)

#wait 3s
sleep(3)
#退出APP
driver.quit()
