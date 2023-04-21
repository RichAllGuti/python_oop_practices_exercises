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
