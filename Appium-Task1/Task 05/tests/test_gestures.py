import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gestures_library import MobileGestures
import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from gestures_library import MobileGestures

def test_image_gallery_gestures(driver):
    gestures = MobileGestures(driver)

    # Test 1: Swipe through images
    for i in range(3):
        gestures.swipe_left()
        time.sleep(1)

    # Verify image changed
    current_image = driver.find_element(AppiumBy.ID, "image_view")
    assert current_image.is_displayed()

    # Test 2: Scroll to find specific item
    gestures.scroll_to_element("Settings")
    settings_button = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Settings']")
    assert settings_button.is_displayed()

    # Test 3: Long press for context menu
    item = driver.find_element(AppiumBy.ID, "list_item_1")
    gestures.long_press(item)
    context_menu = driver.find_element(AppiumBy.ID, "context_menu")
    assert context_menu.is_displayed()


def test_form_interactions(driver):
    gestures = MobileGestures(driver)

    # Test: Multi-finger tap and complex gestures
    # Implement form filling with various input types

    # Text input
    name_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "nameInput")
    name_field.send_keys("John Doe")

    # Hide keyboard
    driver.hide_keyboard()

    # Select from dropdown (requires swipe/scroll)
    dropdown = driver.find_element(AppiumBy.ID, "country_dropdown")
    dropdown.click()

    gestures.scroll_to_element("India")
    india_option = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='India']")
    india_option.click()

    # Submit form
    submit_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "submitButton")
    submit_button.click()

    # Verify submission
    success_message = driver.find_element(AppiumBy.ID, "success_message")
    assert "Success" in success_message.text
