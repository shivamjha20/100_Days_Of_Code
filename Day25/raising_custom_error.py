'''Why Raise Custom Errors?
->Sometimes built‑in exceptions (ValueError, TypeError, etc.)
aren’t descriptive enough.
->You can define your own exception classes to make errors more
 meaningful in your program.
->This improves debugging and makes your code easier to understand.'''
# Example 1: Raising a built-in error manually
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("You tried dividing by zero!")
    return a / b

print(divide(10, 2))
# print(divide(10, 0))  # Raises ZeroDivisionError


# Example 2: Creating a custom exception
class NegativeNumberError(Exception):
    """Raised when a negative number is not allowed."""
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot take square root of a negative number.")
    return x ** 0.5

print(square_root(9))
# print(square_root(-4))  # Raises NegativeNumberError


# Example 3: Handling custom exception
try:
    result = square_root(-4)
except NegativeNumberError as e:
    print("Custom Error:", e)

'''Key Points
->Use raise to trigger an exception.
->Define custom exceptions by subclassing Exception.
->Always provide a clear error message.
->Handle them with try...except just like built-in errors.'''   
