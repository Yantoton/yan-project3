import os
from datetime import datetime
def os_system():
    print("Welcome to the <P.T.M> command system")

    try:
        cmd = input("give your command (open chrome / open notepad):").lower()

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"Current Time : {current_time}")

        if "chrome" in cmd:
            os.system("start chrome")
        elif "notepad" in cmd:
            os.system("start notepad")
        else:
            print("Invalid command...! please try again 'open chrome' or 'open notepad'..!")
            return

        with open ("system.txt", "a") as file:
            file.write(f"__Current useing app time is : [{current_time}] App Started: {cmd}\n")
            file.write(f"Successfully started: {cmd}\n")
    except Exception as e:
        print(f"Error Occured ?..:{e}")

    else:
        print(" successfully the system app started")

    finally:
        print("Program ended")

if __name__ == "__main__":
    os_system()
