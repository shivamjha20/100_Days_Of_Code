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

# Example usage
def main():
    students = {}
    courses = {}
    teachers = {}
    sections = {}
    gradebook = GradeBook()

    while True:
        print("\n--- School Grading Menu ---")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Add Teacher")
        print("4. Create Class Section")
        print("5. Assign Student to Section")
        print("6. Enroll Student in Course")
        print("7. Assign Grade")
        print("8. Show Student Grades")
        print("9. Show Course Students")
        print("10. Show Section Students")
        print("11. Generate Report Card")
        print("12. Generate Class Report")
        print("13. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            students[student_id] = Student(name, student_id)
            print(f"Student {name} added.")

        elif choice == "2":
            course_name = input("Enter course name: ")
            courses[course_name] = Course(course_name)
            print(f"Course {course_name} added.")

        elif choice == "3":
            name = input("Enter teacher name: ")
            subject = input("Enter subject: ")
            teachers[name] = Teacher(name, subject)
            print(f"Teacher {name} added.")

        elif choice == "4":
            section_name = input("Enter section name: ")
            sections[section_name] = ClassSection(section_name)
            print(f"Class Section {section_name} created.")

        elif choice == "5":
            student_id = input("Enter student ID: ")
            section_name = input("Enter section name: ")
            if student_id in students and section_name in sections:
                sections[section_name].add_student(students[student_id])
            else:
                print("Invalid student ID or section name.")

        elif choice == "6":
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name: ")
            if student_id in students and course_name in courses:
                students[student_id].enroll(courses[course_name])
            else:
                print("Invalid student ID or course name.")

        elif choice == "7":
            teacher_name = input("Enter teacher name: ")
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name: ")
            grade = int(input("Enter grade (0-100): "))
            if teacher_name in teachers and student_id in students and course_name in courses:
                teachers[teacher_name].assign_grade(students[student_id], courses[course_name], grade)
            else:
                print("Invalid teacher, student, or course.")

        elif choice == "8":
            student_id = input("Enter student ID: ")
            if student_id in students:
                students[student_id].show_grades()
            else:
                print("Student not found.")

        elif choice == "9":
            course_name = input("Enter course name: ")
            if course_name in courses:
                courses[course_name].show_students()
            else:
                print("Course not found.")

        elif choice == "10":
            section_name = input("Enter section name: ")
            if section_name in sections:
                sections[section_name].show_students()
            else:
                print("Section not found.")

        elif choice == "11":
            student_id = input("Enter student ID: ")
            if student_id in students:
                gradebook.generate_report_card(students[student_id])
            else:
                print("Student not found.")

        elif choice == "12":
            section_name = input("Enter section name: ")
            if section_name in sections:
                gradebook.generate_class_report(sections[section_name])
            else:
                print("Section not found.")

        elif choice == "13":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()