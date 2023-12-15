# import logging
#
# def test_logging_demo():
#     logger = logging.getLogger(__name__)
#
#     file_handler = logging.FileHandler('logfile.log')      #specifying file location
#     formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
#     file_handler.setFormatter(formatter)
#
#     logger.addHandler(file_handler)     #filehandler object
#
#     logger.setLevel(logging.CRITICAL)       #setting the level (displays the set level + the following levels)
#     logger.debug("A debug statement executed")
#     logger.info("An information statement  is executed")
#     logger.warning("A warning statement is executed")
#     logger.error("An error statement executed")
#     logger.critical("A critical error statement executes")
