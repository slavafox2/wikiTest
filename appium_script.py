from appium import webdriver
from selenium.webdriver.common.by import By 


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

driver.find_element(By.ID, 'org.wikipedia:id/search_container').click()
driver.find_element(By.ID, 'org.wikipedia:id/search_src_text').clear().send_keys('python')

text = driver.find_element(By.ID, 'org.wikipedia:id/page_list_item_title').text

assert 'Python' in text, f'Expected Pythton to be the text: {text}'

driver.close()


