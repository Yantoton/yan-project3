class bull:
    def __init__(self,name,tag,weight):
        self.name = name
        self.tag = tag
        self.weight = weight
    def show_info(self):
        print(f"Bull name: {self.name},tag number: {self.tag},weight: {self.weight} kg")

sahiwal = bull("Sahiwal",97,800)
rcc = bull("RCC",67,600)
holstein = bull("Holstein",76,1200)

sahiwal.show_info()
rcc.show_info()
holstein.show_info()

class Moto_Bike:
    def __init__(self,name,number,weight,color):
        self.name = name
        self.number = number
        self.weight = weight
        self.color = color
    def info(self):
        print(f"Bike name:{self.name},Number_plate:{self.number},weight:{self.weight} kg,Bike color:{self.color}")

v2 = Moto_Bike("R15v2","Dhaka_Metro_La-27-4888",131,"Gray_Black")

v2.info()

class Bike_Fuel:
    def __init__(self):
        self.fuel = 0
    def Get_bike_fuel(self):
        self.fuel = int(input("Enter Bike Fuel Here:"))
    def check_fuel(self):
        if self.fuel < 5:
            print("Bike in Reserve mode")
        else:
            print("Bike out of Reserve mode")


fuel = Bike_Fuel()
fuel.Get_bike_fuel()
fuel.check_fuel()

class Result:
    def __init__(self,mark):
        self.result = mark
    def Check_Mark(self):
        if self.result <33:
            print(f"[F] You Failed This Exam mark is:{self.result}")
        elif self.result > 80:
            print(f"[A+] You Passed mark is: {self.result}")
        elif self.result >= 70:
            print(f"[B] You Passed mark is: {self.result}")
        elif self.result >= 50:
            print(f"[C] You Passed mark is: {self.result}")
        elif self.result >= 33:
            print(f"[D] You Passed mark is: {self.result}")

mark =int(input("Enter the mark:"))
show=Result(mark)
show.Check_Mark()

class Num_check:
    def __init__(self,num):
        self.num = num
    def Check_Num(self):
        if self.num % 2 == 0:
            print(f"This is Even {self.num} number")
        else:
            print(f"This is Odd {self.num} number")

num = int(input("Enter the number here:"))
show = Num_check(num)
show.Check_Num()

class Movie_Ticket:
    def __init__(self,age):
        self.age = age
    def check_age(self):
        if self.age < 5:
            print(f"Age is {self.age}The Movie Ticket is Free")
        elif self.age >= 5 and self.age <= 11 :
            print(f"Age is {self.age} The Movie Ticket Price $10")
        elif self.age >=12 and self.age <= 17:
            print(f"Age is {self.age} The Movie Ticket Price $15")
        elif self.age >= 18:
            print(f"Age is {self.age} The Movie Ticket Price $20")

age_input = int(input("Enter your age:"))
show = Movie_Ticket(age_input)
show.check_age()
import mahiyan
output = mahiyan.calculator()
