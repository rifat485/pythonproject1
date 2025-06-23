# ✅ File: 1_phase1/signal_tracker.py
import csv
import os
from datetime import datetime

LOG_FILE = 'data/signal_log.csv'


def log_signal_result(signal, result):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, 'a', newline='') as csvfile:
        fieldnames = ['datetime', 'signal', 'result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'signal': signal,
            'result': result
        })
    print(f"📝 Logged: {signal} - {result}")
