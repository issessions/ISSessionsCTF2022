#How to play:
#View "Instructions" variable

#Libraries
from random import randint, choice
from time import sleep
from datetime import datetime
import time
import threading

def main():
    #Flag for the challenge
    flag = "monkeyCTF{cr3ppy_cr4wl3r5_sh411_n0t_p455}"
    
    #Unicode arrays for fruits and insects
    fruits = ["\U0001f34c", "\U0001f349", "\U0001f347", "\U0001f95c", "\U0001f34d", "\U0001f348", "\U0001f965", "\U0001f95d"]
    insects = ["\U0001f41c", "\U0001f577", "\U0001f997", "\U0001fab0", "\U0001f99f", "\U0001f41d", "\U0001fab2", "\U0001f41e"]
    
    #Timer allowed for response
    timeLimitInSeconds = 2.5
    #Number of insects to be crushed before flag is given
    insectCounter = 100
    
    instructions = f"""
Due to a number of insect-related cases involving produce, the monkeys have decided to hire you to create a system that is able to detect nasty critters during food sorting!

The following are valid fruits: {fruits[0]}, {fruits[1]}, {fruits[2]}, {fruits[3]}, {fruits[4]}, {fruits[5]}, {fruits[6]}, {fruits[7]}.
These are to be expected. You can safely ignore these without issue.

The following are critters: {insects[0]}, {insects[1]}, {insects[2]}, {insects[3]}, {insects[4]}, {insects[5]}, {insects[6]}, {insects[7]}.
Insects are a no-go! You are to stop the conveyer belt when they appear.
    
Each time the console prints either a fruit or insect, it will expect your input. You can stop the conveyer belt by simply entering "stop". Any other texts will be treated as "ignore".
Your job is to ignore all fruits and stop at all insects. Additionally, due to the number of fruits being processed, it must not take longer than {timeLimitInSeconds} to receive input, or you will automatically be fired!

If the fruits/inspects appear as text, it's likely because your terminal/console is not using Unicode. While it makes it harder to read, the challenge should still work the same!
"""
    
    #Start loop with player
    while True:
        print("Welcome to Pest Patrol! Choose an option: \n1 - Instructions\n2 - Start\n0 - Exit")
        userInput = input()
        #Instructions
        if str(userInput).strip() == "1":
            print(instructions)
           
        #Game
        elif str(userInput).strip() == "2":
        
            #Keep looping until insects is at 0
            while insectCounter != 0:
                #Spawns either fruit or insect
                spawn = randint(1,100)
                if spawn == 50:
                    print(choice(insects))
                else:
                    print(choice(fruits))
                    
                #Start timer
                timeStart=datetime.today()
                userInput=input()
                timeEnd=datetime.today()
                    
                #Check if user made correct decision
                if (timeEnd.timestamp()-timeStart.timestamp() <= timeLimitInSeconds):
                    if (str(userInput).strip()) == "stop" and (spawn == 50):
                        insectCounter -= 1
                    elif (str(userInput).strip()) != "stop" and (spawn != 50):
                        pass
                    else:
                        print("Mistakes were made. You're fired!")
                        exit(0)
                else:
                    print("Mistakes were made. You're fired!")
                    exit(0)
            
            #Give flag if player wins game
            print(f"Great work! Here's your reward: {flag}")
            exit(0)
            
        #Terminate game
        elif str(userInput).strip() == "0":
            print("Goodbye!")
            exit(0)
           
        #Loop input if invalid input
        else:
            print("Not a valid input!")

if __name__ == "__main__":
    main()