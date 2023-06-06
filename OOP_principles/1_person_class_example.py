# Define a class representing a person.
class Person:

    def __init__(self, name, age):
        """
        Initialize a Person object with the given name and age.
        """
        self.name = name
        self.age = age
    
    def greet(self):
        """
        Class method to greet the person.
        """
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the Person class
person = Person("John", 25)

# Call the greet method on the person object
person.greet()
