import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass

    #def get_logger(self):
        #logger_name = inspect.stack()[1][3]     #get the name of the correct test case file name
        #logger = logging.getLogger(logger_name)

        #file_handler = logging.FileHandler('logfile.log')  # specifying file location
        #formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        #file_handler.setFormatter(formatter)

        #logger.addHandler(file_handler)  # filehandler object

        #logger.setLevel(logging.INFO)  # setting the level (displays the set level + the following levels)
        #return logger


