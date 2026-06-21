class Goat_Income:
    def __init__(self,target):
        self.target = 150000
    def Check_Status(self,current_income):

        if current_income < self.target:
            gap = self.target - current_income
            return  f"Work Harder! You are {gap} BDT away from your Goal"
        else:
            return f"Congratulations! You have reached your target  {self.target} BDT now you a GOAT Developer"

def main():
    print("Welcome to the GOAT Income")
    while True:
        s_s = input("Enter Start or Stop:").strip().lower()
        if s_s == "start":
            print("Let's Start the GOAT Income")
        elif s_s == "stop":
            print("Quitting the GOAT Income")
            break
        else:
            print("Please Enter either 'start' or 'stop' lower")
            continue
        try:
            income = int(input("Enter Your Income Here:"))
            if income <= 0:
                print(f"[Error]Income can't be Negative")
                continue
            ingoing = Goat_Income(income)
            print(f"\n[status]{ingoing.Check_Status(income)}")
        except ValueError:
            print("Invalid Input: Enter only Integer")
        except Exception as e:
            print(f"The Error Occured: {e}")

if __name__ == "__main__":
    main()
