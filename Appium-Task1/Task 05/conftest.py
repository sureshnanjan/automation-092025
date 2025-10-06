def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        help="Platform to run tests on: android or ios"
    )
