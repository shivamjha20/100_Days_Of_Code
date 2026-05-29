'''What is Recursion?
->Recursion is when a function calls itself to solve a problem.

->Useful for problems that can be broken down into smaller, similar
subproblems (like factorials, Fibonacci, or tree traversal).

->Every recursive function needs a base case (to stop recursion)
and a recursive case (where the function calls itself).'''

# Example 1: Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:                  # recursive case
        return n * factorial(n - 1)

print(factorial(5))   # 120


# Example 2: Fibonacci sequence using recursion
def fibonacci(n):
    if n <= 1:   # base case
        return n
    else:        # recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))   # 8


# Example 3: Sum of a list using recursion
def sum_list(lst):
    if not lst:   # base case: empty list
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4]))   # 10

'''
Key points:

->Always define a base case to avoid infinite recursion.

->Recursion can be elegant but sometimes less efficient than loops
(due to repeated calls and memory usage).

->Python has a recursion depth limit (default ~1000 calls).'''