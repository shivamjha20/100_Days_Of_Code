#pop() → Removes a key and returns its value.
student = {"name": "Shivam", "age": 22, "city":"Bihar"}
print(student.pop("city"))   # Jharkhand
print(student)   # {'name': 'Shivam', 'age': 22}

#popitem() → Removes and returns the last inserted key-value pair.
print(student.popitem())   # ('age', 22)
print(student)   # {'name': 'Shivam'}
