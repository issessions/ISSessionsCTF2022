#include <stdio.h>
#include <string.h>
#include <stdlib.h>
const char *colours[3]= {"Red", "Blue", "Green"};
int main(void)
{       


        
        puts("Thanks for joining the team at banana bucket filler incorporated!\n");
        puts("We have three different coloured bananas, when you come across one you will have to do a task to put it in the bucket.\n");
        puts("Why can't you just drop it in the bucket? Cuz we're trying to help you build character. Get to work!!!");
        
        int rArray[14] = {0,2,0,0,2,2,2,0,2,1,1,2,1,2};
        int r = 0;
        while(1){

                printf("%s banana!\n", colours[rArray[r]]);
                if(rArray[r] == 0){
                        int ans = Numbers(rArray[r]);      
                }
                else if(rArray[r]== 1){
                        
                        int ans = ColoursFunc(rArray[r]);
                }
                else{ //AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA
                        int ans = Third(rArray[r]);
                }
                r++;
        } 
}

void shhhhhbin(){
        execve("/bin/sh", NULL, NULL);
}

int ColoursFunc(int f){
        char answer[10];
        printf("This one is easy, what colour banana are you trying to put in?\n");
        fflush(stdin);
        fgets(answer,100,stdin);
        //answer[strcspn(answer, "\n")] = 0;

        if(strcmp(answer,colours[f])!=0){
                int i = 5;
        }
}

int Numbers(int f){
       

                int x = rand()%10 +1;
                int y = rand()%11 + 2;
                char answer[10];
                        printf("what is %d + %d\n", x,y);
                        fgets(answer,10,stdin);
                        int iAnswer = atoi(answer);             
                        if (iAnswer!=(x+y)){
                        puts("You can't do math! You're FIRED!!!!");
                        exit(1);
                } 
}

int Third(int f){
       char answer[20];
                        printf("You either know it or you don't\n");
                        fgets(answer,20,stdin);
                        answer[strcspn(answer, "\n")] = 0;
                        if(strcmp(answer,"123456789abcdefghi")!=0){
                                puts("I guess you don't know it huh");
                                exit(1);
                        } 
}