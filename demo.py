from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

# logging.info("This is an info message from demo.py")
try:
    a = 1 / 0
except Exception as e:
    logging.info("Divided by zero error occurred")
    raise USvisaException(e, sys)