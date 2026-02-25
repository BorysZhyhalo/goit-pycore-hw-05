from collections import Counter
from typing import List, Dict
'''
Підраховуємо к-ть логів через Counter та фільтруємо по level
'''

def count_logs_by_level(logs: List[Dict[str, str]]) -> Counter:
    return Counter(log["level"] for log in logs)


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    level = level.upper()
    return [log for log in logs if log["level"] == level]