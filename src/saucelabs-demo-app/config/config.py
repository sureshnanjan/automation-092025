"""Configuration management for test automation framework."""

import os
from enum import Enum


class Platform(Enum):
    """Supported mobile platforms."""

    ANDROID = "android"
    IOS = "ios"


class Config:
    """
    Central configuration class for framework settings.

    This class manages all configuration parameters including
    platform settings, timeouts, and application details.
    """

    # Appium Server Configuration
    APPIUM_SERVER_URL = os.getenv(
        "APPIUM_SERVER_URL",
        "http://127.0.0.1:4723"
    )

    # Platform Selection
    PLATFORM = os.getenv("PLATFORM", Platform.ANDROID.value)

    # Timeout Configuration
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))
    COMMAND_TIMEOUT = int(os.getenv("COMMAND_TIMEOUT", "120"))

    # Application Configuration
    ANDROID_APP_PACKAGE = "com.saucelabs.mydemoapp.android"
    ANDROID_APP_ACTIVITY = (
        "com.saucelabs.mydemoapp.android.view.activities.MainActivity"
    )

    IOS_BUNDLE_ID = "com.saucelabs.mydemoapp.ios"

    # Device Configuration
    ANDROID_DEVICE_NAME = os.getenv("ANDROID_DEVICE_NAME", "emulator-5554")
    ANDROID_PLATFORM_VERSION = os.getenv("ANDROID_PLATFORM_VERSION", "13.0")

    IOS_DEVICE_NAME = os.getenv("IOS_DEVICE_NAME", "iPhone 14")
    IOS_PLATFORM_VERSION = os.getenv("IOS_PLATFORM_VERSION", "16.0")

    # Test Data
    TEST_USERNAME = os.getenv("TEST_USERNAME", "bob@example.com")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD", "10203040")

    # Reporting Configuration
    REPORTS_DIR = "reports"
    LOGS_DIR = "logs"
    SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")

    @classmethod
    def get_platform(cls):
        """
        Get the current platform.

        Returns:
            Platform: The current platform enum value
        """
        return Platform(cls.PLATFORM.lower())

    @classmethod
    def is_android(cls):
        """
        Check if current platform is Android.

        Returns:
            bool: True if platform is Android, False otherwise
        """
        return cls.get_platform() == Platform.ANDROID

    @classmethod
    def is_ios(cls):
        """
        Check if current platform is iOS.

        Returns:
            bool: True if platform is iOS, False otherwise
        """
        return cls.get_platform() == Platform.IOS
