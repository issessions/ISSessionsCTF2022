import random
import string

d = ["@gmail.com", "@yahoo.ca", "@hotmail.com", "@outlook.com", "@icloud.com", "@msn.com", "@ymail.com", "@live.com"]

for i in range(0,100):
	username = string.ascii_lowercase
	username = ''.join(random.choice(username) for j in range(random.randint(5, 10))) 
	print(username + d[random.randint(0, 7)])


