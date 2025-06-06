#!/usr/bin/env python3
"""Convert ``resources.csv`` to a Markdown table or bullet list grouped by
category.

By default a bullet list is produced. Use ``--style table`` to generate a
table instead."""

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


def to_markdown(resources, *, style: str = "bullet"):
    """Return Markdown for the given resources.

    ``style`` may be ``"table"`` or ``"bullet"``.
    """

    lines = []
    for category in sorted(resources):
        lines.append(f"### {category}")

        items = sorted(resources[category], key=lambda r: r["name"])
        if style == "table":
            lines.append("| Name | URL | Description |")
            lines.append("| ---- | --- | ----------- |")
            for item in items:
                name = item["name"]
                url = item["url"]
                desc = item.get("description", "")
                lines.append(f"| [{name}]({url}) | {url} | {desc} |")
        else:  # bullet list
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
        "--style",
        choices=["table", "bullet"],
        default="bullet",
        help="Output style: 'table' for a Markdown table or 'bullet' for a bullet list.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="resources.csv",
        help="Path to the CSV file (default: resources.csv)",
    )

    args = parser.parse_args()

    resources = read_resources(args.path)
    md = to_markdown(resources, style=args.style)
    print(md)


if __name__ == "__main__":
    main()
