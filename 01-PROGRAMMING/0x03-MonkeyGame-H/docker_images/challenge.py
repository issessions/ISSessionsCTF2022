import random 
def main():
	operators = ["+","-"]
	for i in range(100):
		sendValues = [random.randint(1,100),operators[random.randint(0,1)],random.randint(1,100),operators[random.randint(0,1)],random.randint(1,100),operators[random.randint(0,1)],random.randint(1,100)]
		sendValues = " ".join([str(x) for x in sendValues])
		print(sendValues)
		try:
			inputAnswer = int(input())
		except:
			print("NUMBERZ ONLY PLZ")
			return 0
		ourAnswer = calculate(sendValues)
		if(inputAnswer != ourAnswer):
			print("Better luck next time, scrub")
			return 0

	print("You win, here's your prize! monkeyCTF{string_parsing}")


def calculate(test):
	split = test.split(" ")
	sumTotal = int(split[0])
	for x in range (1,len(split)-1,2):
		operator = split[x]
		number = int(split[x+1])
		if(operator =='+'):
			sumTotal+= number
		else:
			sumTotal -=number
	return sumTotal

main()