import os, sys

class CreditException(Exception):
    """Creating Custom exception to handle errors

    Args:
        Exception (Exception): Inheriting Exception class from python
    """
    def __init__(self, error_message:Exception, error_details:sys):
        """Passing the error information to parent class and generating custom error

        Args:
            error_message (Exception): Passing error message to Exception class
            error_details (sys): Passing details of the error (line no: row number no: etc) to sys class
        """
        super().__init__(error_message) ## Exception class __init__(self, error_message)
        self.error_message= CreditException.get_detailed_error_message(error_message= error_message,
                                                                        error_details= error_details)
    
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_details:sys)-> str:
        """Generating details error message out of exception details

        Args:
            error_message (Exception): Exception details
            error_details (sys): error details such as line no etc.

        Returns:
            str: Exception string
        """
        _,_,exception_traceback=error_details.exc_info()
        line_number= exception_traceback.tb_lineno
        file_name= exception_traceback.tb_frame.f_code.co_filename

        ## Error_message
        error_message=f"Error occured in Script: [{file_name}] at Line number: [{line_number}] error message: [{error_message}]"
        return error_message
    
    ## When ever we call CreditException it will ping __str__ method
    def __str__(self):
        """__str__ is useful when you try to print object. Usually if __str__ is not specified
        and if we try to print CreditException it would return class object.
        If we specify __str__ and print object it would print what ever we are returning in
        __str__(self): method. 
        """
        return self.error_message
    def __repr__(self)->str:
        return CreditException.__name__.str()