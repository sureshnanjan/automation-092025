import pytest
from appium.webdriver.common.appiumby import AppiumBy

# Device configurations
devices = [
    {
        'platform': 'Android',
        'version': '11.0',
        'device': 'Samsung Galaxy S21',
        'app': 'bs://f8a6d43db506424d3e595ae69dfde7bb5b368660'
    },
    {
        'platform': 'Android',
        'version': '12.0',
        'device': 'Google Pixel 6',
        'app': 'bs://f8a6d43db506424d3e595ae69dfde7bb5b368660'
    },
    {
        'platform': 'iOS',
        'version': '16',
        'device': 'iPhone 13',
        'app': 'bs://f8a6d43db506424d3e595ae69dfde7bb5b368660'
    }
]


@pytest.mark.parametrize("driver", devices, indirect=True)
def test_login_flow(driver):

    # Wait for the app to load
    driver.implicitly_wait(10)

    # Perform login test
    username_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "username")
    username_field.send_keys("testuser@example.com")

    password_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "password")
    password_field.send_keys("Test@123")

    login_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "loginButton")
    login_button.click()

    # Verify successful login
    success_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "welcomeMessage")
    assert success_element.is_displayed()
