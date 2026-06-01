'''isdisjoint():-
->Checks if two sets have no elements in common.
->Returns True if they are disjoint, otherwise False.'''
a = {1, 2}
b = {3, 4}
c = {2, 3}
print(a.isdisjoint(b))   # True (no common elements)
print(a.isdisjoint(c))   # False (2 is common)
