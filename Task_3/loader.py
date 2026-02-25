import logging
from typing import List, Dict
from parser import parse_log_line
'''
Лише читає файл
'''

def load_logs(file_path: str) -> List[Dict[str, str]]:
    logs = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            try:
                parsed = parse_log_line(line)
                logs.append(parsed)
            except ValueError:
                logging.warning(f"Skipping malformed line: {line.strip()}")

    return logs