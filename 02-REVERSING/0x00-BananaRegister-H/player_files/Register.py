from rich.console import Console

console = Console()

class Register:
    def __init__(self) -> None:
        self.banana = 50
        self.unlocked = False

    def _verify_password(self) -> bool:
        try:
            print("\nEnter password here:")
            user_input = list(str(console.input(":arrow_right_hook: ")).lower())
            a = [124, 123, 135, 136, 116, 128, 128, 137, 116, 121, 123, 123, 120, 111, 117, 124, 123, 111, 113, 125, 111, 110, 106, 115]
            for i in range(len(user_input)):
                user_input[i] = ord(user_input[i]) + i
            if user_input[::-1] == a:
                self.unlocked = True
                return True
            return False
        except:
            return False

    def deposit(self) -> None:
        try:
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
            if self._verify_password():
                print("\nEnter amount to be withdrawn:")
                amount = int(console.input(":arrow_right_hook: "))
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

    def flag(self) -> None:
        if self.unlocked:
            console.print("\n:x: REDACTED :x:")
        else:
            console.print("\n:x: Nothing to see here.")

    def display(self) -> None:
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
    account = Register()
    while True:
        if choice in "aA":
            account.deposit()
        elif choice in "bB":
            account.withdraw()
        elif choice in "cC":
            account.display()
        elif choice in "fF":
            account.flag()
        elif choice in "xX":
            exit()
        console.print("\nHere are some things you can do:", style="underline")
        print("\n(A) Deposit\n(B) Withdraw\n(C) Display\n(X) Exit\n")
        print("Enter your choice:")
        choice = str(console.input(":arrow_right_hook: "))
    

if __name__ == "__main__":
    main()
