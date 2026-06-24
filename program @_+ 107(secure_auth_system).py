from abc import ABC, abstractmethod
class SecuritySystem(ABC):
    @abstractmethod
    def authenticate(self,password):
        pass
class IntPassword(SecuritySystem):
    def authenticate(self,password):
        if password == 4343:
            return f"Checking Integer Password....Correct {password} Access Granted"
        else:
            return f"[ERROR]Checking Integer Password....Incorrect {password} Access Denied"

class StrPassword(SecuritySystem):
    def authenticate(self,password):
        if password == "thomas":
            return f"Checking String Password....Correct {password} Access Granted "
        else:
            return f"[ERROR]Checking String Password....Incorrect {password} Access Denied"

def main():
    print("Welcome .P>T<M. Security System")
    while True:
        print("\nOptoins")
        print("1.To check IntPassword ")
        print("2.To check StrPassword ")
        print("'e' to exit")

        choice =input("Enter your choice: ").lower().strip()
        if choice == "e":
            print("\n[STATUS]Exiting .P>T<M. Security System...Goodbye.")
            break
        try:
            if choice == "1":
                int_p =int(input("Type Password in Integer here:"))
                checker = IntPassword()
                print(f"\n[STATUS] {checker.authenticate(int_p)}")

            elif choice == "2":
                str_p = input("Type Password in String here:").strip()
                checker = StrPassword()
                print(f"\n[STATUS] {checker.authenticate(str_p)}")
            else:
                print("[ERROR]Invalid Choice....")
        except ValueError:
            print("\n[ERROR]Invalid Input!.. Enter Only Integer Try Again")

        except  Exception as e:
            print(f"\n[ERROR]The Error Occurred: '{e}' Try Again")



if __name__ == "__main__":
    main()
