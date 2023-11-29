import logging
from datetime import date
import os

def createLogObj(name='Default', logLevel=logging.INFO):
    os.makedirs('logs/', exist_ok=True)
    fileName = 'logs/' + str(date.today()) + '.log'
    msgFormat = '%(name)s %(asctime)s: %(message)s'
    logging.basicConfig(filename=fileName, format=msgFormat, level=logLevel)
    return logging.getLogger(name)

# tests to check logger and options are working
if __name__ == '__main__':
    # This is some example python code
    test_logger = createLogObj("TestLogger")
    test_logger.log(msg="Starting Logging Test", level=logging.INFO)
    example_input = input("Please Enter Something: ")
    test_logger.log(msg=f'Example input {example_input} was recieved', level=logging.INFO)
    test_logger.log(msg='End Logging Test', level=logging.INFO)