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

'''fromkeys() → Creates a dictionary from a list of keys with a
default value'''
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)   # {'a': 0, 'b': 0, 'c': 0}

'''setdefault() → Returns value of a key; if not present, inserts
 it with a default.'''

student = {"name": "Shivam"}
print(student.setdefault("age", 21))   # 21
print(student)   # {'name': 'Shivam', 'age': 21}
