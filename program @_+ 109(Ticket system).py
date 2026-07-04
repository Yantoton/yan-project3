from abc import ABC, abstractmethod

class TicketSystem(ABC):
    @abstractmethod
    def calculate_price(self):
        pass
class VIPTicket(TicketSystem):
    def __init__(self,quantity):
        self.ticket_type = "VIP"
        self.quantity = quantity
    def  calculate_price(self):
       price=500
       total = price *self.quantity

       if self.quantity >= 6:
            discount = total * 0.1
            total = total - discount
            print(f"\nCongratulations! You got a 10% $ discount of {discount}")
       return f"Total Price for {self.quantity} {self.ticket_type} tickets is ${total}"


class RegularTicket(TicketSystem):
    def __init__(self,quantity):
        self.ticket_type ="Regular"
        self.quantity = quantity
    def  calculate_price(self):
        price=100
        total = price * self.quantity

        if self.quantity >= 8:
            discount = total * 0.1
            total = total - discount
            print(f"\nCongratulations! You got a 10% $ discount of {discount}")
        return f"Total Price for {self.quantity} {self.ticket_type} tickets is ${total}"

def main():
    print("Welcome to .P<T>M. Ticket System")
    while True:
        print("\n1.Fifa Vip Ticket-($500)| 2.Fifa Regular Ticket-($100) | 'e' to Exit")

        choice = input("Select an Ticket Option:").lower().strip()
        if choice == "e": break

        try:
            if choice == "1":
              qnty= int(input("To Purchase Vip Ticket Here:"))
              if qnty <= 0:continue
              check_ticket=VIPTicket(qnty)
              print(f"\n[Status]{check_ticket.calculate_price()}")
            elif choice == "2":
                qnty = int(input("To Purchase Regular Ticket Here:"))
                if qnty <= 0:continue
                check_ticket = RegularTicket(qnty)
                print(f"\n[Status]{check_ticket.calculate_price()}")

        except ValueError:
            print("[Error]Invalid Input Enter Only Numbers ")

        except Exception as e:
            print(f"[ERROR] The Occurred {e}")

if __name__ == "__main__":
    main()
