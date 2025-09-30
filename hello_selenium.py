from selenium import webdriver
from selenium.webdriver.common.by import By
mybroswer = webdriver.Firefox()
mybroswer.get('https://the-internet.herokuapp.com/')
assert 'Internet' in mybroswer.title
title = mybroswer.find_element(By.TAG_NAME, 'h1')
assert 'Suresh' in title.text 
mybroswer.quit()