#!/usr/bin/python3

"""Log parsing"""

import re
import sys
from collections import defaultdict, OrderedDict

log_format_regex = r'^((?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' \
    r'|Holberton)\s*-\s*\[([^\]]+)\] "GET \/projects\/260 HTTP\/1\.1" ' \
    r'(200|301|400|401|403|404|405|500|Hello) (\d+)$'


def get_log_info(line: str) -> dict:
    """get info for each server log/line"""
    __match = re.match(log_format_regex, line)

    if not bool(__match):
        return {"is_valid_server_log": False}

    return {
        "is_valid_server_log": bool(bool(__match)),
        "status_code": __match.group(3),
        "file_size": int(__match.group(4))
    }


def print_stats(stat: dict):
    """print statistics"""

    print(f'File size: {stat["file_size"]}')
    if not stat:
        return

    ordered_stat = OrderedDict(sorted(stat.items()))

    [
        print(f'{status_code}: {count}')
        for status_code, count in ordered_stat.items()
        if status_code != "file_size" and status_code.isdigit()
    ]


def log_parse():
    """readline and computes metrics"""
    metrics = defaultdict(int)

    for idx, line in enumerate(sys.stdin):
        if idx % 10 == 0 and idx != 0:
            print_stats(metrics)

        log = get_log_info(line)
        if (log["is_valid_server_log"]):
            metrics[log["status_code"]] += 1
            metrics["file_size"] += log["file_size"]

    print_stats(metrics)


if __name__ == "__main__":
    log_parse()
