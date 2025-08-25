import logging
import os 
from datetime import datetime


"""
Logger Module
------------

This module provides logging functionality for the application with the following features:

- Creates a logs directory if it doesn't exist
- Generates unique log files with timestamps
- Configures logging with both file and console output
- Provides a helper function to get logger instances

Usage:
------
logger = get_logger(__name__)
logger.info("Log message")

The log files are stored in the 'logs' directory with filenames in the format:
MM_DD_YYYY_HH_MM_SS.log

Log Format:
-----------
[ timestamp ] line_number logger_name - log_level - message

The logger is configured to:
- Log to both file and console
- Use INFO as the default log level
- Include timestamp, line number, logger name, log level and message in the output
"""

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.addHandler(logging.StreamHandler())
    return logger
