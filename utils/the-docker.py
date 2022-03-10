#!/usr/bin/env python3
import os
import re
import subprocess
from termcolor import colored


def main():
    path = os.getcwd()
    path = path[:-6]
    docker = re.compile(rf"^{path}/\d\d-\w+/[^/]+/docker_images$")
    k8s = re.compile(rf"^{path}/\d\d-\w+/[^/]+/k8s$")

    for root, dirs, files in walklevel(path=path, depth=3):
        if docker.match(root):
            name = f"gcr.io/issessions/{root.split('/')[-2].split('-')[1].lower()}"
            try:
                if dirs:
                    for dir in dirs:
                        if dir == "nginx":
                            continue
                        build = f"docker build -t {name}-{dir} {root}/{dir}"
                        print(colored(f"Building {name}-{dir}", "green"))
                        subprocess.run(build.split())
                        push = f"docker push {name}-{dir}"
                        print(colored(f"Pushing {name}-{dir}", "green"))
                        subprocess.run(push.split())
                else:
                    build = f"docker build -t {name} {root}"
                    print(colored(f"Building {name}", "green"))
                    subprocess.run(build.split())
                    push = f"docker push {name}"
                    print(colored(f"Pushing {name}", "green"))
                    subprocess.run(push.split())
            except Exception:
                print("ERROR: An error has occurred.")
                exit(1)
        if k8s.match(root):
            try:
                cmd = f"kubectl apply -f {root}"
                print(colored(f"Applying k8s {root}", "green"))
                subprocess.run(cmd.split())
            except Exception:
                print("ERROR: An error has occurred.")
                exit(1)


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
