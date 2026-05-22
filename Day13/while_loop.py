'''A while loop runs as long as a condition is True.
It's useful when you don't know in advance how many times
you need to repeat something.'''
# Example 1: Simple while loop
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# Example 2: Using while with break
num = 1
while True:
    print(num)
    num += 1
    if num > 3:
        break   # stops the loop

# Example 3: Using while with continue
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue   # skips printing 3
    print(x)
