class Cattle_Health:
    def __init__(self,temp):
        self.temp = temp
    def Temp_checker(self):
        if float(self.temp) > 103:
            print(f"Warning_High_Temperature:[{self.temp}-Fahrenheit] Cow might have a Fever.Call The Vet ")
        elif float(self.temp) < 90:
            print(f"Warning_Low_Temperature:[{self.temp}-Fahrenheit] Cow not well.Call The Vet ")
        else:
            print(f"Normal_Temperature:[{self.temp}-Fahrenheit] The Cow is Healthy.")
if __name__ == "__main__":
    while True:
        temp_input = input("To Check The Temperature OR q To quit:")
        if temp_input.lower() == "q" :
             print("Quitting The Program")
             break
        try:
            temp_input = float(temp_input)
            show = Cattle_Health(temp_input)
            show.Temp_checker()
        except ValueError as e:
            print("invalid input.Enter the number OR 'q'")
        except Exception as e:
            print(f"The Error Occured : {e}")
