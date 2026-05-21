'''if–else:-
The if–else statement lets you execute code based on conditions.
if → runs when the condition is True.
else → runs when the condition is False.
You can also use elif (else if) for multiple conditions.'''
# Example 1: Basic if-else
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# Example 2: if-elif-else
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
else:
    print("Grade: C")

# Example 3: Nested if
num = -3
if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")
