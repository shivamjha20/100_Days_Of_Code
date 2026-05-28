'''A docstring (documentation string) is a special string used
 to describe a function, class, or module.

Written inside triple quotes just below the definition line.

Can be accessed using the built-in .__doc__ attribute or the
 help() function.

Helps explain what the code does, making it easier to understand
 and maintain.'''
# Example 1: Function docstring
def add(a, b):
    """
    This function takes two numbers
    and returns their sum.
    """
    return a + b

print(add.__doc__)   # Access docstring
print(add(5, 3))


# Example 2: Class docstring
class Person:
    """
    A simple class to represent a person.
    Attributes:
        name (str): The person's name
        age (int): The person's age
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Example 3: Module-level docstring
"""
This module demonstrates the use of docstrings
in Python for functions, classes, and modules.
"""
