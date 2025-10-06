import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

USERNAME = "tanujsingh_jhcLtJ"
ACCESS_KEY = "pfhBpuadweTk5S5Kzq4d"


@pytest.fixture(scope="function")
def driver(request):
    device_config = request.param

    # Select appropriate options based on platform
    if device_config['platform'].lower() == 'android':
        options = UiAutomator2Options()
    else:
        options = XCUITestOptions()

    options.platform_name = device_config['platform']
    options.platform_version = device_config['version']
    options.device_name = device_config['device']
    options.app = device_config['app']

    # Set BrowserStack options
    options.set_capability(
        'bstack:options',
        {
            "userName": USERNAME,
            "accessKey": ACCESS_KEY,
            "projectName": "Cross-Device Testing",
            "buildName": "Multi-Device Build",
            "sessionName": f"{device_config['device']} Test"
        }
    )

    # Initialize the Appium driver
    driver = webdriver.Remote(
        "https://hub.browserstack.com/wd/hub",
        options=options
    )

    yield driver
    driver.quit()
