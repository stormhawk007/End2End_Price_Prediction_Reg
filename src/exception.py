import sys #importing sys library

def error_message_detail(error,error_detail:sys): #importing error_detail from sys library
    _,_,exc_tb = error_detail.exc_info() #third variable has all the information related to 
                                         # errors such as line no.,error details etc
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

# We are creating a new class which simply imports all the functionality of Exception class in python as parent class and 
# then we will simply call the custom function we created above to give custom message as output in case of errors

class CustomException(Exception): # Inheritting exception class
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message) 
        self.error_message = error_message_detail(error_message,error_detail=error_detail)


    def __str__(self): # for printing error message
        return self.error_message
    

# if __name__ == "__main__":
#     try: 
#         a = 1/0
#     except Exception as e:
#         logging.info("Execution has started")
#         raise CustomException(e,sys)
    