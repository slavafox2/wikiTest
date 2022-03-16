from appium import webdriver
import os
from selenium.webdriver.common.by import By  # https://appium.github.io/python-client-sphinx/webdriver.common.html#module-webdriver.common.appiumby
from appium.webdriver.common.appiumby import AppiumBy   # https://appium.github.io/python-client-sphinx/webdriver.common.html#module-webdriver.common.mobileby

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "11.0",
    "deviceName": "Android Emulator",
    # "deviceName": "Pixel",//
    "automationName": "UiAutomator2",
    # "automationName": "Appium",
    "appWaitActivity": "*",
    "app": r"C:\Users\SL\PycharmProjects\wikiTest\app_apk\wikipedia-2-7-50391-huawei-2022-01-11.apk"
}


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
driver.implicitly_wait(5)
driver.find_element(By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button').click()



# driver.find_element(By.ID, 'org.wikipedia:id/search_toolbar').clear()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'org.wikipedia:id/search_toolbar').clear()
# e = driver.find_element(By.ID, 'org.wikipedia:id/search_container').clear()

# print(driver.current_context)
# try:
#     e = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/androidx.cardview.widget.CardView/android.widget.TextView').clear()
#     e.send_keys('python')
# except:
#     print('not find')

driver.find_element(By.ID, 'org.wikipedia:id/search_container').click()
driver.find_element(By.ID, 'org.wikipedia:id/search_src_text').clear().send_keys('python')

text = driver.find_element(By.ID, 'org.wikipedia:id/page_list_item_title').text

assert 'Python' in text, f'Expected Pythton to be the text: {text}'



