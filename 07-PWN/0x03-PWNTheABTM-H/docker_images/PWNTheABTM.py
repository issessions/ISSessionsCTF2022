balance = 5
import os

def main():
    print("Hello customer! Please select an ABTM option.")
    print("Deposit(D)")
    print("Withdraw(W)")
    print("Check Balance(C)")
    print("Transfer to another customer(T)")
    print("Exit(E)")
    value = input("To select an option, enter the letter shown in brackets: ")
    if(len(value)==1):
        value = value+ "()"
    exec(value)

def D():
    global balance
    value = input("How many banana would you like to deposit: ")
    if (int(value) > 100):
        secondValue = input("Do you really have that much? tell the truth(Y/N): ")
        if(secondValue == "Y"):
            print("OK, banana has been deposited.")
            balance = balance + int(value)
        else:
            print("Thank you for not lying, but unfortunately your account has been closed.")
            quit()
    else:
        print("Banana deposited")
        balance = balance+int(value)
        print("\n")
        main()
def W():
    global balance
    value = input("How many banana would you like to withdraw: ")
    if int(value) > balance:
        secondValue= input("Your request is higher than your current balance. Would you like a loan?(Y/N): ")
        if(secondValue == "Y"):
            print("Loan has been approved. Interest rate is 50% a day with 5 years minimum repay. Bye.")
            balance = balance-int(value)
        else:
            print("Ok, we didn't want to give you a loan anyway")
    print("\n")
    main()
def C():
    global balance
    print(balance)
    print("\n")
    main()

def T():
    global balance
    name = input("Please enter the IP Address of the customer you wish to transfer money to: ")
    amount = input("Please enter the amount you wish to transfer: ")
    print("Money has been transferred")
    balance = balance-amount
    print("\n")
    main()

def E():
    print("Thanks, have a nice day!")
    quit()

main()