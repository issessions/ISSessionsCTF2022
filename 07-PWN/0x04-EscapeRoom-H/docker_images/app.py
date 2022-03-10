import os
import sys
import subprocess as sp

def main():
    black_list = ["cat", "'", ";", "&", "|", "head", "less", "wget", "nl", "tail", "strings", "*", "find", "-m"]

    while True:
        filename = str(input("monkey@monkey:/home/monkey$ file "))
        catch = [i in filename for i in black_list]
        if filename == "app.py":
            continue
        elif any(catch):
            print("Found a dangerous value in input, try again.")
            continue
        else:
            try:
                os.system("file " + filename)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        try:
            print()
            sys.exit(0)
        except SystemExit:
            print()
            os._exit(0)
