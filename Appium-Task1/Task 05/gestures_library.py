from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

# Initialize driver (use BrowserStack config from previous tasks)

class MobileGestures:

    def __init__(self, driver):
        self.driver = driver

    def swipe_left(self):
        """Swipe left on the screen."""
        size = self.driver.get_window_size()
        start_x = int(size['width'] * 0.8)
        start_y = int(size['height'] * 0.5)
        end_x = int(size['width'] * 0.2)

        actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.move_to_location(end_x, start_y)
        actions.pointer_action.pointer_up()
        actions.perform()

    def scroll_to_element(self, element_text):
        """Scroll until element is found (Android only)."""
        try:
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(text("{element_text}"))'
            )
        except Exception as e:
            print(f"⚠️ Element '{element_text}' not found during scroll: {e}")

    def long_press(self, element, duration=2):
        """Long press on an element for a specified duration (seconds)."""
        x = element.location['x']
        y = element.location['y']

        actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.pointer_action.move_to_location(x, y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(duration)
        actions.pointer_action.pointer_up()
        actions.perform()

    def tap(self, element):
        """Single tap on an element."""
        element.click()

    def pinch_zoom(self, element):
        """(Placeholder) Pinch to zoom gesture."""
        # Implementation for pinch gesture
        pass
