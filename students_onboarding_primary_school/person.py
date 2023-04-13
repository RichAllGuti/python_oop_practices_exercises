"""
We need to create the Person class as the parent class for: 
    - students
    - teachers
which each one will be classes more over.

Person class encapsulates the common attributes and methods that both students and teachers will have.

"""

from abc import ABC, abstractmethod

class Person(ABC):

    # Initialize a person with a name and age, the None means that this method does not return anything explicitly.
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    # Introduce the person, the None means that there is no return.
    @abstractmethod
    def introduce(self) -> None:
        pass

