import csv
from datetime import datetime
from pathlib import Path


class EventLogger:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.file_path.exists():
            with self.file_path.open("w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["timestamp", "event", "detail"])

    def log(self, event_name, detail):
        timestamp = datetime.now().isoformat(timespec="seconds")

        with self.file_path.open("a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, event_name, detail])

        print(f"[EVENT] {timestamp} | {event_name} | {detail}")
