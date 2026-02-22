import json
from my_logger import logger
import os
folder = 'work_with_json'

def is_valid_json(filepath:str):
    try:
        with open(filepath, encoding='utf-8') as file:
            json.load(file)
    except json.JSONDecodeError as e:
        logger.error(f'Файл {filepath} не валідний: {e}')

for filename in os.listdir(folder):
    if filename.endswith('.json'):
        filepath = os.path.join(folder, filename)
        is_valid_json(filepath)


