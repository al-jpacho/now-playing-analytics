import glob
import json
import os

RAW_DATA_DIR = "data/raw"


def test_jsonl_file_exists():
    files = glob.glob(os.path.join(RAW_DATA_DIR, "events_*.jsonl"))
    assert files, "No JSONL files found in data/raw/"


def test_jsonl_lines_are_valid_json():
    files = sorted(glob.glob(os.path.join(RAW_DATA_DIR, "events_*.jsonl")))
    latest_file = files[-1]
    with open(latest_file, "r") as f:
        lines = f.readlines()
        assert lines, "File is empty"

        for line in lines:
            try:
                event = json.loads(line)
                assert isinstance(event, dict)
            except json.JSONDecodeError:
                assert False, f"Invalid JSON line: {line.strip()}"
