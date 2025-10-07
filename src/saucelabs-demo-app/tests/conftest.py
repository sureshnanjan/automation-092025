"""Pytest configuration and fixtures."""

import pytest
from utilities.driver_factory import DriverFactory
from utilities.logger import Logger

logger = Logger.get_logger(__name__)


@pytest.fixture(scope="function")
def driver():
    """
    Create and provide driver instance for each test.

    Yields:
        webdriver.Remote: Appium driver instance

    This fixture:
    - Creates a new driver before each test
    - Yields the driver to the test
    - Quits the driver after test completion
    """
    logger.info("=" * 80)
    logger.info("Setting up driver for test")
    driver_instance = DriverFactory.create_driver()

    yield driver_instance

    logger.info("Tearing down driver after test")
    DriverFactory.quit_driver(driver_instance)
    logger.info("=" * 80)


@pytest.fixture(scope="function")
def take_screenshot_on_failure(driver, request):
    """
    Automatically take screenshot on test failure.

    Args:
        driver: Driver fixture
        request: Pytest request object

    Yields:
        None: This fixture doesn't provide any value
    """
    yield

    if request.node.rep_call.failed:
        from utilities.mobile_actions import MobileActions
        actions = MobileActions(driver)
        test_name = request.node.name
        actions.take_screenshot(f"failure_{test_name}")
        logger.info(f"Screenshot taken for failed test: {test_name}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to make test result available to fixtures.

    This hook makes the test result accessible in fixtures
    for conditional actions like taking screenshots on failure.

    Args:
        item: Test item
        call: Test call object

    Yields:
        None: Hook implementation
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


def pytest_configure(config):
    """
    Configure pytest with custom markers.

    Args:
        config: Pytest config object
    """
    config.addinivalue_line(
        "markers",
        "smoke: Mark test as smoke test"
    )
    config.addinivalue_line(
        "markers",
        "regression: Mark test as regression test"
    )
    config.addinivalue_line(
        "markers",
        "login: Mark test as login feature test"
    )
    config.addinivalue_line(
        "markers",
        "product: Mark test as product feature test"
    )