from selenium import webdriver
from selenium.webdriver.common.by import By
mybrowser = webdriver.Chrome()
mybrowser.get('https://the-internet.herokuapp.com/')
assert 'Internet' in mybrowser.title
title = mybrowser.find_element(By.TAG_NAME, 'h1')
assert 'Welcome to the-internet' in title.text 
mybrowser.quit()