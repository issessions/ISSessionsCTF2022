import base64

def main():
	flag = ''
	with open('flag.txt', 'r') as file:
		flag = file.read()
	flag = bytes(flag.encode('ASCII'))
	flag = doa(flag)
	flag = dob(flag)
	flag = base64.b64encode(flag)
	with open('flag.txt', 'w') as file:
		file.write(flag.decode('ASCII'))

def doa(b_flag):
	new_flag = bytes()
	for c in b_flag:
		n = c >> 7
		c = ((c & 0x7F) << 1) + n
		new_flag += c.to_bytes(1, 'big')
	return new_flag

def dob(b_flag):
	n = 16598287
	e = 827
	new_flag = bytes()
	while b_flag:
		ee = e
		value = int.from_bytes(b_flag[:3], 'big')
		b_flag = b_flag[3:]
		base = 1
		while ee > 0:
			if ee & 1:
				base = (base * value) % n
			value = (value * value) % n
			ee = ee >> 1
		new_flag += base.to_bytes(3, 'big')
	return new_flag

if __name__ == "__main__":
	main()