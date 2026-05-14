class Bull_feed:
    def __init__(self,weight):
        self.weight = weight
    def Bull_diet(self):
        if self.weight >= 500:
            print(f"Bull_Weight_is:{self.weight}-Kg.Feed_Suggestion:High Protein Diet & 20kg Green Grass")
        elif self.weight >= 300 and self.weight < 500:
            print(f"Bull_Weight_is:{self.weight}-kg.Feed_Suggestion:Standard Diet & 15kg Green Grass")
        else:
            print(f"Bull_Weight_is:{self.weight}-kg.Feed_Suggestion:Starter Diet & 10kg Green Grass")
weight_input = float(input("To Check The Bull_Weight:"))
if __name__ == "__main__":
    show = Bull_feed(weight_input)
    show.Bull_diet()
