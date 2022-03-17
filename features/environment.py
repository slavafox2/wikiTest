from appium import webdriver
from selenium.webdriver.common.by import By 
from app.application import Application


def before_scenario(context, scenario):
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "11.0",
        "deviceName": "Android Emulator",
        "automationName": "UiAutomator2",
        "appWaitActivity": "*",
        "app": r"C:\...\PycharmProjects\wikiTest\app_apk\wikipedia-2-7-50391-huawei-2022-01-11.apk"
    }

    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
