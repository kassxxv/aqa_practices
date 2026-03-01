import logging

logger = logging.getLogger('decorator_logger')
logger.setLevel(logging.DEBUG)


stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))


logger.addHandler(stream_handler)
