#!/usr/bin/python3
"""Module to convert CSV data to JSON."""

import csv
import json


def convert_csv_to_json(filename):
    """Convert CSV file to JSON file named data.json."""
    try:
        data_list = []

        with open(filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data_list.append(row)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data_list, f, indent=4)

        return True

    except Exception:
        return False
