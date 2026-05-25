#pop() → Removes and returns an item (default last).
fruits = ["apple", "banana"]
fruits.pop()
print(fruits)   # ['apple', 'mango']

#clear() → Removes all items from the list.
fruits.clear()
print(fruits)   # []

#sort() → Sorts the list in ascending order.
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)   # [1, 2, 3, 4]

#reverse() → Reverses the list order.
numbers.reverse()
print(numbers)   # [4, 3, 2, 1]

#index() → Returns the index of the first occurrence.
nums = [10, 20, 30, 20]
print(nums.index(20))   # 1
