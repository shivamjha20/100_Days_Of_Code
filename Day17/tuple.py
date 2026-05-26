'''A tuple is a collection of items just like a list,
 but with one key difference:
Tuples are immutable (cannot be changed after creation).
Defined using parentheses ().
Can contain mixed data types.
Useful when you want data to remain constant.'''
# Example 1: Creating a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)

# Example 2: Accessing elements
print(fruits[0])   # apple
print(fruits[2])   # cherry

# Example 3: Tuples with mixed data types
mixed = (1, "hello", 3.14, True)
print(mixed)

# Example 4: Nested tuple
nested = (("a", "b"), (1, 2))
print(nested)

# Example 5: Tuple unpacking
person = ("Shivam", 21, "India")
name, age, country = person
print(name, age, country)

# Example 6: Single-element tuple (note the comma!)
single = ("apple",)
print(type(single))   # <class 'tuple'>

