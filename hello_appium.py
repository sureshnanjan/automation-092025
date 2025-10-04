from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

# BrowserStack credentials
USERNAME = "sowmyas_wijLeD"
ACCESS_KEY = "BeMzwXpzzhxdyqHtLdit"

# Define capabilities using UiAutomator2Options
options = UiAutomator2Options()
options.platformName = "Android"
options.deviceName = "Google Pixel 7"
options.platformVersion = "13.0"
options.browserName = "Chrome"
options.automationName = "UiAutomator2"

options.set_capability("bstack:options", {
    "userName": USERNAME,
    "accessKey": ACCESS_KEY,
    "buildName": "Python Appium Demo",
    "sessionName": "Herokuapp Check"
})

# Connect to BrowserStack hub
driver = webdriver.Remote(
    command_executor="https://hub-cloud.browserstack.com/wd/hub",
    options=options
)

try:
    driver.get("https://the-internet.herokuapp.com/")

    # Title check
    assert "The Internet" in driver.title

    # Main title check
    title = driver.find_element(By.TAG_NAME, "h1")
    assert "Welcome to the-internet" in title.text

    # Subtitle check
    subtitle = driver.find_element(By.TAG_NAME, "h2")
    assert "Available Examples" in subtitle.text

    # List items check
    list_items = driver.find_elements(By.CSS_SELECTOR, "ul li")
    assert len(list_items) > 0, "❌ No examples found!"

    print("✅ All checks passed successfully on BrowserStack!")

finally:
    driver.quit()

# import ssl
# import certifi
# import urllib3
# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from selenium.webdriver.common.by import By
#
# # ✅ Force urllib3 + SSL to use certifi certificates
# urllib3.disable_warnings()
# ssl_context = ssl.create_default_context(cafile=certifi.where())
#
# # 🔑 Step 1: Add your BrowserStack credentials
# BROWSERSTACK_USERNAME = "sowmyas_wijLeD"
# BROWSERSTACK_ACCESS_KEY = "BeMzwXpzzhxdyqHtLdit"
#
# # 🔑 Step 2: Define capabilities using UiAutomator2Options
# options = UiAutomator2Options()
# options.set_capability("platformName", "Android")
# options.set_capability("deviceName", "Google Pixel 7")   # Use trial device
# options.set_capability("platformVersion", "13.0")
# options.set_capability("browserName", "Chrome")
# options.set_capability("automationName", "UiAutomator2")
#
# options.set_capability("bstack:options", {
#     "userName": BROWSERSTACK_USERNAME,
#     "accessKey": BROWSERSTACK_ACCESS_KEY,
#     "buildName": "Python Appium Demo",
#     "sessionName": "Herokuapp Check"
# })
#
# # 🔑 Step 3: Connect to BrowserStack hub (use options instead of desired_capabilities)
# driver = webdriver.Remote(
#     command_executor=f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
#     options=options
# )
#
# # 🔑 Step 4: Write test steps
# try:
#     driver.get("https://the-internet.herokuapp.com/")
#
#     # Check title
#     assert "The Internet" in driver.title
#
#     # Check main title
#     title = driver.find_element(By.TAG_NAME, "h1")
#     assert "Welcome to the-internet" in title.text
#
#     # Check subtitle
#     subtitle = driver.find_element(By.TAG_NAME, "h2")
#     assert "Available Examples" in subtitle.text
#
#     # Just check list items exist
#     list_items = driver.find_elements(By.CSS_SELECTOR, "ul li")
#     assert len(list_items) > 0, "❌ No examples found!"
#
#     print("✅ All checks passed successfully on BrowserStack!")
#
# finally:
#     driver.quit()
