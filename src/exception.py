import sys
import logging
from logger import logging  # Import the logging configuration from logger.py

# Function to get detailed error message
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Extract traceback details
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file name where the error occurred
    error_message = 'Error occurred in python script [{0}] line number [{1}] error message [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error)
    )  # Format the error message
    return error_message

# Custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call the base class constructor
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
        
        # Log the error message to the log file
        logging.error(self.error_message)  # Log the error message with traceback

    def __str__(self):
        return self.error_message  # Return the detailed error message
