#include <stdio.h>

char v1[] = "\0\0\0\0\0\0\0\0\0\0";
int v2 = 7;
int v3 = 22;
char v4[] =	"\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\2\1\2\1\1\1\1\1\1\1\1\3\1\1\1\1\1\1\1\1\1\2\2\2\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1\1";

void command(int i);

int main(void) {
	puts("Hello hello! What is my flag?");
	fgets(v1, 10, stdin);
	if (v1[7] != '\n' && v1[7] != '\0' && v1[7] != '\r')v2 = 0;

	int i = 0;
	while(i < v2 && v4[v3] != 1) {
		command(i);
		i++;
	}

	if (v4[v3] != 3) {
		puts("Maze Failed. Wrong Flag.");
	} else {
		puts("Maze Success! You got the Flag!");
	}
}

void command(int i) {
	switch (v1[i]) {
		case '0':
			v3 -= 10;
			break;
		case '1':
			v3 += 10;
			break;
		case '2':
			v3 -= 1;
			break;
		case '3':
			v3 += 1;
			break;
		case 'A':
			v3 -= 20;
			break;
		case 'B':
			v3 += 20;
			break;
		case 'C':
			v3 -= 2;
			break;
		case 'D':
			v3 += 2;
			break;
		default:
			v3 = 0;
	}
}
