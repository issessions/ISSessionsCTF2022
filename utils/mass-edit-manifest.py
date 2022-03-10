#!/usr/bin/env python3
import os
import re
import sys
import requests
import yaml
import traceback
import pprint


def main():
    p = pprint.PrettyPrinter(indent=4).pprint
    cwd = os.getcwd()
    path = cwd[:-6]
    pattern = re.compile(rf"^{path}/\d\d-[\w_]+/[^/]+$")
    for root, dirs, files in walklevel(path=path, depth=2):
        if pattern.match(root):
            path = f"{root}/documentation/manifest.yml"
            with open(path, "r") as file:
                challenge = file.read()

            challenge = challenge.replace("state: hidden", "state: visible")

            with open(path, "w") as file:
                file.write(challenge)


def walklevel(path, depth=1):
    """It works just like os.walk, but you can pass it a level parameter
    that indicates how deep the recursion will go.
    If depth is 1, the current directory is listed.
    If depth is 0, nothing is returned.
    If depth is -1 (or less than 0), the full depth is walked.
    """
    if depth < 0:
        for root, dirs, files in os.walk(path):
            yield root, dirs[:], files
        return
    elif depth == 0:
        return

    base_depth = path.rstrip(os.path.sep).count(os.path.sep)
    for root, dirs, files in os.walk(path):
        yield root, dirs[:], files
        cur_depth = root.count(os.path.sep)
        if base_depth + depth <= cur_depth:
            del dirs[:]


if __name__ == "__main__":
    main()
