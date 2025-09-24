from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch browser
mybrowser = webdriver.Firefox()
mybrowser.get("https://the-internet.herokuapp.com/")

# Assert page title
assert "Internet" in mybrowser.title

# Assert main title (h1)
title = mybrowser.find_element(By.TAG_NAME, "h1")
assert "Welcome to the-internet" in title.text

# Assert subtitle (h2)
subtitle = mybrowser.find_element(By.TAG_NAME, "h2")
assert "Available Examples" in subtitle.text

# Close browser
mybrowser.quit()
