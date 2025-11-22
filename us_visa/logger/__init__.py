# Import the logging module (built-in in Python)
# This module helps to record messages like errors, warnings, info, and debug logs.
import logging

# Import the OS module for interacting with the operating system
# Used to create directories and handle file paths.
import os

# Import the 'from_root' function which returns the root directory of your project
# This ensures that logs are always stored inside the project, not depending on where the script is run.
from from_root import from_root

# Import datetime class to get the current date and time
# We use it for generating a unique log file name based on time.
from datetime import datetime

# Create a log file name using current date & time
# strftime() formats the date-time into a string: month_day_year_hour_minute_second.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Directory where all log files will be saved
# Instead of mixing logs in root, we store them in a separate 'logs' folder.
log_dir = "logs"

# Create the complete path for the log file
# Example: project_root/logs/12_01_2025_14_55_30.log
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

# Create the logs directory if it does not exist
# os.path.dirname(logs_path) extracts only the folder path (without the log file name)
# exist_ok=True means: do NOT throw error if folder already exists
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# Configure the logging system
logging.basicConfig(
    # Specify the file where logs will be saved
    filename=logs_path,

    # Define the format of each log message
    # %(asctime)s -> timestamp when the log was created
    # %(levelname)s -> type of log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    # %(message)s -> the actual log message
    format="[%(asctime)s] %(levelname)s - %(message)s",

    # Set the minimum level of logging that will be recorded
    # DEBUG captures all levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    level=logging.DEBUG,
)

# Make logging available for import
__all__ = ['logging']