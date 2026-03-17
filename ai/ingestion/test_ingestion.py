import json
from ingestion.pipeline import IngestionPipeline


def main():

    log_file = "data/logs/corrected.gz.json"

    pipeline = IngestionPipeline(log_file)

    events = pipeline.run()

    print("\nGenerated Events:")
    print(json.dumps(events[:5], indent=4))


if __name__ == "__main__":
    main()