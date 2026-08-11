class Parking:
    def __init__(self):
        self.brand = ["Toyota","Mitsubishi","Mazda"]
        self.model = ["Gt86","Evo","Rx7"]
        self.color = ["Black","Red","White"]
    def store_val(self,choice,val):
        if choice == "1":
            self.brand.append(val)
            print(f"Brand is {self.brand}")
        elif choice == "2":
            self.model.append(val)
            print(f"Model is {self.model}")
        elif choice == "3":
            self.color.append(val)
            print(f"Color is {self.color}")
    def show_val(self):
        print(f"[status]show all brands:{self.brand}")
        print(f"[status]show all models:{self.model}")
        print(f"[status]show all colors:{self.color}")

def main():
    my_parking = Parking()

    print("welcome to toton parking")

    while True:
        option = {
            "1":"brand",
           "2":"model",
            "3":"color",
            "e":"to exit"
        }
        for key,value in option.items():
            print(f"{key}: {value.capitalize()}")
        choice = input("Enter your choice(1-3 or Exit):").lower().strip()

        if choice == "e":
            print("Exiting...")
            break
        try:
            if choice in ["1","2","3"]:
                val = input(f"Enter the option you want to use{option[choice]}:").strip()
                my_parking.store_val(choice,val)
                my_parking.show_val()
            else:
                print("[Error]Invalid Option Enter a Valid Option")

        except Exception as e:
            print(f"[Error]An unexpected error occurred:{e}")

if __name__ == "__main__":
    main()
