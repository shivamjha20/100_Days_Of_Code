'''How for ... else Works?

->The else block runs only if the loop completes normally
(i.e., without hitting a break).

->If the loop is interrupted by a break, the else block is skipped.'''
# Example 1: Loop completes normally
for i in range(5):
    print(i)
else:
    print("Loop finished without break.")

# Example 2: Loop interrupted by break
for i in range(5):
    print(i)
    if i == 2:
        break
else:
    print("Loop finished without break.")  # skipped
