from datetime import datetime
from logger import logger

filtered_log = []
with open('hblog.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if 'Key TSTFEED0300|7E3E|0400' in line:
            filtered_log.append(line.rstrip('\n'))
filtered_log.reverse()

def analyze_log_file_heartbeat(logs:list[str]):
    prev_date = None
    for log in logs:
        idx = log.find('Timestamp ')
        time_str = log[idx+10:idx+18]
        date = datetime.strptime(time_str, "%H:%M:%S")
        if prev_date:
            differences = (date - prev_date).total_seconds()
            if 31 < differences < 33:
                logger.warning(f'Heartbeat delay {differences}s at {time_str}')
            elif differences >= 33:
                logger.error(f'Heartbeat delay {differences}s at {time_str}')
        prev_date = date

analyze_log_file_heartbeat(filtered_log)