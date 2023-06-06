# Define a base class representing a vehicle
class Vehicle:
    def __init__(self, brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def brand_and_name(self):
        print(f"The car is a {self.brand} {self.model} color {self.color}")

# Define a derived class representing a car
class Car(Vehicle):
    def __init__(self, brand, model, color, start_on):
        super().__init__(brand, model, color)
        self.start_on = start_on
    
    def started(self):
        print(f"Is the {self.model}  {self.color} started ?  {self.start_on}")

    def honk(self):
        print("Beep beep!")

# Create an instance of the Car class
car = Car("Toyota", "Camry", "Red", True)

# Call the drive and honk methods on the car object
car.brand_and_name()
car.started()
car.honk()
