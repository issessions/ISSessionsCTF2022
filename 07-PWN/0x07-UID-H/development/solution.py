import hashlib
import string

s = string.ascii_lowercase

with open("hashes.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        for c in s:
            if hashlib.md5(c.encode()).hexdigest() == line.strip():
                print(c, end="")
                break