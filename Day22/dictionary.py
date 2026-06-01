'''
A dictionary is a collection of key-value pairs.
Defined using curly braces {} with keys and values separated by :.
Keys must be unique and immutable (like strings, numbers, tuples).
Values can be of any type (even lists or other dictionaries).'''
# Example 1: Creating a dictionary
student = {
    "name": "Shivam",
    "age": 24,
    "course": "Python"
}
print(student)

# Example 2: Accessing values
print(student["name"])    # Shivam
print(student.get("age")) # 24

# Example 3: Adding and updating values
student["city"] = "Haryana"
student["age"] = 23
print(student)

# Example 4: Removing items
student.pop("course")     # removes 'course'
print(student)

# Example 5: Looping through dictionary
for key, value in student.items():
    print(key, ":", value)

# Example 6: Nested dictionary
students = {
    "101": {"name": "Shivam", "age": 21},
    "102": {"name": "Amit", "age": 22}
}
print(students["101"]["name"])   # Shivam
