#pop() → Removes a key and returns its value.
student = {"name": "Shivam", "age": 22, "city":"Bihar"}
print(student.pop("city"))   # Jharkhand
print(student)   # {'name': 'Shivam', 'age': 22}

#popitem() → Removes and returns the last inserted key-value pair.
print(student.popitem())   # ('age', 22)
print(student)   # {'name': 'Shivam'}

#clear() → Removes all items.
student.clear()
print(student)   # {}

#copy() → Returns a shallow copy.
student = {"name": "Shivam", "age": 23}
new_student = student.copy()
print(new_student)   # {'name': 'Shivam', 'age': 23}
