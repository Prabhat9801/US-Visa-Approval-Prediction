# Importing the os module (not used here but usually useful for file paths or system operations)
import os

# Importing sys to access exception information (error details)
import sys


# This function creates a detailed error message
def error_message_detail(error, error_detail: sys):

    # exc_info() returns a tuple: (exception_type, exception_obj, traceback_obj)
    # We only care about the traceback object, so we use placeholders (_, _)
    # example of exc_info() output: (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x0000023F4C1A8C80>)
    # exapmple of exception_type: <class 'ZeroDivisionError'>
    # example of exception_obj: ZeroDivisionError('division by zero')
    # example of traceback_obj: <traceback object at 0x0000023F4C1A8C80> means - the location in memory where the traceback object is stored
    # trackback is object is used to get information about the call stack at the point where the exception occurred.
    _, _, exc_tb = error_detail.exc_info()

    # Extract the file name where the error happened
    # exc_tb -> traceback
    # tb_frame -> frame object means in simple words it represents the execution frame where the error occurred
    # f_code -> code object means it contains compiled bytecode and other details about the function or module
    # co_filename -> file name of the script where error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a detailed error message
    # Includes: file name, line number, and original error message
    error_message = (
        "Error occurred in python script name [{0}] line number [{1}] error message [{2}]"
        .format(
            file_name,   # Name of the file where error happened
            exc_tb.tb_lineno,  # Line number where exception occurred
            str(error)   # Actual error message
        )
    )

    return error_message   # Return the detailed error message



# Custom Exception Class for the project
class USvisaException(Exception):

    # Constructor for the custom exception
    # error_message = message passed when raising exception
    # error_detail = sys object to extract traceback information
    def __init__(self, error_message, error_detail):
        """
        :param error_message: error message in string format
        """

        # Call the parent Exception class constructor
        super().__init__(error_message)

        # Create a detailed error message by calling the function above
        self.error_message = error_message_detail(
            error_message,          # original error
            error_detail=error_detail   # sys object to extract traceback
        )

    # This method returns the custom detailed error message
    def __str__(self):

        # Whenever exception is printed or converted to string,
        # this detailed message will be shown.
        return self.error_message

__all__ = ['USvisaException']