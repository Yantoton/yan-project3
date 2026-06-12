class Farm_Finance:
    def __init__(self,profit):
        self.__total_profit = profit
    def get_profit(self,password):
        if password == "<PASSWORD>":
            print(f"Total Profit: {self.__total_profit} BDT")
        else:
            print("OOPS:Wrong Password")

my_farm = Farm_Finance(1000000)
pass_input = input("Enter Password to see profit:")
my_farm.get_profit(pass_input)
try:
    print(my_farm.__total_profit)
except AttributeError as e:
    print(f"AttributeError: [Security Alert]:{e}")
