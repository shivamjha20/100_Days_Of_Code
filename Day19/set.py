'''What is set?
->A set is a collection of unique, unordered elements.

->Defined using curly braces {} or the set() constructor.

->Sets are useful when you want to store items without duplicates
and perform mathematical set operations (union, intersection,
difference).'''

# Example 1: Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Example 2: Adding elements
fruits.add("orange")
print(fruits)

# Example 3: Removing elements
fruits.remove("banana")
print(fruits)

# Example 4: Checking membership
print("apple" in fruits)   # True
print("banana" in fruits)  # False

# Example 5: Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2)   # Union → {1, 2, 3, 4, 5, 6}
print(set1 & set2)   # Intersection → {3, 4}
print(set1 - set2)   # Difference → {1, 2}
print(set1 ^ set2)   # Symmetric Difference → {1, 2, 5, 6}
