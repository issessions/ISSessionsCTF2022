from numpy import random

for x in range(0,1000):
	a = random.randint(100000000)
	b = random.randint(100000000)
	c = random.randint(100000000)


	smallest = 0

	if a < b and a < c:
		smallest = a
	elif b < c:
		smallest = b
	else:
		smallest = c
	print("Which is lowest?:", a, b, "or",c,"?")    
	answer = input()
	if(int(answer)!=smallest):
		print("wrong")
		quit()

print("monkeyCTF{Nice_Connecting_Work}")
quit()