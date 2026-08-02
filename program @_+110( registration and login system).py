from abc import ABC, abstractmethod
import json
import os
class Login(ABC):
    @abstractmethod
    def login(self,username,password):
        pass
class LoginManager(Login):
    def __init__(self,filename="users.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename,"w") as file:
                json.dump({},file)

    def load_users(self):
        with open(self.filename, "r") as file:
            return json.load(file)

    def register(self,username,password):
        users = self.load_users()
        if username in users:
            print(f"[Error] Username '{username}' already registered")
            return

        users[username] = password
        with open(self.filename,"w") as file:
            json.dump(users, file, indent = 4)
            print(f"[Success] User registered '{username}' successfully")

    def login(self,username,password):
        users = self.load_users()
        if username in users and users[username]== password:
            print(f"[Info] Correct password: Access Granted for {username}")
        else:
            print(f"[Error] Incorrect password: Access  Denied for {username}")
def main():
    manager = LoginManager()
    print("Welcome to <P.T.M>LoginManager")
    while True:
        option = {
            "\n1.":"Register",
            "2.":"Login",
            "e" :"To Exit"
        }
        print("\n---Option Menu---")
        choice = input("Select an Option (1-2 or Exit):").lower().strip()
        if choice == "e":
            print("Exiting Program Goodbye>>>")
            break
        try:
            if choice == "1":
                user = input("Type New Username Here:").strip()
                pwd = input("Type New Password Here:").strip()
                if user and pwd:
                    manager.register(user,pwd)
                else:
                    print("[Error] Fields can't be blank")

            elif choice == "2":
                user = input("Enter Username Here:").strip()
                pwd = input("Enter Password Here:").strip()
                manager.login(user,pwd)

            else:
                print("[Error]Invalid Choice")

        except Exception as e:
            print(f"[Error] An Unknown Error Occured: {e}")


if __name__ == "__main__":
    main()
