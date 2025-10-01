from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.browser_version = 'stable'
options.browserName = 'Chrome',
options.browserVersion = 'latest',
options.os = 'Windows',
options.os_version =  '10',
options.build = "My Python Build",
options.name =  "My Selenium Test",
options.browserstack.user =  'kishan_C0rn9k',
options.browserstack.key = 'vHNYocPBhHwSYq3vKfsY'



driver = webdriver.Remote(
    command_executor='https://hub-cloud.browserstack.com/wd/hub', options=options
)
# Your test steps here
driver.get("https://the-internet.herokuapp.com/")
print(driver.title)
# ...
driver.quit()
