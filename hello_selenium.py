from selenium import webdriver
from selenium.webdriver.common.by import By
mybrowser = webdriver.Firefox()
mybrowser.get('https://the-internet.herokuapp.com/')

# ✅ Title check
assert 'Internet' in mybrowser.title

# ✅ Main title check
title = mybrowser.find_element(By.TAG_NAME, 'h1')
assert 'Welcome to the-internet' in title.text

# ✅ Subtitle check
subtitle = mybrowser.find_element(By.TAG_NAME, 'h2')
assert 'Available Examples' in subtitle.text

# ✅ List item count check
list_items = mybrowser.find_elements(By.CSS_SELECTOR, "ul li")
assert len(list_items) == 44, f"Expected 44 list items, but found {len(list_items)}"

print("✅ All checks passed successfully")

mybrowser.quit()