"""Logging utility for the test automation framework."""

import logging
import os
from datetime import datetime
from config.config import Config


class Logger:
    """
    Custom logger for test automation framework.

    Provides logging functionality with file and console handlers.
    """

    @staticmethod
    def get_logger(name):
        """
        Create and configure a logger instance.

        Args:
            name (str): Name of the logger (usually __name__)

        Returns:
            logging.Logger: Configured logger instance
        """
        logger = logging.getLogger(name)

        if not logger.handlers:
            logger.setLevel(logging.DEBUG)

            # Create logs directory if it doesn't exist
            os.makedirs(Config.LOGS_DIR, exist_ok=True)

            # File handler
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = os.path.join(
                Config.LOGS_DIR,
                f"test_execution_{timestamp}.log"
            )
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            # Formatter
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
