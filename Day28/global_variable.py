'''Global Variables:-
Declared outside of any function.
Accessible throughout the program.
Can be read inside functions, but to modify them you must 
use the global keyword.
'''
x = 10  # global variable

def show():
    print("Inside function:", x)

show()
print("Outside function:", x)
