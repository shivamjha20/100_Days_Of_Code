'''A for loop is used to iterate over a sequence (like a list,
 tuple, string, or range). It runs the block of code once for
   each item in the sequence.'''
# Example 1: Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 2: Loop through a string
for char in "Python":
    print(char)

# Example 3: Using range()
for i in range(5):
    print(i)

# Example 4: Loop with start and end
for i in range(2, 6):
    print(i)

# Example 5: Loop with step
for i in range(0, 10, 2):
    print(i)
''' The range() function is especially useful with for loops:

range(n) → numbers from 0 to n-1

range(start, end) → numbers from start to end-1

range(start, end, step) → numbers with a step size'''