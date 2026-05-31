#intersection() → Returns common elements.
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))   # {2, 3}

#difference() → Elements in one set but not the other.
a = {1, 2, 3}
b = {2, 3}
print(a.difference(b))   # {1}

#symmetric_difference() → Elements in either set but not both.
a = {1, 2, 3}
b = {3, 4}
print(a.symmetric_difference(b))   # {1, 2, 4}

'''issubset():-
->Checks if all elements of one set are present in another set.
->Returns True if the set is a subset, otherwise False.'''
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))   # True
print(b.issubset(a))   # False

'''issuperset():-
->Checks if a set contains all elements of another set.
->Returns True if the set is a superset, otherwise False.'''
a = {1, 2}
b = {1, 2, 3}
print(b.issuperset(a))   # True
print(a.issuperset(b))   # False

