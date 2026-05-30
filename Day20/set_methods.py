#add() → Adds a single element.
s = {1, 2}
s.add(3)
print(s)   # {1, 2, 3}

#update() → Adds multiple elements (from iterable).
s = {1, 2}
s.update([3, 4, 5])
print(s)   # {1, 2, 3, 4, 5}

#remove() → Removes an element (error if not found).
s = {1, 2, 3}
s.remove(2)
print(s)   # {1, 3}

#discard() → Removes an element (no error if not found).
s = {1, 2, 3}
s.discard(4)   # no error
print(s)       # {1, 2, 3}

#pop() → Removes and returns a random element.
s = {10, 20, 30}
print(s.pop())   # could be 10, 20, or 30
print(s)         # remaining elements

#clear() → Removes all elements.
s = {1, 2, 3}
s.clear()
print(s)   # set()

#copy() → Returns a shallow copy.
s = {1, 2, 3}
t = s.copy()
print(t)   # {1, 2, 3}
