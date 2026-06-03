'''What is Exception Handling?
->Exceptions are errors that occur during program execution.
->Without handling, they stop the program.
->Python provides try...except blocks to catch and handle exceptions
gracefully.
->You can also use else and finally for more control.'''
# Example 1: Basic try-except
try:
    x = 10 / 0   # division by zero
except ZeroDivisionError:
    print("You cannot divide by zero!")

# Example 2: Multiple exceptions
try:
    num = int("abc")   # invalid conversion
except ValueError:
    print("Invalid number format!")
except TypeError:
    print("Type error occurred!")

# Example 3: Catching all exceptions
try:
    lst = [1, 2, 3]
    print(lst[5])   # index out of range
except Exception as e:
    print("Error:", e)

# Example 4: Using else
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division error!")
else:
    print("Division successful:", result)

# Example 5: Using finally
try:
    f = open("test.txt", "w")
    f.write("Hello")
except Exception as e:
    print("Error:", e)
finally:
    f.close()
    print("File closed safely.")
