import os
import json
import pytest
from appium import webdriver


@pytest.fixture(scope="function")
def driver(request):
    """Initialize Appium driver with BrowserStack capabilities."""

    # Get platform (default to android if not provided)
    platform = request.config.getoption("--platform") or "android"

    # Load the capabilities file (e.g., capabilities/android.json)
    caps_path = os.path.join(os.path.dirname(__file__), "..", "capabilities", f"{platform}.json")
    with open(caps_path) as f:
        desired_caps = json.load(f)

    # Initialize WebDriver (BrowserStack endpoint)
    driver = webdriver.Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=desired_caps
    )

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        help="Specify the platform to run tests on (android or ios)"
    )
