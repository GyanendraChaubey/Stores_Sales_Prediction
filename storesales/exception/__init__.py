from fileinput import filename
import os
import sys

class StoresalesException(Exception):

    def __init__(self, error_meassge:Exception, error_detail:sys):
        super().__init__(error_meassge)
        self.error_message=StoresalesException.get_detailed_error_message(error_meassge=error_meassge,
        error_detail=error_detail)

    
    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        """
        error_meassge: Exception object

        error_detail: object of sys module
        """

        _,_,exec_tb = error_detail.exc_info()
        line_number=exec_tb.tb_frame.f_lineno
        file_name=exec_tb.tb_frame.f_code.co_filename
        error_message=f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"
        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return StoresalesException().__name__.str()