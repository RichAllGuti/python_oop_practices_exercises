#
from menu_item import MenuItem

#
class Order:

    #
    def __init__(self):
        self.items = []

    #
    def add_item(self, item):
        self.items.append(item)

    #
    def remove_item(self, item):
        self.items.remove(item)

    #
    def get_total(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total

    #
    def generate_bill(self):

        #
        print("\n")
        print("+--------------------------------------------------+")
        print("|                     Bill                         |")
        print("+--------------------------------------------------+")
        
        for item in self.items:
            print(f"| {item.get_name() :<20} {item.get_price() :>10} {'|' :>18}")
        
        print("+--------------------------------------------------+")
        print(f"| {'Total:':<20} {self.get_total() :>10} {'|' :>18}")
        print("+--------------------------------------------------+")
        print("\n")

