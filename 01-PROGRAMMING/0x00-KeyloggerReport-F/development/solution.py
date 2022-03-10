#!/usr/bin/python3

# Temporarily store keystrokes
keystrokes = []

with open ("log.txt", "r") as logs:
    for line in logs:

        if "Key.shift_r" in line:
            continue

        # Print line since end of line
        if "Key.enter" in line:
            # Skip events that ENTER button is randomly 
            if len(keystrokes) == 0:
                continue

            print("".join(keystrokes))

            # Clear out list
            keystrokes.clear()
            
        elif "Key.space" in line:
            keystrokes.append(" ")

        elif "Key.backspace" in line:
            if len(keystrokes) == 0:
                continue
            else:
                # Remove backspace by popping list
                keystrokes.pop()
        
        else:
            field = 3
            fields = line.split(" ")
            word = fields[field].strip()
            keystrokes.append(chr(int(word)))