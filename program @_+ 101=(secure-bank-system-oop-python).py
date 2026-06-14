class Bank:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
        print(f"Successfully deposited {amount} BDT. New Balance: {self.__balance} BDT")
    def show_balance(self,pin):
        if pin == 54321:
            print(f"[Correct pin] Current balance is {self.__balance} BDT")
        else:
            print(f"[Incorrect pin] can't find that pin")
def main():
    while True:
        s_s = input("Enter Start Or Stop:").lower()
        if s_s == "start":
            print("\n --- Testing Start ---")
        elif s_s == "stop":
            print("Quitting the program here:")
            break
        else:
            print("Please enter either 'start' or 'stop'")
            continue

        try:
            deposit = int(input("Enter your deposit amount: "))
            bank = Bank(deposit)

            pin_input = int(input("enter your pin here:"))
            bank.show_balance(pin_input)

            print("\n --- Testing Security ---")
            print(bank.__balance)
        except AttributeError:
            print(f"AttributeError:[Security Alert]:You can't access the balance directly")
        except ValueError:
            print("IntegerError:[Security Alert]:You cannot Enter The 'String' You can enter only 'Integer'")


if __name__ == "__main__":
    main()
