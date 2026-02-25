from collections import Counter
'''
Відображення талиці порахованих логів
'''

def display_log_counts(counts: Counter) -> None:
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")
