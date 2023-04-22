#
from order import Order

#
class Table:

    #
    def __ini__(self, number):
        self.number = number
        self.order = Order()

    #
    def add_item(self, item):
        self.order.add_item(item)
    
