'''The enumerate() function in Python is a built-in tool that
 makes looping easier when you need both the index and the value
 of items in an iterable (like a list, tuple, or string).
 Syntax:- enumerate(iterable, start=0)
iterable → the sequence you want to loop through.
start → optional, the index to start counting from (default is 0).
'''
# Example 1: Basic usage
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Example 2: Custom start index
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Example 3: Using enumerate with list comprehension
indexed_fruits = [(i, f) for i, f in enumerate(fruits)]
print(indexed_fruits)



'''Key Points
enumerate() saves you from manually using range(len(...)).
It's cleaner, more Pythonic, and avoids off-by-one errors.
Often used in loops where both position and value matter.'''