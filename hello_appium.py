from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Desired Capabilities (change these as per your setup)
desired_caps = {
    "platformName": "Android",
    "platformVersion": "11.0",         # Your device Android version
    "deviceName": "Android Emulator",  # or real device name
    "browserName": "Chrome",           # Using Chrome browser
    "automationName": "UiAutomator2"
}

# Connect to Appium Server
driver = webdriver.Remote("http://localhost:8080, desired_caps)

# Open the URL
driver.get("https://the-internet.herokuapp.com/")

# Verify Title
assert "Internet" in driver.title

# Find element by TAG_NAME
title = driver.find_element(AppiumBy.TAG_NAME, "h1")

# Assert text inside <h1>
assert "Suresh" in title.text

# Quit session
driver.quit()
