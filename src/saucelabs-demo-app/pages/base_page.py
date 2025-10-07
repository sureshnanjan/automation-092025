"""Base page class with common functionality."""

from selenium.webdriver.common.by import By
from config.config import Config
from utilities.mobile_actions import MobileActions
from utilities.mobile_gestures import MobileGestures
from utilities.logger import Logger


class BasePage:
    """
    Base page object class with common page functionality.

    All page objects should inherit from this class to access
    common utilities like actions, gestures, and logging.
    """

    logger = Logger.get_logger(__name__)

    def __init__(self, driver):
        """
        Initialize BasePage with driver instance.

        Args:
            driver (webdriver.Remote): Appium driver instance
        """
        self.driver = driver
        self.actions = MobileActions(driver)
        self.gestures = MobileGestures(driver)

    def get_locator(self, android_locator, ios_locator):
        """
        Get platform-specific locator.

        Args:
            android_locator (tuple): Android locator (By.ID, 'id')
            ios_locator (tuple): iOS locator (By.ID, 'id')

        Returns:
            tuple: Platform-specific locator
        """
        return android_locator if Config.is_android() else ios_locator

    def wait_for_page_load(self, locator, timeout=None):
        """
        Wait for page to load by waiting for specific element.

        Args:
            locator (tuple): Locator of element indicating page loaded
            timeout (int, optional): Custom timeout in seconds

        Returns:
            bool: True if page loaded, False otherwise
        """
        element = self.actions.wait_for_element(locator, timeout)
        return element is not None
