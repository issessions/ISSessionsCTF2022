#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void func1(char* input);
void func2(char* input);
void func3(char* input);
void func4(char* input);
void func5(char* input);


int main(int argc, char* argv[]){
	char filename[] = "flag.txt";
	char userinput[31];
	printf("Put something in!\n");
	fgets(userinput,31,stdin);
	func1(userinput);
	func2(userinput);
	func3(userinput);
	func4(userinput);
	func5(userinput);
	char comparison[] ="maomlYyBU:{KpckrTWaqjYrSiUnHu=s";

	for(int i=0; i<31;i++){
		if(comparison[i]!=userinput[i]){
			//printf("The final flag is %s", userinput);
			exit(1);
		}
	}
	printf("Congrats! If you made it here you know the flag!");
	//printf("After calculations the flag is %s", userinput);
	return 0;
}

void func1(char* input){
	for(int i=0; i<31;i++){
		input[i] = input[i]+3;
	}
	
}

void func2(char* input){
	
	for(int i =0;i<31;i++){
		
		input[i] = input[i]-5;
	}
	
	
}

void func3(char* input){
	
	for(int i =0;i<31;i++){
		input[i] = input[i]-8;
	}
	

}
void func4(char* input){
	
	for(int i =0;i<31;i++){
		input[i] = input[i]+10;
	}
	
}

void func5(char* input){
	char copy[31];
	strcpy(copy,input);
	for(int i =1;i<31;i++){
		int bananananana= (i%4<<3)^2>>4<<2>>1^4; //wow thats a lot of operations!	
		switch(bananananana){
			case 0x02:
				input[i] = input[i-1]%31+44;
				break;
			case 0x04:
				input[i]= copy[i-1]+4/bananananana;
				break;
			case 0x0C:
				input[i]= copy[i-1]-(bananananana);	
				break;
			case 0x14:
				input[i]= copy[i-1]*(0x14/bananananana);
				break;
			case 0x1C:
				input[i]= copy[i-1]-0x01;
				break;
			case 0x2B:
				input[i] = input[i-1] % 44;
				break;
			case 0x3C:
				input[i] = (input[i] + 22) % 43 % 21;
				break;
			default:
				//it would be funny if we didnt change some of the letters in the flag to trick them hehe
				input[i] = input[i];
				break;
		}
	}
}
