#include <stdio.h>

unsigned int v1 = 11;
char v2[100] =	"\0\0\0\0\0\0\0\0\0\0\0\2\2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0";
char v3 = 1;

void walk(unsigned char c);
void shift(unsigned char c);

int main(void) {
	puts("Hello hello! What is my v3?");

	while (v2[v1] == 2 && v1 < 100 && !(v3 & 0x40)) {
		unsigned char in = getchar();
		if (in == '\n') {
			continue;
		}
		walk(in);
		shift(in);
	}

	if (v2[v1] != 3 || v3 != 0x20) {
		puts("Maze Failed. Wrong Flag.");
	} else {
		puts("Maze Success! You got the Flag!");
	}
}

void shift(unsigned char c) {
	char t = v3 == 0x1F ? 3 : 2;
		
	switch(c) {
		case 'A':
			v2[v1 + 10] = t;
			break;
		case 'B':
			v2[v1 + 10] = v3 & 1 ? 0 : t;
			break;
		case '1':
			v2[v1 + 1] = v3 & 1 ? 0 : t;
			break;
		case '2':
			if (v3 & 1) {
				v2[v1 + 10] = t;
			} else {
				v2[v1 - 1] = t;
			}
			break;
		case 'F':
			if (v3 & 1) {
				v2[v1 - 10] = t;
			} else {
				v2[v1 + 10] = t;
			}
			break;
		default:
			v2[v1 - 1] = t;
			break;
	}
}

void walk(unsigned char c) {
	v2[v1] = 0;
	switch (c) {
		case 'A':
			v3 ^= 0x1;
			v1 += 1;
			break;
		case 'B':
			v3 ^= 0x4;
			v1 += 10;
			break;
		case '1':
			v3 += 0x2;
			v1 += 10;
			break;
		case '2':
			v3 ^= 0x8;
			v1 += 10;
			break;
		case 'F':
			v3 ^= 0x10;
			v1 += 10;
			break;
		case 'C':
			v3 += 0x1;
			v1 -=10;
			break;
		default:
			v3 |= 0x40;
			v1 += c & 0x3;
			break;
	}
}
