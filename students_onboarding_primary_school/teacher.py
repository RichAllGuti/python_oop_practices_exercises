#
from person import Person

#
class Teacher(Person):

    #This method initializes the Teacher object with the name and age attributes 
    # from the Person superclass, as well as its own grade attribute.
    def __ini__(self, name: str, age: int, subject: str) -> None:
        super().__init__(name, age)
        self.subject = subject

    # Prints out a message that introduces the teacher object, including its name and grade.
    def introduce(self) -> None:
        print(f"My name is {self.name} and I teach {self.subject}.")
    
