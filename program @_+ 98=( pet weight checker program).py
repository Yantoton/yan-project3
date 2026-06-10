class pet_check:
    def __init__(self,weight):
        self.weight = weight
    def pet_weight(self):
        if self.weight >= 5 :
            return f"pet weight is {self.weight} kg Your pet is Healthy"
        elif 1<= self.weight < 5 :
            return f"pet weight is {self.weight} kg Your pet needs to be Health"

def main():
    while True:
        pet_weight = input("Enter your pet weight or q to quit: ").strip().lower()
        if pet_weight == "q":
            print("Quitting...The Program will exit now [Goodbye]")
            break
        try:
            pet_weight = int(pet_weight)
            if pet_weight <= 0:
                print(f"Invalid input {pet_weight} Weight can't be 0 OR Negative")
                continue
            info = pet_check(pet_weight)
            # info.pet_weight()
            print(f"\n[Info] {info.pet_weight()}")
        except ValueError:
            print(f"Invalid input {pet_weight} You Can enter only integer ")

        except Exception as e:
            print(f"The Error Occured {e}")

if __name__ == "__main__":
    main()
