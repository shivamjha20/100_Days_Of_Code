#keys() → Returns all keys.
student = {"name": "Shivam", "age": 24}
print(student.keys())   # dict_keys(['name', 'age'])

#values() → Returns all values.
print(student.values())   # dict_values(['Shivam', 24])

#items() → Returns key-value pairs as tuples.
print(student.items())   # dict_items([('name', 'Shivam'), ('age', 21)])

#get() → Returns value for a key (safe, no error if missing).
print(student.get("name"))   # Shivam
print(student.get("city", "Not Found"))   # Not Found

