'''Local Variables:-
Declared inside a function.
Exist only while the function runs.
Not accessible outside the function.'''
def demo():
    y = 5  # local variable
    print("Inside function:", y)

demo()
print("Outside function:", y)  # Error: y is not defined
