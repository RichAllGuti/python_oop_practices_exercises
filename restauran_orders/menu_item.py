"""
Here we declare the MenuItem base class and its subclasses. 
Each menu item has a name and a price, which are stored as instance variables in the MenuItem class. 
The Entree, Side, and Drink classes each have additional properties specific to their type of menu item, 
such as protein for Entree and size for Side and Drink.
"""

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Entree(MenuItem):
    def __init__(self, name, price, protein):
        super().__init__(name, price)
        self.protein = protein

    def get_protein(self):
        return self.protein

class Side(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_size(self):
        return self.size

class Drink(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_size(self):
        return self.size