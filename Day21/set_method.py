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

