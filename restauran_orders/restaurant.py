#
from table import Table

#
class Restaurant:
    
    #
    def __init__(self):
        self.tables = [Table(i) for i in range(1,11)]

    #
    def get_table(self, number):
        return self.tables[number -1]
    
    #
    def get_table_orders(self):
        orders = []
        for table in self.table:
            orders.append(table.order)
        return orders

    #
    def get_total_sales(self):
        total = 0
        for order in self.get_table_orders():
            total += order.get_total()
        return total

