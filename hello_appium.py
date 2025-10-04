from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

# BrowserStack credentials
USERNAME = "sowmyas_wijLeD"
ACCESS_KEY = "your access key"

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
