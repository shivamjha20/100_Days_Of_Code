# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Student class inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)   # reuse Person's constructor
        self.student_id = student_id
        self.courses = []
    
    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")

# Teacher class inherits from Person
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def assign_grade(self, student, course, grade):
        print(f"{self.name} assigned grade {grade} to {student.name} in {course}")  

# Example usage
student1 = Student("Alice", 20, "S101")
teacher1 = Teacher("Mr. Sharma", 40, "Math")

student1.enroll("Math")
teacher1.assign_grade(student1, "Math", "A")              