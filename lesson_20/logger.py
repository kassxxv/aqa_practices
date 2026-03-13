import logging

logger = logging.getLogger('heartbeat_validator')
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('hb_test.log', encoding='utf-8')
file_handler.setLevel(logging.WARNING)

formatter = logging.Formatter('%(levelname)s: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
