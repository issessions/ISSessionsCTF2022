import random

def main():
	print("Some of the numbers are missing, can you figure out which?")
	print("The lowest and highest will always be in the string")
	print("If 2,5 and 6 are missing, return them in the form:2 5 6")

	for x in range(500):
		lower = random.randint(0,100)
		higher = random.randint(lower+10,lower+40)
		amount = higher-lower+1
		sendString = []
		for x in range(lower,higher):
			sendString.append(str(x)) 
		random.shuffle(sendString)
		numMissing = random.randint(2,10)
		numReplaced = 0
		replacedNums = []
		while(numReplaced < numMissing):
			cur = random.randint(0,amount-2)
			if(sendString[cur]!='*' and sendString[cur]!=str(lower) and sendString[cur]!=str(higher)):
				replacedNums.append(sendString[cur])
				sendString[cur] = '*'
				numReplaced+=1
		print(sendString)
		response = input()
		splitResponse = response.split(" ")
		matched = 0
		for x in splitResponse:
			if x in replacedNums:
				matched+=1
		if(matched!=numMissing):
			print("FAILURE")
			return 0
	print("monkeyCTF{alot_of_rules_huh}")


main()
