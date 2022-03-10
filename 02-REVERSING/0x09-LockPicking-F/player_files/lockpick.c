#include <stdio.h>
#include <ctype.h>
#include <stdint.h>

uint32_t pick = 0;
char success[] = "Congrats! You opened the lock! Go on and claim your treasure!";
char fail[] = "Aww, looks like you didn't get the lock this time...";

char fiddle(char c);

int main(void) {
	char c = 0;
	char n = 0;
	char* msg = fail;

	printf("%s", "Hmmm, a tricky lock we got here, can we pick it? End lockpicking with 'E'\n");

	do {
		c = getchar();
		n = getchar();
		if (isprint(n)) ungetc(n, stdin);
		else if (n != '\n') while (getchar() != '\n');
		c = fiddle(c);
	} while (c != 'E');
	
	int flag = 1;
	for (int i = 0; i < 32; i++) {
		flag &= pick & 1;
		pick >>= 1;
	}


	if (flag) {
		msg = success;
	}

	printf("%s\n", msg);
}

char fiddle(char c) {
	if (c == 'E') {
		return c;
	}
	switch(c) {
		case '1':
			pick -= 138841;
			break;
		case '2':
			pick += 5;
			break;
		case '3':
			pick += 11;
			break;
		case '4':
			pick += 61;
			break;
		case '5':
			pick *= 3;
			break;
		case '6':
			pick *= 7;
			break;
		case '7':
			pick *= 11;
			break;
		case '8':
			pick *= 53;
			break;
		default:
			pick = 0;
	}
	return c;
}
