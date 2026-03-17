from collections import defaultdict


class EventBuilder:

    def build_events(self, normalized_logs):

        events = defaultdict(list)

        for log in normalized_logs:
            key = (log["src_ip"], log["dst_ip"], log["protocol"])

            events[key].append(log)

        built_events = []

        for key, logs in events.items():

            total_bytes = sum(l["bytes_transferred"] for l in logs)

            built_events.append({
                "src_ip": key[0],
                "dst_ip": key[1],
                "protocol": key[2],
                "log_count": len(logs),
                "total_bytes": total_bytes
            })

        return built_events