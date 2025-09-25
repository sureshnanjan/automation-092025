from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch a new Firefox browser instance
mybrowser = webdriver.Firefox()

# Open the target website
mybrowser.get('https://the-internet.herokuapp.com/')

# Title check
assert 'Internet' in mybrowser.title

# Main title check
title = mybrowser.find_element(By.TAG_NAME, 'h1')
assert 'Welcome to the-internet' in title.text

# Subtitle check
subtitle = mybrowser.find_element(By.TAG_NAME, 'h2')
assert 'Available Examples' in subtitle.text

# List item count check
list_items = mybrowser.find_elements(By.CSS_SELECTOR, "ul li")
assert len(list_items) == 44, f"Expected 44 list items, but found {len(list_items)}"

# Print a success message if all checks pass
print("All checks passed successfully")

# Close the browser window
mybrowser.quit()
