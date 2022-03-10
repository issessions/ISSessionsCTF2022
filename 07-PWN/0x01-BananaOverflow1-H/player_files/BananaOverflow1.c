#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void you_better_not_hack_me_and_take_my_banana()
{
  char flag[0x100] = {0};
  FILE *fp = fopen("./flag.txt", "r");
  if (!fp)
  {
    puts("you need to run this on the server, use the netcat");
    exit(-1);
  }
  fgets(flag, 0xff, fp);
  puts(flag);
  fclose(fp);
}

int main(void)
{
  char plz_dont_jump[32];
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  setbuf(stderr, NULL);

  puts("If my banana bucket can only hold 32 banana's, what happens if i try to put in 33?");

  gets(plz_dont_jump);
  if(1==2){
  you_better_not_hack_me_and_take_my_banana();
  }
}