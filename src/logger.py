import logging
import os
from Lib.datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(

    filename= LOG_FILE_PATH,
    format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,
)


# if __name__ == "__main__": # If you are running this file only then the below code will be executed 
#     # and if you are importing it somewehere else then the below code won't work
#     logging.info("Execution has started")