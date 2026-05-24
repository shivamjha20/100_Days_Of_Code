'''A list is a collection of items in Python that can hold
 multiple values in a single variable.

Defined using square brackets [].

Lists are ordered, mutable (can be changed), and can contain
 mixed data types.'''
# Example 1: Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Example 2: Accessing elements
print(fruits[0])   # apple
print(fruits[2])   # cherry

# Example 3: Modifying elements
fruits[1] = "mango"
print(fruits)      # ['apple', 'mango', 'cherry']

# Example 4: Adding elements
fruits.append("orange")
print(fruits)      # ['apple', 'mango', 'cherry', 'orange']

# Example 5: Removing elements
fruits.remove("apple")
print(fruits)      # ['mango', 'cherry', 'orange']

# Example 6: Looping through a list
for fruit in fruits:
    print(fruit)

# Example 7: Mixed data types
mixed = [1, "hello", 3.14, True]
print(mixed)
