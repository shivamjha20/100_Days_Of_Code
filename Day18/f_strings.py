'''F-Strings in Python
Introduced in Python 3.6.
Stands for formatted string literals.
Allow you to embed expressions inside string constants using {}.
Start the string with the letter f or F.'''
# Example 1: Simple variable substitution
name = "Shivam"
age = 21
print(f"My name is {name} and I am {age} years old.")

# Example 2: Expressions inside f-strings
x = 5
y = 3
print(f"{x} + {y} = {x + y}")

# Example 3: Formatting numbers
pi = 3.14159
print(f"Value of pi: {pi:.2f}")   # rounds to 2 decimal places

# Example 4: Using functions inside f-strings
def greet(name):
    return f"Hello, {name}!"

print(greet("Shivam"))

# Example 5: Multi-line f-string
a, b = 10, 20
print(f"""
Values:
a = {a}
b = {b}
Sum = {a + b}
""")
'''👉 Key points:
Use f"..." and put variables or expressions inside {}.
Supports formatting (like decimals, alignment, padding).
Cleaner and faster than older methods like str.format() or
 % formatting.'''