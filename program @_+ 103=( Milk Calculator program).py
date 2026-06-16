class Milk_Calculator:
    def __init__(self,morning,evening):
        self.morning = morning
        self.evening = evening
        self.total = 0
    def get_total(self):
        self.total = self.morning + self.evening
        print(f"[Result] The total milk from both times is {self.total} liters.")

def main():
    print("___ Welcome to P.T.M Farm Management___")
    while True:
        choice = input("Do you want to calculate milk [yes/no]:").strip().lower()
        if choice == "yes":
            print("\n --- Let's Calculate Milk ---")
        elif choice == "no":
            print("--- Quiting Milk Calculator ---")
            break
        else:
            print("Invalid Choice: please enter either 'yes' or 'no'")
            continue
        try:
            morning = float(input("Enter your morning milk calculate:"))

            evening = float(input("Enter your evening milk calculate:"))

            calculate = Milk_Calculator(morning,evening)
            calculate.get_total()
        except ValueError:
            print("[Error] Invalid Input! Please enter only integers")

        except Exception as e:
            print(f"The Error Occured:{e}")

if __name__ == "__main__":
    main()
