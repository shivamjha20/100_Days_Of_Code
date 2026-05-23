#Positional Arguments:-Passed in order, matched by position.
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Shivam", 24)   # Hello Shivam, you are 24 years old.

'''Keyword Arguments:-Passed using the parameter name,
 order doesn’t matter.'''
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=24, name="Shivam")   # Hello Shivam, you are 24 years old.

#Default Arguments:-Provide default values if not specified.
def greet(name="Guest"):
    print("Hello", name)

greet("Shivam")   # Hello Shivam
greet()           # Hello Guest

'''Variable-Length Arguments (*args):-
Accepts multiple positional arguments as a tuple.'''
def add_numbers(*args):
    print(sum(args))

add_numbers(1, 2, 3, 4)   # 10
