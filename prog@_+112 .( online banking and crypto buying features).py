
class Online_Banking:
    def __init__(self,user_name,balance):
        self.user_name = user_name
        self.balance = balance
    def withdraw(self,amount):
     self.balance -= amount
     return f"\n[Withdraw Success...]your {amount} BDT dispensed for {self.user_name}. Remaining: {self.balance} BDT."


    def deposit(self,amount):
      self.balance += amount
      return f"\n[Deposit Success...]your {amount} BDT dispensed for {self.user_name}. Remaining: {self.balance} BDT."


class SmartCrypto(Online_Banking):
    def buy_crypto(self,btc_amount):
        if btc_amount <= self.balance:
            self.balance -= btc_amount
            return f"\n[Success]Crypto Trade:Successfully Bought {btc_amount} BDT worth of Crypto using {self.user_name}'s account Balance. Remaining: {self.balance} BDT."
        return f"\n[ERROR!...]Insufficient Balance to Buy Crypto! Available :{self.balance} BDT."

def main():
    try:
        user = input("Enter your account holder name:").strip()

        initial_balance = int(input("Enter your initial balance:"))

        my_bank = SmartCrypto(user,initial_balance)

        print(f"\n[Account Activated] Account created for {my_bank.user_name} with {my_bank.balance} BDT")

    except ValueError:
        print(f"\n[ERROR]Initial Balance must be an Numeric Value program closing")
        return

    while True:
        print("\n==================OPTION=================")
        print("1. Withdraw Balance")
        print("2. Deposit Balance")
        print("3.Buy Crypto")
        print("q.Quit Program")
        print("============================================")

        choice = input("Enter Your Option(1/2/3/ or q):").strip().lower()
        if choice == "q":
            print("\nExiting... Thank your for your Time")
            break

        try:
            if choice =="1":
                withdraw_input = int(input("Enter the amount you want to withdraw:"))
                if withdraw_input <= 0:
                    print(f"\n[ERROR..]Invalid Withdraw {withdraw_input} Amount! can't be Zero or Negative")
                    continue
                print(my_bank.withdraw(withdraw_input))

            elif choice =="2":
                deposit_input = int(input("Enter the amount you want to deposit:"))
                if deposit_input <= 0:
                    print(f"\n[ERROR..]Invalid Deposit {deposit_input} Amount can't be Zero or Negative")
                    continue
                print(my_bank.deposit(deposit_input))
            elif choice =="3":
                buy_crypto_input = int(input("Enter the amount you want to buy:"))
                if buy_crypto_input <= 0:
                    print(f"\n[ERROR...]Invalid Crypto {buy_crypto_input} Amount can't be Zero or Negative")
                    continue
                print(my_bank.buy_crypto(buy_crypto_input))
            else:
                print(f"\n[ERROR]Invalid Option Selected '{choice}'| Please select 1/2/3 or 'q' ")

        except ValueError:
            print(f"\n[ERROR]Invalid your enter Numeric value")
        except KeyboardInterrupt :
            print("\nExiting...Program stopped safely by the user.")
            break
        except Exception as e:
            print(f"\n[ERROR]The ERROR Occured: {e}")
if __name__ == "__main__":
    main()
