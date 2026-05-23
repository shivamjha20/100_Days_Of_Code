'''A function is a block of reusable code that performs a 
specifictask.

Defined using the def keyword.

Can take parameters (inputs).

Can return a value using return.

Helps make code modular, readable, and reusable.'''
# Example 1: Simple function
def greet():
    print("Hello, welcome to Python!")

greet()   # Calling the function


# Example 2: Function with parameters
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 3))   # 8


# Example 3: Function with default parameter
def greet_user(name="Guest"):
    print("Hello,", name)

greet_user("Shivam")   # Hello, Shivam
greet_user()           # Hello, Guest


# Example 4: Function returning multiple values
def calculate(a, b):
    return a + b, a - b, a * b

sum_val, diff_val, prod_val = calculate(10, 4)
print("Sum:", sum_val)
print("Difference:", diff_val)
print("Product:", prod_val)
