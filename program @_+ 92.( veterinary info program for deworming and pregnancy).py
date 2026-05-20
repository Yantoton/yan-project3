class Deworming_Info:
    def __init__(self,age):
        self.age = age
    def Month_Age_Info(self):
        if self.age < 6 :
            return f"The age is {self.age} month old:Give 1 Deworming Tablet"
        elif 6 <= self.age < 12:
            return f"The age is {self.age} month old:Give 2 Deworming Tablet"
        else:
            return f"The age is {self.age} Month old:Give 3 Deworming Tablet"

class Cow(Deworming_Info):
    def Pregnancy_Advice(self):
        if  1 <=  self.age <= 3:
            return f"(First Trimester): {self.age} pregnancy month It is highly sensitive to strong drugs, which can cause fetal loss."
        elif 4 <= self.age <= 6:
            return f"(Second Trimester): {self.age} pregnancy month This is a stable period and the safest time for regular vaccinations and deworming."
        elif 7 <= self.age <= 9:
            return f"(Third Trimester): {self.age} pregnancy month Cows need good quality nutrition. Do not deworm in the last month to avoid "
        else:
            return f" status {self.age} month.The cow standard 1-9 month pregnancy period."

def Main():
    print("--- welcome To (P.T.M) Veterinary Info ---  ")
    while True:
        print("\nOptions:")
        print("1. Check Deworming dose age advice")
        print("2. Check pregnancy Deworming advice ")
        print("'q' to exit")

        choice = input("Enter Your Choice: ").lower().strip()

        if choice == "q":
            print("Quitting... the program will stop now")
            break

        try:
            if choice == '1':
                age = int(input("To Check Deworming dose age:"))
                if age < 0:
                    print("Age can't be negative")
                    continue
                info = Deworming_Info(age)
                print(f"\n[Info] {info.Month_Age_Info()}")

            elif choice == '2':

                preg_age = int(input("To Check pregnancy Deworming advice:"))
                if preg_age < 0:
                    print("Month can't be negative")
                info = Cow(preg_age)
                print(f"\n[Advice] {info.Pregnancy_Advice()}")

            else:
                print("Invalid Choice! please select 1, 2, OR q")

        except ValueError:
            print("Invalid  Input,Enter only Integer Value ")

        except Exception as e:
            print(f"The Error Occured: {e}")


if __name__ == "__main__":
    Main()
