import sys

"""
Custom Exception Handler Module

This module provides a custom exception class for handling and formatting error messages
in a consistent way across the application.

Classes:
    CustomException: A custom exception class that captures error details and provides
                    formatted error messages with file name and line number information.

Methods:
    CustomException.__init__: Initializes the custom exception with error message and details
    CustomException.get_error_message: Static method to format error messages with file and line info

Example:
    try:
        # Some code that might raise an exception
        raise ValueError("Invalid input")
    except Exception as e:
        raise CustomException(str(e), sys) from e
"""


class CustomException(Exception):
    def __init__(self, error_message: str, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_details = error_details
    
    @staticmethod
    def get_error_message(error_details: sys) -> str:
        _, _, exc_tb = error_details.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}]"
        return error_message