#include <stdio.h>
#include <stdlib.h>
int main()
{
    setbuf(stdout, NULL);
    int con;
    con = 0;
    int account_balance = 1000;
    while(con == 0){
        
        printf("Welcome to the Banana market!\n");
        printf("We sell Bananas\n");

        printf("\n1. Check Account Balance\n");
        printf("\n2. Buy Bananas\n");
        printf("\n3. Exit\n");
        int menu;
        printf("\n Enter a menu selection\n");
        fflush(stdin);
        scanf("%d", &menu);
        if(menu == 1){
            printf("\n\n\n Balance: %d \n\n\n", account_balance);
        }
        else if(menu == 2){
            printf("Currently for sale\n");
            
            printf("1. Red Banana\n");
            printf("2. Yellow Banana\n");
            printf("3. Orange Banana\n");
            printf("4. THE Banana\n");
            int auction_choice;
            fflush(stdin);
            scanf("%d", &auction_choice);
            if(auction_choice == 1){
                printf("These Red Bananas cost 900 each, we only have 1000 left\n");
                unsigned long long number_Bananas = 0;
                fflush(stdin);
                scanf("%llu", &number_Bananas);
                
                if(number_Bananas > 0 && number_Bananas < 1000){
                    int total_cost = 0;
                    total_cost = 900*number_Bananas;
                    printf("\nThe final cost is: %d\n", total_cost);
                    if(total_cost <= account_balance){
                        account_balance = account_balance - total_cost;
                        printf("\nYour current balance after transaction: %d\n\n", account_balance);
                    }
                    else{
                        printf("Not enough funds to complete purchase\n");
                    }
                                    
                    
                } else {
                    printf("Sorry, we only have 1000 left\n");
                }    
            }
            if(auction_choice == 2){
                printf("These Yellow Bananas cost 500 each, we only have 500 left\n");
                unsigned long long number_Bananas = 0;
                fflush(stdin);
                scanf("%llu", &number_Bananas);
                
                if(number_Bananas > 0 && number_Bananas < 500){
                    int total_cost = 0;
                    total_cost = 900*number_Bananas;
                    printf("\nThe final cost is: %d\n", total_cost);
                    if(total_cost <= account_balance){
                        account_balance = account_balance - total_cost;
                        printf("\nYour current balance after transaction: %d\n\n", account_balance);
                    }
                    else{
                        printf("Not enough funds to complete purchase\n");
                    }
                                       
                } else{
                    printf("Sorry, we only have 500 left\n");
                }    
            }
            if(auction_choice == 3){
                printf("These Orange Bananas cost 500 each, we can order more so just buy as many as you want\n");
                unsigned long long number_Bananas = 0;
                fflush(stdin);
                scanf("%llu", &number_Bananas);
                
                if(number_Bananas > 0){
                    int total_cost = 0;
                    total_cost = 900*number_Bananas;
                    printf("\nThe final cost is: %d\n", total_cost);
                    if(total_cost <= account_balance){
                        account_balance = account_balance - total_cost;
                        printf("\nYour current balance after transaction: %d\n\n", account_balance);
                    }
                    else{
                        printf("Not enough funds to complete purchase\n");
                    }
                                    
                    
                }    
            }

            else if(auction_choice == 4){
                printf("THE Banana costs 2000 dollars, and we only have 1 in stock\n");
                printf("Enter 1 to buy one");
                int bid = 0;
                fflush(stdin);
                scanf("%d", &bid);
                
                if(bid == 1){
                    
                    if(account_balance > 2000){
                        FILE *f = fopen("flag.txt", "r");
                        if(f == NULL){

                            printf("flag not found: please run this on the server\n");
                            exit(0);
                        }
                        char buf[64];
                        fgets(buf, 63, f);
                        printf("YOUR FLAG IS: %s\n", buf);
                        }
                    
                    else{
                        printf("\nNot enough funds for transaction\n\n\n");
                    }}

            }
        }
        else{
            con = 1;
        }

    }
    return 0;
}