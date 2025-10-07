"""Mobile gesture utilities for cross-platform automation."""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from config.config import Config
from utilities.logger import Logger


class MobileGestures:
    """
    Cross-platform mobile gesture utility class.

    Provides unified API for common mobile gestures like swipe,
    scroll, tap, long press, etc., working seamlessly on both
    Android and iOS platforms.
    """

    logger = Logger.get_logger(__name__)

    def __init__(self, driver):
        """
        Initialize MobileGestures with driver instance.

        Args:
            driver (webdriver.Remote): Appium driver instance
        """
        self.driver = driver
        self.actions = ActionChains(driver)

    def swipe(self, start_x, start_y, end_x, end_y, duration=800):
        """
        Perform swipe gesture from start to end coordinates.

        Args:
            start_x (int): Starting X coordinate
            start_y (int): Starting Y coordinate
            end_x (int): Ending X coordinate
            end_y (int): Ending Y coordinate
            duration (int): Duration of swipe in milliseconds

        Returns:
            bool: True if swipe succeeded, False otherwise
        """
        try:
            self.logger.info(
                f"Swiping from ({start_x}, {start_y}) to "
                f"({end_x}, {end_y})"
            )

            actions = ActionBuilder(
                self.driver,
                mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
            )
            actions.pointer_action.move_to_location(start_x, start_y)
            actions.pointer_action.pointer_down()
            actions.pointer_action.pause(duration / 1000)
            actions.pointer_action.move_to_location(end_x, end_y)
            actions.pointer_action.release()
            actions.perform()

            self.logger.info("Swipe performed successfully")
            return True

        except Exception as e:
            self.logger.error(f"Failed to perform swipe: {str(e)}")
            return False

    def swipe_left(self, duration=800):
        """
        Swipe left on the screen.

        Args:
            duration (int): Duration of swipe in milliseconds

        Returns:
            bool: True if swipe succeeded, False otherwise
        """
        size = self.driver.get_window_size()
        start_x = int(size['width'] * 0.8)
        end_x = int(size['width'] * 0.2)
        y = int(size['height'] * 0.5)

        return self.swipe(start_x, y, end_x, y, duration)

    def swipe_right(self, duration=800):
        """
        Swipe right on the screen.

        Args:
            duration (int): Duration of swipe in milliseconds

        Returns:
            bool: True if swipe succeeded, False otherwise
        """
        size = self.driver.get_window_size()
        start_x = int(size['width'] * 0.2)
        end_x = int(size['width'] * 0.8)
        y = int(size['height'] * 0.5)

        return self.swipe(start_x, y, end_x, y, duration)

    def swipe_up(self, duration=800):
        """
        Swipe up on the screen.

        Args:
            duration (int): Duration of swipe in milliseconds

        Returns:
            bool: True if swipe succeeded, False otherwise
        """
        size = self.driver.get_window_size()
        x = int(size['width'] * 0.5)
        start_y = int(size['height'] * 0.8)
        end_y = int(size['height'] * 0.2)

        return self.swipe(x, start_y, x, end_y, duration)

    def swipe_down(self, duration=800):
        """
        Swipe down on the screen.

        Args:
            duration (int): Duration of swipe in milliseconds

        Returns:
            bool: True if swipe succeeded, False otherwise
        """
        size = self.driver.get_window_size()
        x = int(size['width'] * 0.5)
        start_y = int(size['height'] * 0.2)
        end_y = int(size['height'] * 0.8)

        return self.swipe(x, start_y, x, end_y, duration)

    def scroll_to_element(self, element):
        """
        Scroll to make element visible.

        Args:
            element: WebElement to scroll to

        Returns:
            bool: True if scroll succeeded, False otherwise
        """
        try:
            self.logger.info("Scrolling to element")

            if Config.is_android():
                self.driver.execute_script(
                    "mobile: scrollToElement",
                    {"element": element}
                )
            else:
                self.driver.execute_script(
                    "mobile: scroll",
                    {"element": element, "toVisible": True}
                )

            self.logger.info("Scrolled to element successfully")
            return True

        except Exception as e:
            self.logger.error(f"Failed to scroll to element: {str(e)}")
            return False

    def long_press(self, element, duration=2000):
        """
        Perform long press on element.

        Args:
            element: WebElement to long press
            duration (int): Duration of press in milliseconds

        Returns:
            bool: True if long press succeeded, False otherwise
        """
        try:
            self.logger.info("Performing long press")

            location = element.location
            size = element.size
            x = location['x'] + size['width'] / 2
            y = location['y'] + size['height'] / 2

            actions = ActionBuilder(
                self.driver,
                mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
            )
            actions.pointer_action.move_to_location(int(x), int(y))
            actions.pointer_action.pointer_down()
            actions.pointer_action.pause(duration / 1000)
            actions.pointer_action.release()
            actions.perform()

            self.logger.info("Long press performed successfully")
            return True

        except Exception as e:
            self.logger.error(f"Failed to perform long press: {str(e)}")
            return False

    def tap(self, x, y):
        """
        Tap at specific coordinates.

        Args:
            x (int): X coordinate
            y (int): Y coordinate

        Returns:
            bool: True if tap succeeded, False otherwise
        """
        try:
            self.logger.info(f"Tapping at coordinates ({x}, {y})")

            actions = ActionBuilder(
                self.driver,
                mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
            )
            actions.pointer_action.move_to_location(x, y)
            actions.pointer_action.pointer_down()
            actions.pointer_action.pointer_up()
            actions.perform()

            self.logger.info("Tap performed successfully")
            return True

        except Exception as e:
            self.logger.error(f"Failed to perform tap: {str(e)}")
            return False

    def double_tap(self, element):
        """
        Perform double tap on element.

        Args:
            element: WebElement to double tap

        Returns:
            bool: True if double tap succeeded, False otherwise
        """
        try:
            self.logger.info("Performing double tap")

            location = element.location
            size = element.size
            x = int(location['x'] + size['width'] / 2)
            y = int(location['y'] + size['height'] / 2)

            self.tap(x, y)
            self.tap(x, y)

            self.logger.info("Double tap performed successfully")
            return True

        except Exception as e:
            self.logger.error(f"Failed to perform double tap: {str(e)}")
            return False

    def pinch(self, element, percent=100, steps=50):
        """
        Perform pinch gesture on element.

        Args:
            element: WebElement to pinch
            percent (int): Pinch percentage
            steps (int): Number of steps for smooth pinch

        Returns:
            bool: True if pinch succeeded, False otherwise
        """
        try:
            self.logger.info("Performing pinch gesture")

            if Config.is_android():
                self.driver.execute_script(
                    "mobile: pinchCloseGesture",
                    {
                        "elementId": element.id,
                        "percent": percent / 100,
                        "speed": steps
                    }
                )
            else:
                self.driver.execute_script(
                    "mobile: pinch",
                    {"element": element, "scale": percent / 100}
                )

            self.logger.info("Pinch performed successfully")
            return True

        except Exception as e:
            self.logger.error(f"Failed to perform pinch: {str(e)}")
            return False

    def zoom(self, element, percent=200, steps=50):
        """
        Perform zoom gesture on element.

        Args:
            element: WebElement to zoom
            percent (int): Zoom percentage
            steps (int): Number of steps for smooth zoom

        Returns:
            bool: True if zoom succeeded, False otherwise
        """
        try:
            self.logger.info("Performing zoom gesture")

            if Config.is_android():
                self.driver.execute_script(
                    "mobile: pinchOpenGesture",
                    {
                        "elementId": element.id,
                        "percent": percent / 100,
                        "speed": steps
                    }
                )
            else:
                self.driver.execute_script(
                    "mobile: pinch",
                    {"element": element, "scale": percent / 100}
                )

            self.logger.info("Zoom performed successfully")
            return True

        except Exception as e:
            self.logger.error(f"Failed to perform zoom: {str(e)}")
            return False
