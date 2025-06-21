#!/usr/bin/env python3
"""Sort entries within each category of resources.csv alphabetically."""

import csv
from collections import OrderedDict


def load_rows(path="resources.csv"):
    by_cat = OrderedDict()
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row["category"]
            by_cat.setdefault(cat, []).append(row)
    return reader.fieldnames, by_cat


def write_sorted(fieldnames, by_cat, path="resources.csv"):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for cat, rows in by_cat.items():
            for row in sorted(rows, key=lambda r: r["name"].casefold()):
                writer.writerow(row)


def main(path="resources.csv"):
    fieldnames, by_cat = load_rows(path)
    write_sorted(fieldnames, by_cat, path)
    print(f"Sorted entries written back to {path}.")


if __name__ == "__main__":
    main()
