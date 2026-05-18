class Smart_Calculator:
    def __init__ (self,num1,operator,num2):
        self.num1 = num1
        self.operator = operator
        self.num2 = num2
    def calculator(self):
        if self.operator == "+":
            return  self.num1 + self.num2
        elif self.operator == "-":
            return self.num1 - self.num2
        elif self.operator == "*":
            return  self.num1 * self.num2
        elif self.operator == "/":
            if self.num2 == 0:
                raise ZeroDivisionError("Division_Error: You can't divide by zero ")
            return self.num1 / self.num2
        else:
            return "Error: Operator Not Supported"
if __name__ == "__main__":
 print("|___Welcome to The P.T.M Smart Calculator___|")
 print("Operations: + (Add), - (Subtract), * (Multiply), / (Divide)")
 while True:
                try:
                    ask=input("Enter do want to calculate (yes/no):").lower().strip()
                    if ask == "yes":
                         print("Starting the Calculation")
                    elif ask == "no":
                        print("Quitting The Program")
                        break
                    else:
                        print("You can only use 'yes or no'")
                        break

                    num1 = float(input("Please Enter the first number:"))

                    operator = input("Enter operator:( '+' , '-' , '*' , '/' ):").strip()

                    num2 = float(input("Please enter the second number:"))

                    calc = Smart_Calculator(num1,operator,num2)
                    result = calc.calculator()

                    print(f"The Result Is: {num1} {operator} {num2} = {result}")

                except ValueError:
                    print("Invalid Input!: Please Enter only Integers Try again ")
                except Exception as e:
                    print(f"The Error Occurred : {e}")
