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