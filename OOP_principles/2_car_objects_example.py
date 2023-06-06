# Define a class representing a car
class Car:

    def __init__(self, brand, model):
        """
        Initialize a Car object with the given brand and model.
        """
        self.brand = brand
        self.model = model
    
    def drive(self):
        """
        Simulate driving the car by printing a message.
        """
        print(f"The {self.brand} {self.model} is driving.")

# Create two instances of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

# Call the drive method on the car objects
car1.drive()
car2.drive()
