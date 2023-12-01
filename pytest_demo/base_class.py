import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    # def get_logger(self):
        # logger_name = inspect.stack()[1][3]     #get the name of the correct test case file name
        # logger = logging.getLogger(logger_name)

        # file_handler = logging.FileHandler('logfile.log')  # specifying file location
        # formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        # file_handler.setFormatter(formatter)

        # logger.addHandler(file_handler)  # filehandler object

        # logger.setLevel(logging.INFO)  # setting the level (displays the set level + the following levels)
        # return logger
    def verify_link_presence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

