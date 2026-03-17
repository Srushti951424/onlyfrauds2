import json
import gzip
from pathlib import Path


class LogCollector:
    def __init__(self, log_path):
        self.log_path = Path(log_path)

    def collect_logs(self):
        logs = []

        if self.log_path.suffix == ".gz":
            with gzip.open(self.log_path, "rt", encoding="utf-8") as f:
                for line in f:
                    logs.append(line.strip())

        elif self.log_path.suffix == ".json":
            with open(self.log_path, "r") as f:
                logs = json.load(f)

        else:
            with open(self.log_path, "r") as f:
                logs = f.readlines()

        return logs