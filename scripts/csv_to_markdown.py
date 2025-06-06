#!/usr/bin/env python3
"""Convert resources.csv to a Markdown table grouped by category."""

import csv
from collections import defaultdict

def read_resources(path="resources.csv"):
    data = defaultdict(list)
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[row["category"]].append(row)
    return data

def to_markdown(resources):
    lines = []
    for category in sorted(resources):
        lines.append(f"### {category}")
        lines.append("| Name | URL | Description |")
        lines.append("| ---- | --- | ----------- |")
        for item in sorted(resources[category], key=lambda r: r["name"]):
            name = item["name"]
            url = item["url"]
            desc = item.get("description", "")
            lines.append(f"| [{name}]({url}) | {url} | {desc} |")
        lines.append("")
    return "\n".join(lines)

if __name__ == "__main__":
    resources = read_resources()
    md = to_markdown(resources)
    print(md)
