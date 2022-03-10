#!/usr/bin/env python3
import os
import re
import sys
import requests
import yaml
import traceback


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


def main():
    cwd = os.getcwd()
    path = cwd[:-6]
    pattern = re.compile(rf"^{path}/\d\d-[\w_]+/[^/]+$")

    if sys.argv[1] != "install" and sys.argv[1] != "sync":
        print("\nUSAGE:")
        print("\n  OPTION #1: installing all challenges")
        print("  ./ctfd-upload.py install")
        print("\n  OPTION #2: update challenges")
        print("  ./ctfd-upload.py sync\n")
        exit(1)

    # get the list of challenges
    url = "https://ctf.issessions.ca/api/v1/challenges"
    access_token = ""
    headers = {"Authorization": f"Token {access_token}"}
    challenges = requests.get(url, headers=headers, json=True).json()["data"]
    challenges = [x["name"] for x in challenges]

    for root, dirs, files in walklevel(path=path, depth=2):
        if pattern.match(root):
            try:
                if sys.argv[1] == "install":
                    with open(f"{root}/documentation/manifest.yml", "r") as file:
                        challenge = yaml.safe_load(file)["challenge"]["name"]
                        if not challenges.__contains__(challenge):
                            os.system(f"{cwd}/ctf challenge {sys.argv[1]} {root}")
                else:
                    os.system(f"{cwd}/ctf challenge {sys.argv[1]} {root}")
            except Exception:
                print("ERROR: An error has occurred.")
                traceback.print_exc()
                exit(1)


if __name__ == "__main__":
    main()
