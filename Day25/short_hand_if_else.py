# Example 1: Simple usage
x = 10
result = "Positive" if x > 0 else "Non-positive"
print(result)   # Positive

# Example 2: Even or odd
num = 7
parity = "Even" if num % 2 == 0 else "Odd"
print(parity)   # Odd

# Example 3: Inline assignment
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)   # Adult

# Example 4: Nested shorthand (not recommended for readability)
score = 85
grade = "A" if score >= 90 else "B" if score >= 75 else "C"
print(grade)   # B
