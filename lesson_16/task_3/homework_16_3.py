import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'task_2'))
from my_logger import logger
import xml.etree.ElementTree as ET

def find_incoming(xml_path: str, group_number: int) -> str:
    root = ET.parse(xml_path).getroot()
    incoming = next((group.findtext("timingExbytes/incoming") for group in root.findall("group") if group.findtext("number") == str(group_number)), None)
    logger.info(f"Group = {group_number}, timingExbytes/incoming = {incoming}")
    return incoming


if __name__ == "__main__":
    for num in [0, 1, 2, 4, 5, 99]:
        find_incoming("groups.xml", num)