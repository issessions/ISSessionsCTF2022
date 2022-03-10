

split = test.split(" ")
sumTotal = int(split[0])
for x in range (1,len(split)-1,2):
	print(split[x])
	operator = split[x]
	number = int(split[x+1])
	if(operator =='+'):
		sumTotal+= number
	else:
		sumTotal -=number

print(sumTotal)





