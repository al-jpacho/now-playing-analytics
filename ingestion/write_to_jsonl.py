import json
import os
import time
from datetime import datetime
from pathlib import Path

from event_simulation.generate_events import generate_event

RAW_DATA_DIR = Path("data/raw")


def get_current_filepath(current_hour: str) -> str:
    """
    Generates the file path for the current hour's events JSONL file.

    Args:
        current_hour (str): The current hour in 24-hour format.

    Returns:
        str: The file path to the JSONL file containing events for the specified hour.
    """

    return f"{RAW_DATA_DIR}/events_{current_hour}.jsonl"


def ensure_raw_data_dir():
    os.makedirs(RAW_DATA_DIR, exist_ok=True)


def main():
    ensure_raw_data_dir()

    current_hour = None
    current_file = None

    try:
        while True:
            now = datetime.now()
            event_hour = now.strftime("%Y-%m-%d-%H")

            if event_hour != current_hour:
                if current_file:
                    current_file.close()
                current_hour = event_hour
                current_filepath = get_current_filepath(current_hour)
                current_file = open(current_filepath, "a")

            event = generate_event()
            current_file.write(json.dumps(event) + "\n")
            current_file.flush()

            time.sleep(1)

    except KeyboardInterrupt:
        if current_file:
            current_file.close()
        print("Event generation stopped.")


if __name__ == "__main__":
    main()
