"""
# Appium Test Automation Framework

A comprehensive cross-platform mobile test automation framework built with 
Appium, Pytest, and Python for automating the My Demo App 
(com.saucelabs.mydemoapp.android) on both iOS and Android platforms.

## Features

- **Cross-Platform Support**: Unified API for both Android and iOS platforms
- **Page Object Model**: Clean separation of test logic and page interactions
- **Reusable Utilities**: Common gesture and action libraries
- **Comprehensive Logging**: Detailed logging for debugging and reporting
- **Screenshot on Failure**: Automatic screenshot capture on test failures
- **Pytest Integration**: Advanced test execution with markers and fixtures
- **PEP 8 & Flake8 Compliant**: Clean, maintainable, documented code

## Project Structure

```
appium_framework/
├── config/
│   ├── __init__.py
│   ├── config.py              # Central configuration management
│   └── capabilities.py        # Device capabilities
├── pages/
│   ├── __init__.py
│   ├── base_page.py          # Base page with common functionality
│   ├── login_page.py         # Login page object
│   ├── product_page.py       # Product page object
│   └── cart_page.py          # Cart page object
├── utilities/
│   ├── __init__.py
│   ├── driver_factory.py     # Driver creation and management
│   ├── mobile_gestures.py    # Cross-platform gesture utilities
│   ├── mobile_actions.py     # Common element interaction utilities
│   └── logger.py             # Custom logging utility
├── tests/
│   ├── __init__.py
│   ├── conftest.py           # Pytest fixtures and configuration
│   ├── test_login.py         # Login feature tests
│   └── test_product.py       # Product feature tests
├── reports/                   # Test reports and screenshots
├── logs/                      # Execution logs
├── requirements.txt
├── pytest.ini
└── README.md
```

## Prerequisites

1. **Python**: Version 3.8 or higher
2. **Appium Server**: Version 2.0 or higher
3. **Node.js**: For Appium installation
4. **Android SDK**: For Android testing
5. **Xcode**: For iOS testing (macOS only)

## Installation

### 1. Install Appium Server

```bash
npm install -g appium
appium driver install uiautomator2
appium driver install xcuitest
```

### 2. Clone the Repository

```bash
git clone <repository-url>
cd appium_framework
```

### 3. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

### Environment Variables

Set the following environment variables to customize the framework:

```bash
# Platform selection
export PLATFORM=android  # or ios

# Appium server
export APPIUM_SERVER_URL=http://127.0.0.1:4723

# Android device
export ANDROID_DEVICE_NAME=emulator-5554
export ANDROID_PLATFORM_VERSION=13.0

# iOS device
export IOS_DEVICE_NAME="iPhone 14"
export IOS_PLATFORM_VERSION=16.0

# Test credentials
export TEST_USERNAME=bob@example.com
export TEST_PASSWORD=10203040
```

### Editing Config Files

You can also modify `config/config.py` directly to set default values.

## Running Tests

### Start Appium Server

```bash
appium
```

### Run All Tests

```bash
pytest tests/
```

### Run Specific Test File

```bash
pytest tests/test_login.py
```

### Run Tests with Markers

```bash
# Run smoke tests only
pytest -m smoke

# Run regression tests only
pytest -m regression

# Run login feature tests
pytest -m login

# Run product feature tests
pytest -m product
```

### Run Tests in Parallel

```bash
pytest tests/ -n 2  # Run with 2 workers
```

### Generate HTML Report

```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

### Run with Verbose Output

```bash
pytest tests/ -v -s
```

## Framework Components

### 1. Configuration Management (`config/`)

- **config.py**: Central configuration class managing all settings
- **capabilities.py**: Platform-specific device capabilities

### 2. Page Objects (`pages/`)

All page objects inherit from `BasePage` which provides:
- Platform-specific locator selection
- Access to mobile actions and gestures
- Common page utilities

#### LoginPage
- `navigate_to_login()`: Navigate to login screen
- `enter_username(username)`: Enter username
- `enter_password(password)`: Enter password
- `login(username, password)`: Complete login flow
- `logout()`: Perform logout

#### ProductPage
- `get_all_products()`: Get all product elements
- `click_product_by_index(index)`: Select product by index
- `add_to_cart()`: Add product to cart
- `get_cart_count()`: Get cart badge count

#### CartPage
- `open_cart()`: Navigate to cart page
- `get_cart_items()`: Get all cart items
- `remove_item_by_index(index)`: Remove item from cart
- `proceed_to_checkout()`: Proceed to checkout

### 3. Utilities (`utilities/`)

#### MobileGestures
Cross-platform gesture utilities:
- `swipe(start_x, start_y, end_x, end_y, duration)`: Custom swipe
- `swipe_left()`, `swipe_right()`, `swipe_up()`, `swipe_down()`
- `scroll_to_element(element)`: Scroll to element
- `long_press(element, duration)`: Long press gesture
- `tap(x, y)`: Tap at coordinates
- `double_tap(element)`: Double tap gesture
- `pinch(element, percent)`: Pinch gesture
- `zoom(element, percent)`: Zoom gesture

#### MobileActions
Common element interaction utilities:
- `click(locator)`: Click element
- `send_keys(locator, text)`: Send text to element
- `get_text(locator)`: Get element text
- `get_attribute(locator, attribute)`: Get element attribute
- `is_displayed(locator)`: Check if element is displayed
- `wait_for_element(locator)`: Wait for element visibility
- `take_screenshot(name)`: Capture screenshot
- `hide_keyboard()`: Hide mobile keyboard

#### DriverFactory
- `create_driver()`: Create platform-specific driver
- `quit_driver(driver)`: Quit driver and cleanup

#### Logger
- `get_logger(name)`: Get configured logger instance

### 4. Tests (`tests/`)

#### conftest.py
Pytest fixtures:
- `driver`: Creates driver for each test
- `take_screenshot_on_failure`: Auto-capture on failures
- Test hooks for result reporting

#### Test Files
- `test_login.py`: Login functionality tests
- `test_product.py`: Product and cart tests

## Best Practices Implemented

1. **Page Object Model**: Separation of concerns
2. **DRY Principle**: Reusable utilities and base classes
3. **Explicit Waits**: Robust element waiting strategies
4. **Error Handling**: Try-catch blocks with proper logging
5. **Cross-Platform**: Unified API for both platforms
6. **Documentation**: Comprehensive docstrings
7. **Logging**: Detailed execution logging
8. **PEP 8 Compliance**: Flake8 validated code
9. **Test Isolation**: Independent test execution
10. **Fixtures**: Setup and teardown management

## Code Quality

### Run Flake8

```bash
flake8 config/ pages/ utilities/ tests/ --max-line-length=79
```

### Code Style Guidelines

- Maximum line length: 79 characters
- Docstrings for all classes and methods
- Type hints where applicable
- Descriptive variable and function names
- Comments for complex logic

## Troubleshooting

### Appium Server Issues

```bash
# Check if Appium is running
appium --version

# Start Appium with logging
appium --log-level debug
```

### Device Not Found

```bash
# List Android devices
adb devices

# List iOS simulators
xcrun simctl list devices
```

### Element Not Found

- Check locator strategy (Accessibility ID preferred)
- Increase explicit wait timeout
- Verify element hierarchy with Appium Inspector
- Check platform-specific locators

### Tests Failing Randomly

- Increase implicit/explicit wait times
- Add explicit waits for dynamic elements
- Check for animations/transitions
- Verify network connectivity for API-dependent features

## Continuous Integration

### Example GitHub Actions Workflow

```yaml
name: Mobile Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: macos-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        npm install -g appium
        appium driver install uiautomator2
    
    - name: Run tests
      run: pytest tests/ -m smoke
    
    - name: Upload reports
      uses: actions/upload-artifact@v2
      with:
        name: test-reports
        path: reports/
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License

This project is licensed under the MIT License.

## Support

For issues and questions:
- Open an issue on GitHub
- Check Appium documentation: https://appium.io/docs/
- Check Pytest documentation: https://docs.pytest.org/

## Authors

- Your Name - Initial work

## Acknowledgments

- Appium community for excellent documentation
- Pytest team for the testing framework
- SauceLabs for the My Demo App
"""