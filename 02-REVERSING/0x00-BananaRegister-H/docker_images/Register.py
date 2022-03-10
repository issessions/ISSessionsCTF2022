from rich.console import Console

console = Console()

## A class representing a banana register
class Register:
    def __init__(self) -> None:
        self.banana = 50
        self.unlocked = False

    ## Method used to verify password
    def _verify_password(self) -> bool:
        try:
            print("\nEnter password here:")
            user_input = list(str(console.input(":arrow_right_hook: ")).lower())
            a = [124, 123, 135, 136, 116, 128, 128, 137, 116, 121, 123, 123, 120, 111, 117, 124, 123, 111, 113, 125, 111, 110, 106, 115]
            ## Shift by index
            for i in range(len(user_input)):
                user_input[i] = ord(user_input[i]) + i
            ## Reverse and compare
            if user_input[::-1] == a:
                self.unlocked = True
                return True
            return False
        except:
            return False

    def deposit(self) -> None:
        try:
            ## Verifies password
            if self._verify_password():
                print("\nEnter amount to be deposited:")
                amount = int(console.input(":arrow_right_hook: "))
                self.banana += amount
                console.print(":arrow_right_hook: " + str(amount) + " bananas deposited successfully :white_check_mark: .\n")
            else:
                console.print("\n:x: Incorrect password.")
        except:
            console.print("\n:x: Deposit unsuccessful.")
            return False

    def withdraw(self) -> None:
        try:
            ## Verifies password
            if self._verify_password():
                print("\nEnter amount to be withdrawn:")
                amount = int(console.input(":arrow_right_hook: "))
                ## Check if there's enough bananas
                if self.banana >= amount:
                    self.banana -= amount
                    console.print(":arrow_right_hook: " + str(amount) + " bananas withdrawn successfully :white_check_mark: .\n")
                else:
                    console.print("\n:x: There is not enough bananas in the register.")
            else:
                console.print("\n:x: Incorrect password.")
        except:
            console.print("\n:x: Withdraw unsuccessful.")
            return False

    ## Shows flag if the password was entered
    def flag(self) -> None:
        if self.unlocked:
            console.print("\n:arrow_right_hook: monkeyCTF{5h1ft1ng_15_t00_w3ak}\n")
        else:
            console.print("\n:x: Nothing to see here.")

    def display(self) -> None:
        ## Verifies password
        if self._verify_password():
            console.print(":arrow_right_hook: Balance: " + str(self.banana) + " bananas" if self.banana > 0 else " banana" + " in the register.\n")
        else:
            console.print("\n:x: Incorrect password.")

def main():
    console.print(":banana: :banana: :banana: :banana: :banana: :banana: :banana: :banana: :banana:")
    console.print(":banana:    Banana Register   :banana:", style="bold white")
    console.print(":banana: :banana: :banana: :banana: :banana: :banana: :banana: :banana: :banana:")
    console.print("\nHere are some things you can do:", style="underline")
    console.print("\n(A) Deposit\n(B) Withdraw\n(C) Display\n(X) Exit\n")
    print("Enter your choice:")
    choice = str(console.input(":arrow_right_hook: "))
    ## Create instance
    account = Register()
    ## Loop until terminated
    while True:
        ## User wants to deposit
        if choice in "aA":
            account.deposit()
        ## User wants to withdraw
        elif choice in "bB":
            account.withdraw()
        ## User wants to display balance
        elif choice in "cC":
            account.display()
        ## User wants to display flag
        elif choice in "fF":
            account.flag()
        ## User wants to terminate program
        elif choice in "xX":
            exit()
        ## Display menu and take input
        console.print("\nHere are some things you can do:", style="underline")
        print("\n(A) Deposit\n(B) Withdraw\n(C) Display\n(X) Exit\n")
        print("Enter your choice:")
        choice = str(console.input(":arrow_right_hook: "))
    

if __name__ == "__main__":
    main()
