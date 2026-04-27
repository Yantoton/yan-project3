from datetime import datetime

def calculate_fact(n):
    if n == 0 or n == 1:
        
        return 1
    
    else:
        
        return n * calculate_fact(n - 1)

def main():
    
    print("__P.T.M Factorial Calculator__")
    
    current_time = datetime.now().strftime("%d-%m-%Y_%H%M%S")
    
    print("Current Date/Time:",current_time)
    
    while True:
        
        num = input("Enter the number here or type '(q to quiti)' :").strip().lower()
        
        if num == "q":
            
            print("Quiting The __P.T.M Factorial Calculator__")
            
            break
        try:
            num = int(num)
            
            if num < 0:
                
                print("Error...: Factorial number should be positive Number")
                
                continue

            result = calculate_fact(num)
            
            print(f"Factorial of {num} is {result}")


            with open("fact.txt", "a", encoding="utf-8") as file:
                file.write(f"Current Program Date/Time:{current_time}\n"
                           f"Factorial of {num} is {result}\n")
                print("Successfully Calculated Factorial and save the file to fact.txt")
        except ValueError:
            
            print("Error...: Invalid Input The value must be an integer")
            
        except Exception as e:
            
            print(f"Error...: An unexpected Error Occured: {e}")
            
if  __name__ == "__main__":
    main()
