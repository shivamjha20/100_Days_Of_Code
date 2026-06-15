import json

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id, class_section=None):
        super().__init__(name)
        self.student_id = student_id
        self.class_section = class_section
        self.grades = {}

    def enroll(self, course):
        course.add_student(self)
        print(f"{self.name} enrolled in {course.course_name}")

    def show_grades(self):
        print(f"Grades for {self.name}:")
        if not self.grades:
            print("No grades yet.")
        for course, grade in self.grades.items():
            print(f"- {course}: {grade}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def assign_grade(self, student, course, grade):
        student.grades[course.course_name] = grade
        print(f"{self.name} assigned {grade} to {student.name} in {course.course_name}")