from menu_item import Entree, Side, Drink
from order import Order

def main():

    # Example
    order = Order()

    #
    entree = Entree("Chicken Alfredo", 15.99, "Chicken")
    side = Side("Garlic Bread", 4.99, "Large")
    drink = Drink("Soda", 2.99, "Medium")
    drink = Drink("cup of wine", 5.50, "300ml")

    order.add_item(entree)
    order.add_item(side)
    order.add_item(drink)

    order.generate_bill()

    order.remove_item(side)

    order.generate_bill()

if __name__ == "__main__":
    main()