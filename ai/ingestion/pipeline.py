from ingestion.log_collector import LogCollector
from ingestion.log_parser import LogParser
from ingestion.log_normalizer import LogNormalizer
from ingestion.event_builder import EventBuilder


class IngestionPipeline:

    def __init__(self, log_path):

        self.collector = LogCollector(log_path)
        self.parser = LogParser()
        self.normalizer = LogNormalizer()
        self.event_builder = EventBuilder()

    def run(self):

        print("Collecting logs...")
        raw_logs = self.collector.collect_logs()

        print("Parsing logs...")
        parsed_logs = self.parser.parse(raw_logs)

        print("Normalizing logs...")
        normalized_logs = self.normalizer.normalize(parsed_logs)

        print("Building events...")
        events = self.event_builder.build_events(normalized_logs)

        return events