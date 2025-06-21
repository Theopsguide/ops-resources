#!/usr/bin/env python3
"""Filter rows in resources.csv by category."""

import argparse
import csv
import sys


def load_rows(path: str) -> list[dict[str, str]]:
    """Return list of rows from the CSV file."""
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def filter_by_category(rows: list[dict[str, str]], category: str) -> list[dict[str, str]]:
    """Return rows matching the given category."""
    if category is None:
        return rows
    return [row for row in rows if row["category"] == category]


def main() -> None:
    parser = argparse.ArgumentParser(description="Filter resources.csv by category")
    parser.add_argument(
        "--category",
        help="Category to filter (if omitted, all rows are printed)",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="resources.csv",
        help="Path to the CSV file (default: resources.csv)",
    )
    args = parser.parse_args()

    rows = load_rows(args.path)
    matches = filter_by_category(rows, args.category)

    writer = csv.DictWriter(sys.stdout, fieldnames=["category", "name", "url", "description"])
    writer.writeheader()
    for row in matches:
        writer.writerow(row)


if __name__ == "__main__":
    main()
