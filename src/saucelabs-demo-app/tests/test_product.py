"""Product feature test cases."""

import pytest
from config.config import Config
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utilities.logger import Logger

logger = Logger.get_logger(__name__)


@pytest.mark.product
class TestProduct:
    """Test suite for product functionality."""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """
        Setup method to login before each test.

        Args:
            driver: Driver fixture

        This fixture runs automatically before each test in this class.
        """
        logger.info("Setting up: Logging in before test")
        login_page = LoginPage(driver)
        login_page.login(Config.TEST_USERNAME, Config.TEST_PASSWORD)
        yield
        logger.info("Teardown: Test completed")

    @pytest.mark.smoke
    def test_view_product_list(self, driver):
        """
        Test viewing product list.

        Steps:
        1. Verify product page is displayed
        2. Verify products are visible

        Expected Result:
        - Product page should display multiple products
        """
        logger.info("Starting test: test_view_product_list")

        product_page = ProductPage(driver)

        # Verify product page is displayed
        assert product_page.is_product_page_displayed(), \
            "Product page not displayed"

        # Verify products are present
        product_count = product_page.get_product_count()
        assert product_count > 0, "No products found on page"

        logger.info(f"Found {product_count} products on page")
        logger.info("Test passed: test_view_product_list")

    @pytest.mark.smoke
    def test_add_product_to_cart(self, driver):
        """
        Test adding product to cart.

        Steps:
        1. Select first product
        2. Add product to cart
        3. Verify cart count increases

        Expected Result:
        - Product should be added to cart
        - Cart count should increase by 1
        """
        logger.info("Starting test: test_add_product_to_cart")

        product_page = ProductPage(driver)

        # Get initial cart count
        initial_count = product_page.get_cart_count()
        logger.info(f"Initial cart count: {initial_count}")

        # Click on first product
        assert product_page.click_product_by_index(0), \
            "Failed to click product"

        # Add to cart
        assert product_page.add_to_cart(), \
            "Failed to add product to cart"

        # Navigate back to product list
        driver.back()

        # Verify cart count increased
        new_count = product_page.get_cart_count()
        logger.info(f"New cart count: {new_count}")

        assert new_count == initial_count + 1, \
            f"Cart count not increased. Expected {initial_count + 1}, " \
            f"got {new_count}"

        logger.info("Test passed: test_add_product_to_cart")

    @pytest.mark.regression
    @pytest.mark.regression
    def test_view_cart_contents(self, driver):
        """
        Test viewing cart contents.

        Steps:
        1. Add product to cart
        2. Open cart page
        3. Verify cart items are displayed

        Expected Result:
        - Cart should display added items
        - Cart item count should match added items
        """
        logger.info("Starting test: test_view_cart_contents")

        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        # Add a product to cart
        product_page.click_product_by_index(0)
        product_page.add_to_cart()

        # Open cart
        assert cart_page.open_cart(), "Failed to open cart"

        # Verify items in cart
        cart_item_count = cart_page.get_cart_item_count()
        assert cart_item_count > 0, "No items found in cart"

        logger.info(f"Cart contains {cart_item_count} item(s)")
        logger.info("Test passed: test_view_cart_contents")

    @pytest.mark.regression
    def test_remove_item_from_cart(self, driver):
        """
        Test removing item from cart.

        Steps:
        1. Add product to cart
        2. Open cart
        3. Remove item from cart
        4. Verify cart is empty

        Expected Result:
        - Item should be removed from cart
        - Cart should be empty
        """
        logger.info("Starting test: test_remove_item_from_cart")

        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        # Add a product to cart
        product_page.click_product_by_index(0)
        product_page.add_to_cart()

        # Open cart
        cart_page.open_cart()

        # Get initial item count
        initial_count = cart_page.get_cart_item_count()
        logger.info(f"Initial cart items: {initial_count}")

        # Remove item
        assert cart_page.remove_item_by_index(0), \
            "Failed to remove item from cart"

        # Verify cart is empty or has fewer items
        new_count = cart_page.get_cart_item_count()
        logger.info(f"Cart items after removal: {new_count}")

        assert new_count < initial_count, \
            "Item was not removed from cart"

        logger.info("Test passed: test_remove_item_from_cart")
