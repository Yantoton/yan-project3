from abc import ABC, abstractmethod

class Vault(ABC):
    @abstractmethod
    def open_vault(self,key):
        pass
class MobileVault(Vault):
    def __init__(self,balance):
        self.__balance = balance
    def open_vault(self,password):
        word_pass = "melon"
        if password == word_pass:
            return f"[SUCCESS] Vault Opened!..Your balance is {self.__balance} BDT"
        else:
            return "[DENIED] Vault Can't Open Password Is Wrong"

class CardVault(Vault):
    def __init__(self,balance):
        self.__balance = balance
    def open_vault(self,password):
        pin_pass = 54321
        if password == pin_pass:
            return f"[SUCCESS] Vault Opened!..Your balance is {self.__balance} BDT"
        else:
            return "[DENIED] Vault Can't Open password Is Wrong"

def main():
    print("Welcome .P<T>M. Vault System")
    while True:
        print("\n1.TO Mobile Vault | 2. TO Card Vault | 'e'.To Exit")

        choice = input("Select an Option:").lower().strip()

        if choice ==  "e": break

        try:
            if choice == "1":
                mob_balance =  MobileVault(1200)
                word_pass = input("Enter MobileVault Password:").strip()
                print(mob_balance.open_vault(word_pass))
            elif choice == "2":
                card_balance = CardVault(1300)
                pin_pass = int(input("Enter CardVault 5-digit Pin:"))
                print(card_balance.open_vault(pin_pass))
        except ValueError:
            print("[ValueError] Invalid Input Enter Numbers Only!..Try Again")
        except AttributeError as e:
            print(f"[AttributeError] Security Alert!..: {e}")

if __name__ == "__main__":
    main()
