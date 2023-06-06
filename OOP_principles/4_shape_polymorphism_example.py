# Define a base class representing a shape
class Shape:
    def calculate_area(self):
        pass

# Define derived classes representing different shapes
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

# Create instances of different shape objects
rectangle = Rectangle(4, 6)
circle = Circle(3)

# Call the calculate_area method on the shape objects
print(rectangle.calculate_area())
print(circle.calculate_area())
