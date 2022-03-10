import socket

#Socket
addr = "challenges.issessions.ca"
port = 5106

waveUni = "\U0001F30A"
pirateUni = "\U0001f3f4"

#Establish connection and start game
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((addr, port))
data = clientsocket.recv(1024)
print(data)
clientsocket.send(bytes("2\n", "utf-8"))

#Play game
while True:
    #Receive wave
    data = clientsocket.recv(1024)
    
    #Remove spaces
    wave = (str(data, "utf-8")).replace(" ", "")
    print(wave)
    
    #Refresh values
    returnString = ""
    yCount = 1
    xCount = 1
    
    #Check string line by line
    for y in wave.splitlines():
        #Is it a valid wave?
        if waveUni not in y:
            pass
        #Check each pirate flag in the waves and increment by each character
        else:
            for x in y:
                if x == pirateUni:
                    returnString += str(yCount)+":"+str(xCount)+","
                xCount += 1
            yCount+=1
            xCount = 1
    
    #Send results
    print(returnString[:-1]+"\n")
    clientsocket.send(bytes(returnString[:-1]+"\n", "utf-8"))
            
exit(0)