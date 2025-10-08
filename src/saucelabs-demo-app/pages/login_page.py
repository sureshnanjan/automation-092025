"""Login page object."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Login page object for My Demo App.

    Contains all locators and methods related to login functionality.
    """

    # Android Locators
    ANDROID_MENU_BUTTON = (
        By.XPATH,
        "//android.view.ViewGroup[@content-desc='open menu']/android.widget.ImageView"
    )
    ANDROID_LOGIN_MENU_ITEM = (
        By.ACCESSIBILITY_ID,
        "menu item log in"
    )
    ANDROID_USERNAME_FIELD = (
        By.ACCESSIBILITY_ID,
        "Username input field"
    )
    ANDROID_PASSWORD_FIELD = (
        By.ACCESSIBILITY_ID,
        "Password input field"
    )
    ANDROID_LOGIN_BUTTON = (
        By.ACCESSIBILITY_ID,
        "Login button"
    )
    ANDROID_ERROR_MESSAGE = (
        By.XPATH,
        "//android.view.ViewGroup[@content-desc='generic-error-message']/android.widget.TextView"
    )
    ANDROID_LOGOUT_MENU_ITEM = (
        By.ACCESSIBILITY_ID,
        "menu item log out"
    )
    ANDROID_CONFIRM_LOGOUT_BUTTON = (
        By.XPATH,
        "//android.widget.Button[@resource-id='android:id/button1']"
    )

    # iOS Locators
    IOS_MENU_BUTTON = (
        By.ACCESSIBILITY_ID,
        "tab bar option menu"
    )
    IOS_LOGIN_MENU_ITEM = (
        By.ACCESSIBILITY_ID,
        "menu item log in"
    )
    IOS_USERNAME_FIELD = (
        By.ACCESSIBILITY_ID,
        "Username input field"
    )
    IOS_PASSWORD_FIELD = (
        By.ACCESSIBILITY_ID,
        "Password input field"
    )
    IOS_LOGIN_BUTTON = (
        By.ACCESSIBILITY_ID,
        "Login button"
    )
    IOS_ERROR_MESSAGE = (
        By.ACCESSIBILITY_ID,
        "generic-error-message"
    )
    IOS_LOGOUT_MENU_ITEM = (
        By.ACCESSIBILITY_ID,
        "menu item log out"
    )
    IOS_CONFIRM_LOGOUT_BUTTON = (
        By.ACCESSIBILITY_ID,
        "Log Out"
    )

    def __init__(self, driver):
        """
        Initialize LoginPage.

        Args:
            driver (webdriver.Remote): Appium driver instance
        """
        super().__init__(driver)

    def open_menu(self):
        """
        Open the hamburger/tab menu.

        Returns:
            bool: True if menu opened successfully, False otherwise
        """
        locator = self.get_locator(
            self.ANDROID_MENU_BUTTON,
            self.IOS_MENU_BUTTON
        )
        success = self.actions.click(locator)
        if success:
            self.logger.info("Menu opened")
        return success

    def navigate_to_login(self):
        """
        Navigate to login screen from menu.

        Returns:
            bool: True if navigation successful, False otherwise
        """
        if self.open_menu():
            locator = self.get_locator(
                self.ANDROID_LOGIN_MENU_ITEM,
                self.IOS_LOGIN_MENU_ITEM
            )
            success = self.actions.click(locator)
            if success:
                self.logger.info("Navigated to login screen")
            return success
        return False

    def enter_username(self, username):
        """
        Enter username in username field.

        Args:
            username (str): Username to enter

        Returns:
            bool: True if successful, False otherwise
        """
        locator = self.get_locator(
            self.ANDROID_USERNAME_FIELD,
            self.IOS_USERNAME_FIELD
        )
        success = self.actions.send_keys(locator, username)
        if success:
            self.logger.info(f"Entered username: {username}")
        return success

    def enter_password(self, password):
        """
        Enter password in password field.

        Args:
            password (str): Password to enter

        Returns:
            bool: True if successful, False otherwise
        """
        locator = self.get_locator(
            self.ANDROID_PASSWORD_FIELD,
            self.IOS_PASSWORD_FIELD
        )
        success = self.actions.send_keys(locator, password)
        if success:
            self.logger.info("Entered password")
        return success

    def click_login_button(self):
        """
        Click the login button.

        Returns:
            bool: True if successful, False otherwise
        """
        locator = self.get_locator(
            self.ANDROID_LOGIN_BUTTON,
            self.IOS_LOGIN_BUTTON
        )
        success = self.actions.click(locator)
        if success:
            self.logger.info("Clicked login button")
        return success

    def login(self, username, password):
        """
        Perform complete login flow.

        Args:
            username (str): Username to login with
            password (str): Password to login with

        Returns:
            bool: True if login successful, False otherwise
        """
        self.logger.info(f"Attempting login with username: {username}")

        if not self.navigate_to_login():
            return False

        if not self.enter_username(username):
            return False

        if not self.enter_password(password):
            return False

        if not self.click_login_button():
            return False

        # Hide keyboard after login
        self.actions.hide_keyboard()

        self.logger.info("Login flow completed")
        return True

    def get_error_message(self):
        """
        Get error message text if displayed.

        Returns:
            str: Error message text or empty string
        """
        locator = self.get_locator(
            self.ANDROID_ERROR_MESSAGE,
            self.IOS_ERROR_MESSAGE
        )
        return self.actions.get_text(locator)

    def is_error_displayed(self):
        """
        Check if error message is displayed.

        Returns:
            bool: True if error is displayed, False otherwise
        """
        locator = self.get_locator(
            self.ANDROID_ERROR_MESSAGE,
            self.IOS_ERROR_MESSAGE
        )
        return self.actions.is_displayed(locator, timeout=5)

    def logout(self):
        """
        Perform logout operation.

        Returns:
            bool: True if logout successful, False otherwise
        """
        self.logger.info("Attempting logout")

        if not self.open_menu():
            return False

        logout_locator = self.get_locator(
            self.ANDROID_LOGOUT_MENU_ITEM,
            self.IOS_LOGOUT_MENU_ITEM
        )

        if not self.actions.click(logout_locator):
            return False

        confirm_locator = self.get_locator(
            self.ANDROID_CONFIRM_LOGOUT_BUTTON,
            self.IOS_CONFIRM_LOGOUT_BUTTON
        )

        success = self.actions.click(confirm_locator)
        if success:
            self.logger.info("Logout successful")
        return success
