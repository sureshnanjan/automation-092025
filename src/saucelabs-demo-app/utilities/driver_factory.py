"""Driver factory for creating Appium driver instances."""

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from config.config import Config
from config.capabilities import Capabilities
from utilities.logger import Logger


class DriverFactory:
    """
    Factory class for creating and managing Appium driver instances.

    This class handles driver initialization and cleanup for both
    Android and iOS platforms.
    """

    logger = Logger.get_logger(__name__)

    @staticmethod
    def create_driver():
        """
        Create Appium driver based on platform configuration.

        Returns:
            webdriver.Remote: Configured Appium driver instance

        Raises:
            Exception: If driver creation fails
        """
        try:
            DriverFactory.logger.info(
                f"Creating driver for platform: {Config.PLATFORM}"
            )

            if Config.is_android():
                options = UiAutomator2Options().load_capabilities(
                    Capabilities.get_android_capabilities()
                )
            else:
                options = XCUITestOptions().load_capabilities(
                    Capabilities.get_ios_capabilities()
                )

            driver = webdriver.Remote(
                Config.APPIUM_SERVER_URL,
                options=options
            )

            driver.implicitly_wait(Config.IMPLICIT_WAIT)
            DriverFactory.logger.info("Driver created successfully")

            return driver

        except Exception as e:
            DriverFactory.logger.error(f"Failed to create driver: {str(e)}")
            raise

    @staticmethod
    def quit_driver(driver):
        """
        Quit the Appium driver and cleanup resources.

        Args:
            driver (webdriver.Remote): Driver instance to quit
        """
        if driver:
            try:
                DriverFactory.logger.info("Quitting driver")
                driver.quit()
                DriverFactory.logger.info("Driver quit successfully")
            except Exception as e:
                DriverFactory.logger.error(
                    f"Error while quitting driver: {str(e)}"
                )
