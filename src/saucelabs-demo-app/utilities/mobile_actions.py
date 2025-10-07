"""Mobile actions utility for cross-platform element interactions."""

import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import Config
from utilities.logger import Logger


class MobileActions:
    """
    Cross-platform mobile actions utility class.

    Provides unified API for common element interactions like click,
    send keys, wait for element, etc., with proper error handling
    and logging.
    """

    logger = Logger.get_logger(__name__)

    def __init__(self, driver):
        """
        Initialize MobileActions with driver instance.

        Args:
            driver (webdriver.Remote): Appium driver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    def click(self, locator, timeout=None):
        """
        Click on element located by locator.

        Args:
            locator (tuple): Locator tuple (By.ID, 'element_id')
            timeout (int, optional): Custom timeout in seconds

        Returns:
            bool: True if click succeeded, False otherwise
        """
        try:
            element = self.wait_for_element(locator, timeout)
            if element:
                element.click()
                self.logger.info(f"Clicked on element: {locator}")
                return True
            return False

        except Exception as e:
            self.logger.error(f"Failed to click element {locator}: {str(e)}")
            return False

    def send_keys(self, locator, text, clear_first=True, timeout=None):
        """
        Send keys to element.

        Args:
            locator (tuple): Locator tuple (By.ID, 'element_id')
            text (str): Text to send
            clear_first (bool): Clear field before sending keys
            timeout (int, optional): Custom timeout in seconds

        Returns:
            bool: True if send keys succeeded, False otherwise
        """
        try:
            element = self.wait_for_element(locator, timeout)
            if element:
                if clear_first:
                    element.clear()
                element.send_keys(text)
                self.logger.info(
                    f"Sent keys '{text}' to element: {locator}"
                )
                return True
            return False

        except Exception as e:
            self.logger.error(
                f"Failed to send keys to {locator}: {str(e)}"
            )
            return False

    def get_text(self, locator, timeout=None):
        """
        Get text from element.

        Args:
            locator (tuple): Locator tuple (By.ID, 'element_id')
            timeout (int, optional): Custom timeout in seconds

        Returns:
            str: Element text or empty string if failed
        """
        try:
            element = self.wait_for_element(locator, timeout)
            if element:
                text = element.text
                self.logger.info(
                    f"Retrieved text '{text}' from element: {locator}"
                )
                return text
            return ""

        except Exception as e:
            self.logger.error(
                f"Failed to get text from {locator}: {str(e)}"
            )
            return ""

    def get_attribute(self, locator, attribute, timeout=None):
        """
        Get attribute value from element.

        Args:
            locator (tuple): Locator tuple (By.ID, 'element_id')
            attribute (str): Attribute name
            timeout (int, optional): Custom timeout in seconds

        Returns:
            str: Attribute value or empty string if failed
        """
        try:
            element = self.wait_for_element(locator, timeout)
            if element:
                value = element.get_attribute(attribute)
                self.logger.info(
                    f"Retrieved attribute '{attribute}' = '{value}' "
                    f"from element: {locator}"
                )
                return value
            return ""

        except Exception as e:
            self.logger.error(
                f"Failed to get attribute from {locator}: {str(e)}"
            )
            return ""

    def is_displayed(self, locator, timeout=None):
        """
        Check if element is displayed.

        Args:
            locator (tuple): Locator tuple (By.ID, 'element_id')
            timeout (int, optional): Custom timeout in seconds

        Returns:
            bool: True if element is displayed, False otherwise
        """
        try:
            element = self.wait_for_element(locator, timeout)
            if element:
                displayed = element.is_displayed()
                self.logger.info(
                    f"Element {locator} displayed: {displayed}"
                )
                return displayed
            return False

        except Exception as e:
            self.logger.error(
                f"Failed to check if element displayed {locator}: {str(e)}"
            )
            return False

    def is_enabled(self, locator, timeout=None):
        """
        Check if element is enabled.

        Args:
            locator (tuple): Locator tuple (By.ID, 'element_id')
            timeout (int, optional): Custom timeout in seconds

        Returns:
            bool: True if element is enabled, False otherwise
        """
        try:
            element = self.wait_for_element(locator, timeout)
            if element:
                enabled = element.is_enabled()
                self.logger.info(
                    f"Element {locator} enabled: {enabled}"
                )
                return enabled
            return False

        except Exception as e:
            self.logger.error(
                f"Failed to check if element enabled {locator}: {str(e)}"
            )
            return False

    def wait_for_element(self, locator, timeout=None):
        """
        Wait for element to be visible.

        Args:
            locator (tuple): Locator tuple (By.ID, 'element_id')
            timeout (int, optional): Custom timeout in seconds

        Returns:
            WebElement: Element if found, None otherwise
        """
        try:
            wait_time = timeout if timeout else Config.EXPLICIT_WAIT
            wait = WebDriverWait(self.driver, wait_time)
            element = wait.until(
                EC.visibility_of_element_located(locator)
            )
            self.logger.info(f"Element found: {locator}")
            return element

        except TimeoutException:
            self.logger.error(
                f"Timeout waiting for element: {locator}"
            )
            return None

    def wait_for_element_clickable(self, locator, timeout=None):
        """
        Wait for element to be clickable.

        Args:
            locator (tuple): Locator tuple (By.ID, 'element_id')
            timeout (int, optional): Custom timeout in seconds

        Returns:
            WebElement: Element if found and clickable, None otherwise
        """
        try:
            wait_time = timeout if timeout else Config.EXPLICIT_WAIT
            wait = WebDriverWait(self.driver, wait_time)
            element = wait.until(
                EC.element_to_be_clickable(locator)
            )
            self.logger.info(f"Element clickable: {locator}")
            return element

        except TimeoutException:
            self.logger.error(
                f"Timeout waiting for clickable element: {locator}"
            )
            return None

    def wait_for_elements(self, locator, timeout=None):
        """
        Wait for multiple elements to be visible.

        Args:
            locator (tuple): Locator tuple (By.ID, 'element_id')
            timeout (int, optional): Custom timeout in seconds

        Returns:
            list: List of WebElements or empty list if not found
        """
        try:
            wait_time = timeout if timeout else Config.EXPLICIT_WAIT
            wait = WebDriverWait(self.driver, wait_time)
            elements = wait.until(
                EC.visibility_of_all_elements_located(locator)
            )
            self.logger.info(
                f"Found {len(elements)} elements: {locator}"
            )
            return elements

        except TimeoutException:
            self.logger.error(
                f"Timeout waiting for elements: {locator}"
            )
            return []

    def hide_keyboard(self):
        """
        Hide mobile keyboard if visible.

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if Config.is_android():
                self.driver.hide_keyboard()
            else:
                # For iOS, tap on a coordinate outside keyboard
                size = self.driver.get_window_size()
                self.driver.tap([(size['width'] / 2, 50)])

            self.logger.info("Keyboard hidden")
            return True

        except Exception as e:
            self.logger.warning(f"Failed to hide keyboard: {str(e)}")
            return False

    def take_screenshot(self, name="screenshot"):
        """
        Take screenshot and save to reports directory.

        Args:
            name (str): Screenshot name prefix

        Returns:
            str: Screenshot file path or empty string if failed
        """
        try:
            os.makedirs(Config.SCREENSHOTS_DIR, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}.png"
            filepath = os.path.join(Config.SCREENSHOTS_DIR, filename)

            self.driver.save_screenshot(filepath)
            self.logger.info(f"Screenshot saved: {filepath}")
            return filepath

        except Exception as e:
            self.logger.error(f"Failed to take screenshot: {str(e)}")
            return ""

    def switch_to_context(self, context_name):
        """
        Switch to specific context (NATIVE_APP or WEBVIEW).

        Args:
            context_name (str): Context name to switch to

        Returns:
            bool: True if switch succeeded, False otherwise
        """
        try:
            contexts = self.driver.contexts
            if context_name in contexts:
                self.driver.switch_to.context(context_name)
                self.logger.info(f"Switched to context: {context_name}")
                return True
            else:
                self.logger.error(
                    f"Context {context_name} not found in {contexts}"
                )
                return False

        except Exception as e:
            self.logger.error(f"Failed to switch context: {str(e)}")
            return False
