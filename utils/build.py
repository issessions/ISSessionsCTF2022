#!/usr/bin/env python3
import os
import re
import shutil
import sys
from os.path import basename, normpath
from zipfile import ZipFile
import traceback

import yaml

try:
    from yaml import CDumper as Dumper
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Dumper, Loader


def main():
    if get(sys.argv, 1) == "make":
        print(f">>>Starting Build Process<<<")
        try:
            if get(sys.argv, 2):
                directory = sys.argv[2]
                if directory == ".":
                    directory = os.getcwd()
                build_challenge(directory)
            else:
                print(
                    "ERROR: You must provide a path to the challenge directory you wish to build."
                )
        except Exception:
            print("ERROR: An error has occurred.")
    elif get(sys.argv, 1) == "--all" or get(sys.argv, 1) == "-a":
        print(f">>>Starting Build Process<<<")
        path = os.getcwd()[:-6]
        pattern = re.compile(rf"^{path}/\d\d-[\w\W]+/[^/]+$")
        for root, dirs, files in walklevel(path=path, depth=2):
            if pattern.match(root):
                try:
                    build_challenge(root)
                except Exception:
                    print("ERROR: An error has occurred.")
                    traceback.print_exc()
                    exit(1)
    else:
        print("\nUSAGE:")
        print("\n  OPTION #1: Prepare a single challenge for deployment to CTFd.")
        print("  build.py make [challenge_directory]")
        print("\n  OPTION #2: Prepare all challenge for deployment to CTFd.")
        print("  build.py [--all|-a]\n")


# credits: @TheMatt2
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


def zip_directory(zip_filename, directory):
    with ZipFile(zip_filename, "w") as zipObj:
        for folderName, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(folderName, filename)
                zipObj.write(file_path, basename(file_path))


def verify_challenge(challenge):
    # check for required settings
    required = {
        "name": str,
        "author": str,
        "category": str,
        "description": str,
        "value": int,
        "type": str,
    }
    for section in required:
        if not challenge.get(section):
            print(f"ERROR: key: '{section}' is missing from the manifest file")
            raise
        if not isinstance(challenge.get(section), required[section]):
            print(f"ERROR: key: '{section}' is supposed to be a '{required[section]}'")
            raise
    # check challenge type and verify structure
    extra = {"minimum": int, "initial": int, "decay": int}
    if challenge["type"] == "dynamic":
        manifest_extra = challenge.get("extra")
        if manifest_extra:
            if isinstance(manifest_extra, dict):
                for section in extra:
                    if not manifest_extra.get(section):
                        print(
                            f"ERROR: key: 'extra.{section}' is missing from the manifest file"
                        )
                        raise
                    if not isinstance(manifest_extra.get(section), extra[section]):
                        print(
                            f"ERROR: key: 'extra.{section}' is supposed to be a '{extra[section]}'"
                        )
                        raise
            else:
                print(f"ERROR: key: 'extra' is supposed to be a '{dict}'")
                raise
        else:
            print(f"ERROR: key: 'extra' is missing from the manifest file")
            raise
    # check for types optional settings
    option = {
        "connection_info": str,
        "attempts": int,
        "topics": list,
        "tags": list,
        "files": list,
        "hints": list,
        "requirements": list,
        "state": str,
        "version": str,
    }
    for section in option:
        if challenge.get(section) and not isinstance(
            challenge.get(section), option[section]
        ):
            print(f"ERROR: key: '{section}' is supposed to be a '{option[section]}'")
            raise


def build_challenge(root):
    root = normpath(root)
    name = "/".join(root.split("/")[-2:])
    challenge_key = basename(root)
    player_files_dir = f"{root}/player_files/"
    player_files_zip = f"{challenge_key.split('-')[1]}.zip"
    player_files_zip_from_root = f"{root}/{player_files_zip}"
    instructions_file = f"{root}/documentation/instructions.txt"
    hint_file = f"{root}/documentation/hint.txt"
    manifest_file = f"{root}/documentation/manifest.yml"
    challenge_dot_yaml_file = f"{root}/challenge.yml"
    print(f"\n>>>Preparing {name} for deployment to CTFd<<<")
    if not os.path.exists(f"{root}/documentation"):
        print(f"ERROR: No documentation folder found in {root}.")
        raise

    # parse manifest file
    if os.path.exists(manifest_file):
        try:
            print("INFO: reading manifest file.")
            with open(manifest_file) as file:
                challenge = yaml.load(file, Loader=Loader)["challenge"]
        except (yaml.YAMLError, KeyError):
            print(
                f"ERROR: Encountered a YAML parsing error when parsing {manifest_file}."
            )
            raise
    else:
        print(f"ERROR: No manifest file found in {root}.")
        raise
    # parse instructions file
    if os.path.exists(instructions_file):
        try:
            print("INFO: reading instructions.txt file.")
            with open(instructions_file) as file:
                instructions = file.read().replace("\n", "<br>")
        except OSError:
            print(f"ERROR: Error reading: {instructions_file}.")
            raise
        print("INFO: Adding content of instructions.txt to challenge metadata.")
        challenge.update({"description": instructions})
    else:
        print(
            f"ERROR: No instructions file found in the {root}/documentation/ directory."
        )
        raise
    # parse hint file
    if os.path.exists(hint_file):
        try:
            print("INFO: reading hint.txt file.")
            with open(hint_file) as file:
                hint = file.read().replace("\n", "<br>")
        except OSError:
            print(f"ERROR: Error reading: {hint_file}.")
        hint_cost = challenge.get("hint_cost", None)
        if hint_cost is not None:
            print("INFO: Adding content of hint.txt to challenge metadata.")
            challenge.update(
                {"hints": [{"content": hint, "cost": challenge["hint_cost"]}]}
            )
            challenge.pop("hint_cost", None)
        else:
            print(
                f"ERROR: No hint_cost specified even though a hint file was found in the"
                f" {root}/documentation/ directory."
            )
            raise
    # check to see if player_files directory exists and zip contents
    if os.path.exists(player_files_dir):
        print("INFO: Copying instructions.txt file into player_files directory.")
        shutil.copy(src=instructions_file, dst=player_files_dir)
        print(
            f"INFO: Zipping player_files directory into {player_files_zip_from_root}."
        )
        zip_directory(
            zip_filename=player_files_zip_from_root, directory=player_files_dir
        )
        print("INFO: Adding player files archive location to challenge metadata.")
        challenge.update({"files": [player_files_zip]})
    else:
        print(f"INFO: No player_files directory found for {challenge_key}.")

    # check to see if challenge.yml data is formatted properly
    verify_challenge(challenge)

    # write the data to a file
    try:
        with open(challenge_dot_yaml_file, "w") as file:
            print("INFO: Dumping challenge metadata into CTFd challenge.yml file.")
            yaml.dump(challenge, file)
    except yaml.YAMLError:
        print("ERROR: An error occurred while dumping the challenge.yml file.")
        raise
    except OSError:
        print(f"ERROR: error creating/writing to {challenge_dot_yaml_file}.")
        raise


def get(ll, index):
    try:
        return ll[index]
    except IndexError:
        return None


if __name__ == "__main__":
    main()
