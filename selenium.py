from selenium import webdriver
from selenium.webdriver.common.by import By
mybroswer = webdriver.Chrome()
mybroswer.get('https://the-internet.herokuapp.com/')
assert 'Internet' in mybroswer.title
title = mybroswer.find_element(By.TAG_NAME, 'h1')
assert 'Welcome to the-internet' in title.text 
mybroswer.quit()