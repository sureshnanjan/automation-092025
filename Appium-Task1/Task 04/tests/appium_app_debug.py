import json
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and quit the Appium driver."""
    # Load capabilities from JSON file
    with open("Task_04_Debugging_W_Appium_Inspector/capabilities/android.json") as f:
        desired_cap = json.load(f)

    # Convert capabilities dict into UiAutomator2Options
    options = UiAutomator2Options().load_capabilities(desired_cap)

    # Initialize driver with BrowserStack endpoint
    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        options=options
    )

    yield driver
    driver.quit()


def test_with_waits(driver):
    """Test navigation in the ApiDemos app using waits."""
    wait = WebDriverWait(driver, 10)

    # Step 1: Click "Accessibility"
    accessibility = wait.until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Accessibility"))
    )
    accessibility.click()

    # Step 2: Wait for "Accessibility Node Provider" to be visible
    node_provider = wait.until(
        EC.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "Accessibility Node Provider")
        )
    )

    # Step 3: Verify element is displayed
    assert node_provider.is_displayed(), "Accessibility Node Provider not visible on screen"
