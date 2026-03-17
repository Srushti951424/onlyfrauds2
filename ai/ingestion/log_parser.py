import json


class LogParser:

    def parse(self, raw_logs):
        parsed_logs = []

        for log in raw_logs:
            try:
                if isinstance(log, str):
                    log = json.loads(log)

                parsed_logs.append({
                    "timestamp": log.get("timestamp"),
                    "source_ip": log.get("src_ip"),
                    "destination_ip": log.get("dst_ip"),
                    "protocol": log.get("protocol"),
                    "action": log.get("action"),
                    "bytes": log.get("bytes", 0)
                })

            except Exception:
                continue

        return parsed_logs