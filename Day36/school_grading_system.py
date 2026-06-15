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

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        print(f"Students in {self.course_name}:")
        for s in self.students:
            print(f"- {s.name} ({s.student_id})")

class ClassSection:
    def __init__(self, section_name):
        self.section_name = section_name
        self.students = []

    def add_student(self, student):
        student.class_section = self.section_name
        self.students.append(student)
        print(f"{student.name} assigned to {self.section_name}")

    def show_students(self):
        print(f"Students in {self.section_name}:")
        for s in self.students:
            print(f"- {s.name} ({s.student_id})")


class GradeBook:
    def calculate_gpa(self, student):
        if not student.grades:
            return None
        total = sum(student.grades.values())
        gpa = total / len(student.grades)
        return gpa

    def generate_report_card(self, student):
        print("\n--- Report Card ---")
        print(f"Student: {student.name} ({student.student_id}) | Class: {student.class_section}")
        print("Grades:")
        if not student.grades:
            print("No grades yet.")
        else:
            for course, grade in student.grades.items():
                print(f"- {course}: {grade}")
            gpa = self.calculate_gpa(student)
            print(f"GPA: {gpa:.2f}")
        print("-------------------\n")

    def generate_class_report(self, class_section):
        print(f"\n=== Report Cards for {class_section.section_name} ===")
        for student in class_section.students:
            self.generate_report_card(student)