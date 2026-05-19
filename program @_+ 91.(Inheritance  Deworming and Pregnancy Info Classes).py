class Deworming_info:
    def __init__(self,age):
        self.age = age
    def month_age(self):
        if self.age < 6 :
            print(f"the age is {self.age} month old:Give 1 Deworming Tablet")
        elif 6 <= self.age < 12:
            print(f"The age is {self.age} month old:Give 2 Deworming Tablet")
        else:
            print(f"The age is {self.age} Month old:Give 3 Deworming Tablet")
if __name__ == "__main__":
    while True:
        age_input = input("To Check The Deworming age OR q To quit:")
        if age_input.lower() == "q":
            print("Quitting The Program")
            break
        try:
            age_input = int(age_input)
            info = Deworming_info(age_input)
            info.month_age()
        except ValueError as e:
            print("Invalid Input:You can Enter only Integers OR ['q'] To Quitting The Program")
        except Exception as e:
            print(f"The Error Occured : {e}")

class cow(Deworming_info):
    def pregnancy(self):
        if self.age > 1 and self.age <= 3:
            print(f"First Trimester: {self.age} pregnancy month It is highly sensitive to strong drugs, which can cause fetal loss.")
        elif self.age >= 4 and self.age <= 6:
            print(f"Second Trimester: {self.age} pregnancy month This is a stable period and the safest time for regular vaccinations and deworming.")
        elif self.age >=  7 and self.age <= 9:
            print(f"Third Trimester: {self.age} pregnancy month Cows need good quality nutrition. Do not deworm in the last month to avoid ")
        else:
            print(f"{self.age} month You can start milking now.")
if __name__ == "__main__":
    while True:

            preg_age_input = input("To Check The Pregnancy age For Deworming OR 'q' TO quit:").lower().strip()
            if preg_age_input == "q":
                print("Quitting The Program")
                break
            try:
                preg_age = int(preg_age_input)
                info = cow(preg_age)
                info.pregnancy()
            except ValueError:
                print("Invalid Input:You can Enter only Integers OR ['q'] To Quitting The Program")
            except Exception as e:
                print(f"The Error Occured: {e}")
