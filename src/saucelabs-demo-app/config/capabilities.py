"""Device capabilities configuration for Android and iOS."""

from config.config import Config


class Capabilities:
    """
    Capabilities manager for Android and iOS devices.

    This class provides device-specific capabilities required
    for Appium driver initialization.
    """

    @staticmethod
    def get_android_capabilities():
        """
        Get Android device capabilities.

        Returns:
            dict: Android capabilities dictionary
        """
        return {
            "platformName": "Android",
            "platformVersion": Config.ANDROID_PLATFORM_VERSION,
            "deviceName": Config.ANDROID_DEVICE_NAME,
            "appPackage": Config.ANDROID_APP_PACKAGE,
            "appActivity": Config.ANDROID_APP_ACTIVITY,
            "automationName": "UiAutomator2",
            "autoGrantPermissions": True,
            "noReset": False,
            "fullReset": False,
            "newCommandTimeout": Config.COMMAND_TIMEOUT,
        }

    @staticmethod
    def get_ios_capabilities():
        """
        Get iOS device capabilities.

        Returns:
            dict: iOS capabilities dictionary
        """
        return {
            "platformName": "iOS",
            "platformVersion": Config.IOS_PLATFORM_VERSION,
            "deviceName": Config.IOS_DEVICE_NAME,
            "bundleId": Config.IOS_BUNDLE_ID,
            "automationName": "XCUITest",
            "autoAcceptAlerts": True,
            "noReset": False,
            "fullReset": False,
            "newCommandTimeout": Config.COMMAND_TIMEOUT,
        }

    @staticmethod
    def get_capabilities():
        """
        Get platform-specific capabilities based on configuration.

        Returns:
            dict: Capabilities dictionary for current platform
        """
        if Config.is_android():
            return Capabilities.get_android_capabilities()
        else:
            return Capabilities.get_ios_capabilities()
