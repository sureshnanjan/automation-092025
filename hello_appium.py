from appium import webdriver
from selenium.webdriver.common.by import By
desired_caps = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "app": "/path/to/your/app.apk",
    "automationName": "UiAutomator2"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# Locate the element with text 'hello_appium'
element = driver.find_element(By.XPATH, "//*[@text='hello_appium']")
# Interact with it (e.g., click)
element.click()
# Quit the session
driver.quit()
