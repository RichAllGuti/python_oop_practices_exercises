import unittest
from menu_item import Entree, Side, Drink
from order import Order
from table import Table
from restaurant import Restaurant


class TestRestaurantOrderingSystem(unittest.TestCase):

    def setUp(self):
        self.entree1 = Entree('Steak', 20.0, 'beef')
        self.side1 = Side('Fries', 5.0, 'large')
        self.drink1 = Drink('Soda', 2.0, 'medium')

        self.entree2 = Entree('Chicken', 15.0, 'chicken')
        self.side2 = Side('Salad', 7.0, 'small')
        self.drink2 = Drink('Water', 0.0, 'small')

        self.order1 = Order()
        self.order1.add_item(self.entree1)
        self.order1.add_item(self.side1)
        self.order1.add_item(self.drink1)

        self.order2 = Order()
        self.order2.add_item(self.entree2)
        self.order2.add_item(self.side2)
        self.order2.add_item(self.drink2)

        self.table1 = Table(1)
        self.table1.add_item(self.entree1)
        self.table1.add_item(self.side1)
        self.table1.add_item(self.drink1)

        self.table2 = Table(2)
        self.table2.add_item(self.entree2)
        self.table2.add_item(self.side2)
        self.table2.add_item(self.drink2)

        self.restaurant = Restaurant()
        self.restaurant.add_table(self.table1)
        self.restaurant.add_table(self.table2)

    def test_menu_item_get_name(self):
        self.assertEqual(self.entree1.get_name(), 'Steak')
        self.assertEqual(self.side1.get_name(), 'Fries')
        self.assertEqual(self.drink1.get_name(), 'Soda')

    def test_menu_item_get_price(self):
        self.assertEqual(self.entree1.get_price(), 20.0)
        self.assertEqual(self.side1.get_price(), 5.0)
        self.assertEqual(self.drink1.get_price(), 2.0)

    def test_entree_get_protein(self):
        self.assertEqual(self.entree1.get_protein(), 'beef')
        self.assertEqual(self.entree2.get_protein(), 'chicken')

    def test_side_get_size(self):
        self.assertEqual(self.side1.get_size(), 'large')
        self.assertEqual(self.side2.get_size(), 'small')

    def test_drink_get_size(self):
        self.assertEqual(self.drink1.get_size(), 'medium')
        self.assertEqual(self.drink2.get_size(), 'small')

    def test_order_add_remove_items(self):
        self.assertEqual(len(self.order1.items), 3)
        self.order1.remove_item(self.drink1)
        self.assertEqual(len(self.order1.items), 2)

    def test_order_get_total(self):
        self.assertEqual(self.order1.get_total(), 27.0)
        self.assertEqual(self.order2.get_total(), 22.0)

    def test_table_add_item(self):
        self.assertEqual(len(self.table1.order.items), 3)
        self.table1.add_item(self.drink2)
        self.assertEqual(len(self.table1.order.items), 4)

    def test_restaurant_add_table(self):
        self.assertEqual(len(self.restaurant.tables), 2)
        table3 = Table(3)
        self.restaurant.add_table(table3)
        self.assertEqual(len(self.restaurant.tables), 3)

    def test_restaurant_get_total_revenue(self):
        # create a new order and add it to table 1
        entree3 = Entree('Fish', 18.0, 'fish')
        side3 = Side('Rice', 4.0, 'small')
        drink3 = Drink('Beer', 5.0, 'large')
        order3 = Order()
        order3.add_item(entree3)
        order3.add_item(side3)
        order3.add_item(drink3)
        self.table1.add_item(entree3)
        self.table1.add_item(side3)
        self.table1.add_item(drink3)
        
        # calculate expected total revenue
        total_revenue = self.entree1.get_price() + self.side1.get_price() + self.drink1.get_price() + \
                        self.entree2.get_price() + self.side2.get_price() + self.drink2.get_price() + \
                        entree3.get_price() + side3.get_price() + drink3.get_price()
        
        self.assertEqual(self.restaurant.get_total_revenue(), total_revenue)

    def test_restaurant_get_table_by_number(self):
        # test getting a table that exists
        self.assertEqual(self.restaurant.get_table_by_number(1), self.table1)
        
        # test getting a table that does not exist
        self.assertIsNone(self.restaurant.get_table_by_number(3))

    def test_restaurant_get_orders(self):
        orders = self.restaurant.get_orders()
        self.assertIn(self.order1, orders)
        self.assertIn(self.order2, orders)
        self.assertNotIn(Order(), orders) # make sure an empty order is not included in the list

