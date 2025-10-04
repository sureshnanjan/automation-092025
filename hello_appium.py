from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Desired Capabilities
desired_caps = {
    "platformName": "Android",
    "platformVersion": "11",             # update to match your emulator/phone
    "deviceName": "Medium_Phone_API_36.1",  # your emulator/device name
    "browserName": "Chrome",
    "automationName": "UiAutomator2",
    # "chromedriverExecutable": r"C:\tools\chromedriver.exe"  # if needed
}

# Create options object (required in Selenium 4.25+)
chrome_options = Options()
for key, value in desired_caps.items():
    chrome_options.set_capability(key, value)

# Connect to Appium
driver = webdriver.Remote(
    command_executor="http://localhost:4723/wd/hub",
    options=chrome_options
)

# Open website
driver.get("https://the-internet.herokuapp.com/")

# Assert title
assert "Internet" in driver.title
title_el = driver.find_element(By.TAG_NAME, "h1")
print("Heading text:", title_el.text)

time.sleep(2)
driver.quit()
