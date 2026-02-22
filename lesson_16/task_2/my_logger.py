import logging

logger = logging.getLogger('json_validator')
logger.setLevel(logging.INFO)


file_handler = logging.FileHandler('json__validate.log', encoding='utf-8')
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
