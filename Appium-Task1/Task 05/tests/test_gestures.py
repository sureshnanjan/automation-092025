import sys
import os
import json
import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Add gestures_library import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gestures_library import MobileGestures


@pytest.fixture(scope="function")
def driver(request):
    platform = request.config.getoption("--platform")

    with open(f"capabilities/{platform}.json") as f:
        desired_caps = json.load(f)

    # Use the local APK file path
    apk_path = os.path.abspath("ApiDemos-debug.apk")
    desired_caps["appium:app"] = apk_path

    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        desired_capabilities=desired_caps
    )

    yield driver
    driver.quit()


def test_image_gallery_gestures(driver):
    gestures = MobileGestures(driver)

    print("\n======= PAGE SOURCE (Initial) =======")
    print(driver.page_source[:2000])  # print only first 2000 chars
    print("====================================\n")

    # Step 1: Open "Views"
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Views")').click()
    time.sleep(2)

    # Step 2: Scroll to and open "Gallery"
    gestures.scroll_to_element("Gallery")
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Gallery")').click()
    time.sleep(1)

    # Step 3: Tap "1. Photos"
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1. Photos")').click()
    time.sleep(1)

    # Step 4: Swipe through images
    for _ in range(3):
        gestures.swipe_left()
        time.sleep(1)

    # Step 5: Validate image presence
    image = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/gallery")
    assert image.is_displayed()


def test_form_interactions(driver):
    gestures = MobileGestures(driver)

    # Step 1: Go to "Views" → "Controls" → "2. Dark Theme"
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Views")').click()
    time.sleep(1)
    gestures.scroll_to_element("Controls")
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Controls")').click()
    time.sleep(1)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2. Dark Theme")').click()
    time.sleep(1)

    print("\n======= PAGE SOURCE (Form Screen) =======")
    print(driver.page_source[:2000])
    print("========================================\n")

    # Step 2: Enter name
    name_field = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/edit")
    name_field.send_keys("John Doe")
    driver.hide_keyboard()

    # Step 3: Toggle checkbox and switch
    checkbox = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/check1")
    checkbox.click()
    assert checkbox.is_selected()

    toggle = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/toggle1")
    toggle.click()
    assert toggle.get_attribute("checked") in ["true", True]
