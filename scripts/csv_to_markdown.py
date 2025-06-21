#!/usr/bin/env python3
"""Convert ``resources.csv`` to a Markdown bullet list grouped by category."""

import argparse
import csv
from collections import defaultdict


def read_resources(path: str = "resources.csv"):
    data = defaultdict(list)
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[row["category"]].append(row)
    return data


def to_markdown(resources):
    """Return Markdown bullet list for the given resources."""

    lines = []
    for category in sorted(resources):
        lines.append(f"### {category}")

        items = sorted(resources[category], key=lambda r: r["name"])
        for item in items:
            name = item["name"]
            url = item["url"]
            desc = item.get("description", "")
            if desc:
                lines.append(f"- [{name}]({url}) – {desc}")
            else:
                lines.append(f"- [{name}]({url})")

        lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert resources.csv to Markdown")
    parser.add_argument(
        "path",
        nargs="?",
        default="resources.csv",
        help="Path to the CSV file (default: resources.csv)",
    )

    args = parser.parse_args()

    resources = read_resources(args.path)
    md = to_markdown(resources)
    print(md)


if __name__ == "__main__":
    main()
