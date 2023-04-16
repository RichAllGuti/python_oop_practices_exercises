#
from student import Student
from teacher import Teacher
from school import School

# Create some students
student1 = Student("Alice", 7, 1)
student2 = Student("Bob", 8, 2)
student3 = Student("Carol", 7, 1)

# Create some teachers
#teacher1 = Teacher("Dave", 35)
#teacher2 = Teacher("Eve", 28 )
#teacher3 = Teacher("John Doe", 35)

# Create a school
school = School("ABC Primary School", "Stret 6")

# Add students and teachers to the school
school.add_student(student1)
school.add_student(student2)
school.add_student(student3)
#school.add_teacher(teacher1)
#school.add_teacher(teacher2)
#teacher3.introduce()
#school.add_teacher(teacher3)
# List the students and teachers in the school
school.list_students()
school.list_teachers()
