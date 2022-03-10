#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
#define _GNU_SOURCE

#define HISTSIZE 10000

int history[HISTSIZE];
int hist_size = 0;
int euid = 0;
int ruid = 0;

void sighndlr() {
    signal(SIGTSTP, SIG_IGN);
    FILE* fptr = fopen("/root/flag.txt", "r"); // only root should be able to open
    if (fptr != NULL) {
        char s[100];
        fgets(s, 100, fptr);
        fclose(fptr);
        printf(s);
    }
    exit(1);
}
void sighdnlr2(){
    signal(SIGFPE, SIG_IGN);
    seteuid(euid);
    printf("FPE! Logging and Resetting History...\n");
    int max = hist_size;
    hist_size = 0;
    for(int i = 0; i < max; i++){
            history[i] = 0;
            for (int j = 0; j < 100000; j++) {
                history[i] += j;
            }
    }
    seteuid(ruid);
    printf("Exiting...\n");
    exit(1);
}

void add_hist(double res) {
        if (hist_size < HISTSIZE) {
                history[hist_size] = res;
                hist_size++;
        }
}

int main(void) {
    // Run as real user
    euid = geteuid();
    ruid = getuid();
    seteuid(ruid);

    signal(SIGTSTP, sighndlr);
    signal(SIGFPE, sighdnlr2);

    printf("Welcome to the monkey calculating simlacrum! I don't even know what that means!\n");
    int res = 0;
    char c = 'a';
    char input[64];
    while (c != 'e') {
            printf("What would you like to do? (h for help)\n");
            fgets(input, 64, stdin);
            c = input[0];
            switch(c) {
                case 'p':
                    printf("Can I have a number?\n");
                    fgets(input, 64, stdin);
                    res = 100 + atoi(input) - 1;
                    printf("That's not my favourite number!\n");
                    add_hist(res);
                    printf("100 + %d - 1 = %d\n", atoi(input), res);
                    break;
                case 'l':
                    printf("Can I have a number?\n");
                    fgets(input, 64, stdin);
                    res = 100 - atoi(input) - 1;
                    printf("That's my favourite number!\n");
                    add_hist(res);
                    printf("100 - %d - 1 = %d\n", atoi(input), res);
                    break;
                case 'n':
                    printf("Can I have a number?\n");
                    fgets(input, 64, stdin);
                    res = 100 * (atoi(input) - 1);
                    printf("Wow, that's a number!\n");
                    add_hist(res);
                    printf("100 * (%d - 1) = %d\n", atoi(input), res);
                    break;
                case 'a':
                    printf("Can i have a number?\n");
                    fgets(input,64,stdin);
                    res = 100 / (atoi(input) - 1);
                    printf("Nice, that's my favourite number!\n");
                    add_hist(res);
                    printf("100 / (%d - 1) = %d\n", atoi(input), res);
                    break;
                case 'e':
                    break;
                default:
                    printf("p - add\nl - subtract\nn - multiply\na - divide\ne - exit\n");
            }
    }
}