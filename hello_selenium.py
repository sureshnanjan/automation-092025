from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome automatically
mybrowser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

mybrowser.get('https://the-internet.herokuapp.com/')

assert 'Internet' in mybrowser.title

title = mybrowser.find_element(By.TAG_NAME, 'h2')
assert 'Available Examples' in title.text

print("Test Passed")

mybrowser.quit()

