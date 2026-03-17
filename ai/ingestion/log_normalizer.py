class LogNormalizer:

    def normalize(self, parsed_logs):

        normalized = []

        for log in parsed_logs:

            normalized.append({
                "timestamp": log["timestamp"],
                "src_ip": log["source_ip"],
                "dst_ip": log["destination_ip"],
                "protocol": log["protocol"].lower() if log["protocol"] else None,
                "action": log["action"].lower() if log["action"] else None,
                "bytes_transferred": int(log["bytes"])
            })

        return normalized