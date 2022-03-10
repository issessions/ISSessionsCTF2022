#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void func5(char* input);


int main(int argc, char* argv[]){
	
	char comparison[] ="maomlYyBU:{KpckrTWaqjYrSiUnHu=s";
	func5(comparison);
	printf("After calculations the flag is %s", comparison);

	return 0;
}

void func5(char* input){
	char copy[31];
	strcpy(copy,input);
	for(int i =1;i<32;i++){
		int bananananana= (i%4<<3)^2>>4<<2>>1^4; //holy @$#% thats a lot of operations!	
		switch(bananananana){
			case 0x04:
				input[i-1]= copy[i]-4/bananananana;
				printf("at i of %d the input was made into %c\n", i, input[i]);
				break;
			case 0x0C:
				input[i-1]= copy[i]+(bananananana);
				printf("at i of %d the input was made into %c\n", i, input[i]);
				break;
			case 0x14:
				input[i-1]= copy[i]*(0x14/bananananana);
				printf("at i of %d the input was made into %c\n", i, input[i]);
				break;
			case 0x1C:
				input[i-1]= copy[i]+0x01;
				printf("at i of %d the input was made into %c\n", i, input[i]);
				break;
			default:
				//it would be funny if we didnt change some of the letters in the flag to trick them
				input[i] = input[i];
				break;
		}
		printf("banananana is currently %d\n", bananananana);
	}
}





//monkeyCTF{LooksScarierThanItIs}