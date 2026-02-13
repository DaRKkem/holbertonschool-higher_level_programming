#!/usr/bin/env python3
"""Module to convert CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format and save it to data.json."""
    try:
        data = []

        with open(csv_filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        with open("data.json", "w") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except Exception:
        return False
