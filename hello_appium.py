import time
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By

# BrowserStack credentials
BROWSERSTACK_USERNAME = "USERNAME"
BROWSERSTACK_ACCESS_KEY = "ACCESS_KEY"

# BrowserStack capabilities for Android Chrome
desired_cap = {
    "platformName": "android",
    "browserName": "chrome",
    "deviceName": "Samsung Galaxy S23 Ultra",
    "os_version": "13.0",
    "project": "HerokuApp Web Testing",
    "build": "Python-Appium-BS",
    "name": "Verify HerokuApp Homepage",
    "browserstack.debug": True,
    "browserstack.networkLogs": True
}

# Step 1: Create an AppiumOptions object
options = AppiumOptions()
options.load_capabilities(desired_cap)

# Step 2: Start Remote WebDriver session with options
driver = webdriver.Remote(
    command_executor=f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub.browserstack.com/wd/hub",
    options=options
)

# Open the website
driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)

# Title check
assert "Internet" in driver.title, f"Unexpected title: {driver.title}"

# Main title check
title = driver.find_element(By.TAG_NAME, "h1")
assert "Welcome to the-internet" in title.text, f"Main title mismatch: {title.text}"

# Subtitle check
subtitle = driver.find_element(By.TAG_NAME, "h2")
assert "Available Examples" in subtitle.text, f"Subtitle mismatch: {subtitle.text}"

# List items check
list_items = driver.find_elements(By.CSS_SELECTOR, "ul li")
assert len(list_items) == 44, f"Expected 44 list items, found {len(list_items)}"

print(" All checks passed successfully on mobile browser!")

# Close session
driver.quit()
