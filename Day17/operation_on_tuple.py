#Indexing & Slicing:-Access elements by index, or slice ranges.
tup = (10, 20, 30, 40, 50)
print(tup[0])       # 10
print(tup[-1])      # 50
print(tup[1:4])     # (20, 30, 40)

#Concatenation:-Combine two tuples using +.
tup1 = (1, 2, 3)
tup2 = (4, 5)
result = tup1 + tup2
print(result)       # (1, 2, 3, 4, 5)

#Repetition:-Repeat elements using *.
tup = ("Hi",) * 3
print(tup)          # ('Hi', 'Hi', 'Hi')

#Membership Test:-Check if an element exists with in.
tup = (10, 20, 30)
print(20 in tup)    # True
print(40 in tup)    # False
