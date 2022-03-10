import random 
def main():
	operators = ["+","-","*"]
	for i in range(100):
		sendValues = [random.randint(1,100),operators[random.randint(0,2)],random.randint(1,100),operators[random.randint(0,2)],random.randint(1,100),operators[random.randint(0,2)],random.randint(1,100)]
		#sendValues = " ".join([str(x) for x in sendValues])
		sendStr = ""
		for x in sendValues:
			if x == "*" or x =="+" or x=="-":
				x *= random.randint(3,20)
			sendStr += " "+(str(x))
		print(sendStr)
		try:
			inputAnswer = int(input())
		except:
			print("NUMBERZ ONLY PLZ")
			return 0
		ourAnswer = calculate(sendValues)
		if(inputAnswer != ourAnswer):
			print("FAILURE, POLICE ARE ON ROUTE!!!")
			return 0

	print("Welcome back mr managere, monkeyCTF{string_parsing}")


def calculate(test):
	print(test)
	strBuilder = " ".join([str(x) for x in test])
	sumTotal = eval(strBuilder)
			
	return sumTotal

main()