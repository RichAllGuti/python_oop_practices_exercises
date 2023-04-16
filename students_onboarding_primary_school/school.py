#
from typing import List

from student import Student
from teacher import Teacher

"""
Define a School class with two instance variables: name and address. 
The __init__ method initializes the name and address variables with values passed as arguments, 
and initializes two empty lists for students and teachers.
"""
class School:
    """A class representing a school."""

    def __init__(self, name: str, address: str) -> None:
        
        #
        self.name = name
        self.address = address
        self.students: List[Student] = []
        self.teachers: List[Teacher] = []


    # Define two methods add_student and add_teacher to add a Student and Teacher object to their respective list.
    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def add_teacher(self, teacher: Teacher) -> None:
        self.teachers.append(teacher)

    """
    Finally define two methods list_students and list_teachers to list all the students and teachers in the school respectively. 
    These methods iterate through the list of students or teachers and call the introduce method on each object, 
    which prints a brief introduction of the student or teacher.
    """
    #
    def list_students(self) -> None:
        """List all the students in the school."""
        print(f"{self.name} Students:")
        for student in self.students:
            student.introduce()


    def list_teachers(self) -> None:
        """List all the teachers in the school."""
        print(f"{self.name} Teachers:")
        for teacher in self.teachers:
            teacher.introduce()

