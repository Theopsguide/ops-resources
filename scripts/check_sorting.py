#!/usr/bin/env python3
"""Verify that resources.csv is alphabetically sorted within each category."""

import csv
import sys
from collections import OrderedDict


def load_by_category(path="resources.csv"):
    data = OrderedDict()
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row["category"]
            data.setdefault(cat, []).append(row["name"])
    return data


def check_sorted(data):
    errors = []
    for category, names in data.items():
        sorted_names = sorted(names, key=str.casefold)
        if names != sorted_names:
            errors.append(category)
    return errors


def main(path="resources.csv") -> int:
    data = load_by_category(path)
    errors = check_sorted(data)
    if errors:
        for cat in errors:
            print(f"Entries for category '{cat}' are not alphabetically sorted.")
        return 1
    print("All categories sorted correctly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
