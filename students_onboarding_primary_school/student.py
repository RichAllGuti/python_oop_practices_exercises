#
from person import Person

class Student(Person):
    
    #This method initializes the Student object with the name and age attributes 
    # from the Person superclass, as well as its own grade attribute.
    def __init__(self, name: str, age: int, grade: int) -> None:
        super().__init__(name, age)
        self.grade = grade


    # Prints out a message that introduces the Student object, including its name and grade.
    def introduce(self) -> None:
        print(f"My name is{self.name} and I'm in grade {self.grade} ")

