from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Firefox browser
mybrowser = webdriver.Firefox()
mybrowser.get("https://the-internet.herokuapp.com/")

# 1. Verify page title contains 'Internet'
assert "Internet" in mybrowser.title, "Page title does not contain 'Internet'"

# 2. Verify main heading (h1)
main_heading = mybrowser.find_element(By.TAG_NAME, "h1")
assert main_heading.text == "Welcome to the-internet", "Main heading text mismatch"

# 3. Verify subheading (h2) - 'Available Examples'
sub_heading = mybrowser.find_element(By.TAG_NAME, "h2")
assert sub_heading.text == "Available Examples", "Subheading text mismatch"

print("All checks passed successfully!")

# Close the browser
mybrowser.quit()
