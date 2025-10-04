from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "Android Emulator",
    "browserName": "Chrome",
    "automationName": "UiAutomator2"
}
mybrowser = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
mybrowser.get("https://the-internet.herokuapp.com/")
assert "Internet" in mybrowser.title
title = mybrowser.find_element(By.TAG_NAME, 'h1')
assert 'Tanuj' in title.text
mybrowser.quit()
