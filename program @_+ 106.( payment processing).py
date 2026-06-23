from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class Visa(Payment):
    def pay(self, amount):
        return f"Your Payment {amount} Successfully Paid By Visa"

class Pay_pal(Payment):
    def pay(self, amount):
        return f"Your Payment {amount} Successfully Paid By PayPal"

def main():
    print("Welcome P.T.M Online Payment Service")

    while True:
        print("\nSelect Your Options:")
        print("1.To Use Visa")
        print("2.To Use PayPal")
        print("'e' to Exit")
        choice = input("Enter your Choice:").lower().strip()
        if choice == "e":
            print("Goodbye.The program will now exit.")
            break
        try:
            if choice == "1":
                use_visa = int(input("Enter Visa Payment Amount here:"))
                if use_visa < 0:
                    print(f"\n[Error]Invalid payment {use_visa} amount! Payment amount can't be Negative.")
                    continue

                check = Visa()
                print(f"\n[Info] {check.pay(use_visa)}")

            elif choice == "2":
                use_paypal = int(input("Enter PayPal Amount here:"))
                if use_paypal < 0:
                    print(f"\n[Error] Invalid payment {use_paypal} amount! Payment amount can't be Negative.")
                    continue
                cho = Pay_pal()
                print(f"\n[Info] {cho.pay(use_paypal)}")

        except ValueError:
            print("\n[Error]Invalid Input: You can Enter only integers.")
        except Exception as e:
            print(f"\n[Error]The Error Occured:{e}")
        else:
            print("\n[Info]The Payment Successful!")

if __name__ == "__main__":
    main()
