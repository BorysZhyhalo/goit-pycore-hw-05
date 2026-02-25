from typing import Dict
'''
Парсинг одного рядка. Якщо довжина не дорівнює 4, то піднімаємо помилку, яка логується
'''

def parse_log_line(line: str) -> Dict[str, str]:
    parts = line.strip().split(maxsplit=3)
    if len(parts) != 4:
        raise ValueError("Invalid log format")

    date, time, level, message = parts

    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message,
    }