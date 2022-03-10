#How to play:
#Between 3-7 (inclusive) will be generated on a grid that ranges from 6-9 tiles on the X/Y axis.
#The user is to input a string that has the ships coordinates.
#The string should be comma seperated (no spaces).
#The coordinates start at the Y axis as first number, followed by a colon, followed by the X axis.
#An example is shown below:
#🌊🌊🏴‍
#🌊🏴‍🌊
#🌊🌊🌊
#The correct answer/string for this would be 1:3,2:2
#The string does not need to be in any particular order.
#If an incorrect coordinate is hit or any pirate ships remains, the user will fail
#the challenge and must start over.

#Libraries
from random import randint
from time import sleep
from datetime import datetime
import time
import threading

#===========================================
#Create the grid the user will see/play with
#===========================================
def GenerateGrid():
    #Declare Variables
    gridArray=[]
    answer=[]
    sendString=""
    waveEmoji="\U0001F30A"
    pirateEmoji="\U0001F3F4"

    #Generate Grid Variables
    gridSize=randint(6,9)
    shipCount=randint(3,7)

    #Generate Grid
    rowArray=[]
    for x in range(gridSize):
        for y in range(gridSize):
            rowArray.append(waveEmoji)
        gridArray.append(rowArray)
        rowArray=[]
    
    #Generate and Insert Answer/Ship spaces
    for count in range(1, shipCount+1):
        #Continue looping if a ship space is already taken
        checker=True
        while checker:
            #Generate ship space
            shipX=randint(1,gridSize)
            shipY=randint(1,gridSize)
            tempAnswer=str(shipX)+":"+str(shipY)
            #If true, re-generate answer
            if tempAnswer in answer:
                pass
            #If false, move to next answer and insert pirate emoji
            else:
                checker=False
                answer.append(tempAnswer)
                gridArray[shipX-1][shipY-1]=pirateEmoji

    #Setting up the print string of the grid
    for x in range(gridSize):
        for y in range(gridSize):
            sendString+=gridArray[x][y]+"  "
        sendString+="\n\n"

    return sendString, answer



#===========================================
#Await for user input and validate it
#===========================================
def CheckInput(answer, userInput):
    #Declare variables
    failure=0
    
    #Process user input
    userInput=userInput.split(',')
    inputCopy = userInput.copy()

    #Test every element in user input
    #If an incorrect position is chosen, the user will fail
    #If all elements are correct, the user will pass this test
    for element in inputCopy:
        if element in answer:
            userInput.remove(element)
            answer.remove(element)
        else:
            failure=1

    #After the test case, both answer and userInput should be empty
    #If at least on element remains in either array, the user will fail
    if answer or userInput:
        failure=1

    #Failure should equal zero for the user to pass
    if not failure:
        return 1
    else:
        return 0



#===========================================
#Output the flag to the user
#===========================================
def PrintFlag():
    flag = "monkeyCTF{l00k_4t_m3_1_4m_th3_c4pt41n_n0w!!!}"
    return flag

#Main
def main():
    keepAlive=1
    forceQuit=0
    waveEmoji="\U0001F30A"
    pirateEmoji="\U0001F3F4"
        
    #Instruction loop
    loopTrue=1
    while loopTrue:
        print("\nWelcome to Pirate Attack! Choose your option.\n1 - Instructions\n2 - Play Game\n0 - Exit")
        userInput=input()
        #Instructions
        if userInput == "1":
            print("===HOW TO PLAY===")
            print("A grid will be generated showing different emojis.")
            print(f"Within the grid, there will be either a {waveEmoji} or {pirateEmoji}.")
            print(f"The {waveEmoji} will represent an empty space, while {pirateEmoji} are your targets.")
            print("As supplies are extrodinary limited, you cannot afford to miss any targets.")
            print("In addition to that, missing a valid target will result in an automatic loss.")
            print("You are also on a strict timer. Take too long, and you will lose!")
            print("Your job is to survive as many consecutive waves as possible without losing.\n")
            print("In order to send a valid attack string, you must do the following:")
            print("1. All coordinates will be written as Y:X. Y and X are to be replaced with the row/column number.")
            print("2. To seperate each coordinate, you must use a comma, no spaces.")
            print("3. The order does not matter.")
            print("For example, with the grid below:")
            print(f"{waveEmoji}{waveEmoji}{pirateEmoji}")
            print(f"{waveEmoji}{pirateEmoji}{waveEmoji}")
            print(f"{waveEmoji}{waveEmoji}{waveEmoji}")
            print("The correct answer would be either 1:3,2:2 or 2:2,1:3.")
            print("===NOTE===\nDepending on the terminal you're using, the emojis may appear as text. Note that this should not change the functionality, just appearence.")
        #Play Game
        elif userInput == "2":
            loopTrue = 0
        #Exit
        elif userInput == "0":
            print("Goodbye!")
            loopTrue = 0
            keepAlive = 0
            forceQuit = 1
        #Invalid choice
        else:
            print("Not a valid option. Please choose a valid option.")

    #Game loop
    while keepAlive:
        #Declare important variables
        userPassRequirement=100
        isUserPlaying=1
        successCount=0
        timeLimitInSeconds=20

        #Loop the game until an end condition is met
        while isUserPlaying:
            #If the user meets the success count, terminate game and reward
            if successCount >= userPassRequirement:
                isUserPlaying = 0
                keepAlive = 0
                print("Congratulations, you won! Here's your reward, captain.")
                print(PrintFlag())
            #If user has not met success count, play the game again
            else:
                print("\nA new wave of pirates approaches!")
                generated = GenerateGrid()
                print(generated[0])

                #Takes user input and times it. If exceeds timeEnd-timeStart, user loses.
                timeStart=datetime.today()
                userInput=input()
                timeEnd=datetime.today()

                #Check if user's time is valid
                if (timeEnd.timestamp()-timeStart.timestamp() <= timeLimitInSeconds):
                    isUserPlaying = CheckInput(generated[1],userInput)
                else:
                    isUserPlaying = 0
                    keepAlive = 0
                    print("Time exceeded!")

                #If the user passes, increase success counter
                if isUserPlaying:
                    successCount+=1
                    print(f"Correct! Current number of waves survived: {successCount}")

        #Lose condition
        if (successCount < userPassRequirement) and not forceQuit:
                print("You Lost.")
                keepAlive=0

if __name__ == "__main__":
    main()