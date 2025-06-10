#!/usr/bin/env python3
"""Check that all URLs in resources.csv return HTTP 200."""

import argparse
import csv
import sys

import requests


DEFAULT_TIMEOUT = 5


def read_urls(path: str):
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row["name"], row["url"]


def check_links(path: str, timeout: int) -> int:
    failures = []
    for name, url in read_urls(path):
        try:
            resp = requests.get(url, timeout=timeout, allow_redirects=True, stream=True)
            resp.close()
            if resp.status_code != 200:
                failures.append((name, url, resp.status_code))
        except requests.RequestException as e:
            failures.append((name, url, str(e)))

    if failures:
        print("Broken links found:")
        for name, url, info in failures:
            print(f"- {name}: {url} ({info})")
        return 1
    else:
        print("All links returned HTTP 200.")
        return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify that URLs in resources.csv are reachable")
    parser.add_argument(
        "path",
        nargs="?",
        default="resources.csv",
        help="Path to the CSV file (default: resources.csv)",
    )
    parser.add_argument(
        "--timeout",
        "-t",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"Request timeout in seconds (default: {DEFAULT_TIMEOUT})",
    )

    args = parser.parse_args()
    return check_links(args.path, args.timeout)


if __name__ == "__main__":
    sys.exit(main())
