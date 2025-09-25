from selenium import webdriver
from selenium.webdriver.common.by import By
mybroswer = webdriver.Firefox()
mybroswer.get('https://the-internet.herokuapp.com/')
assert 'Internet' in mybroswer.title
title = mybroswer.find_element(By.XPATH, '/html/body/div[2]/div/h2')
assert 'Available Examples' in title.text 
mybroswer.quit()