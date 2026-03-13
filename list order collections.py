
#Lists — Ordered Collections
#Mutable & Ordered
#Lists are ordered, changeable collections that allow duplicates. Defined with square brackets [ ]. Can hold mixed types.
#🔍Accessing Elements
#Access by index (0-based), slice with [start:stop:step], iterate with for loop, or use list comprehensions.
#🛠️List Methods
#append(), insert(), remove(), pop(), sort(), reverse(), extend(), index(), count(), copy(), clear().


#===============================================
# Creating lists
nums = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1,2], [3,4], [5,6]]
empty = []

# Accessing
print(nums[0]) # 1
print(nums[-1]) # 5
print(nums[1:4]) # [2, 3, 4]
print(nested[1][0]) # 3

# Updating
nums[0] = 99
print(nums) # [99, 2, 3, 4, 5]

# Adding elements
nums.append(6) # add to end
nums.insert(0, 0) # add at index
nums.extend([7, 8]) # add multiple
print(nums)

# Removing elements
nums.remove(99) # remove by value
popped = nums.pop() # remove last
del nums[0] # remove by index
print(nums)

#======================================================
# Sorting
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort() # in-place
print(nums) # [1, 1, 2, 3, 4, 5, 6, 9]

nums.sort(reverse=True) # descending
print(nums) # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() returns new list
original = [3, 1, 4]
new = sorted(original)
print(original) # [3, 1, 4] (unchanged)

# Other methods
nums = [1, 2, 3, 2, 1]
print(nums.count(2)) # 2
print(nums.index(3)) # 2
nums.reverse()
print(nums) # [1, 2, 3, 2, 1]

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(squares) # [1, 4, 9, 16, 25]

# Filter with comprehension
evens = [x for x in range(10) if x%2==0]
print(evens) # [0, 2, 4, 6, 8]

# Unpacking
a, b, *rest = [1, 2, 3, 4, 5]
print(a, b, rest) # 1 2 [3, 4, 5]
#============================================================
Tuples — Immutable Sequences
Immutable
Once created, tuples cannot be changed. No adding, removing, or modifying elements. This makes them hashable and usable as dict keys.
⚡Faster than Lists
Tuples are more memory efficient and faster to iterate. Use them for fixed collections of data.
📦Packing & Unpacking
Easily pack values into a tuple and unpack them into variables. Great for returning multiple values from functions.
#=======================================================
# Creating tuples
point = (3, 4)
colors = ("red", "green", "blue")
single = (42,) # trailing comma needed!
from_list = tuple([1, 2, 3])

# Accessing (same as lists)
print(colors[0]) # red
print(colors[-1]) # blue
print(colors[0:2]) # ('red', 'green')

# Unpacking
x, y = point
print(f"x={x}, y={y}") # x=3, y=4

# Swap values
a, b = 10, 20
a, b = b, a
print(a, b) # 20 10

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last) # 1 [2,3,4] 5

# Cannot modify!
# point[0] = 5 → TypeError!
#==========================================================
# Tuple methods
nums = (1, 2, 3, 2, 4, 2)
print(nums.count(2)) # 3
print(nums.index(3)) # 2

# Concatenation & repetition
a = (1, 2)
b = (3, 4)
print(a + b) # (1, 2, 3, 4)
print(a * 3) # (1, 2, 1, 2, 1, 2)

# Length & membership
print(len(nums)) # 6
print(2 in nums) # True

# Tuples as dict keys (hashable)
locations = {
(0, 0): "Origin",
(1, 0): "East",
(0, 1): "North"
}
print(locations[(0, 0)]) # Origin

# Named tuples (better readability)
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y) # 3 4
#===========================================
Dictionaries — Key-Value Mapping
🔑Key-Value Pairs
Unordered (insertion-ordered since 3.7) collection of key:value pairs. Keys must be unique and hashable. Values can be any type.
⚡O(1) Lookup
Dictionary lookups are extremely fast (constant time). Use them when you need to map identifiers to data.
🔧Dict Methods
get(), keys(), values(), items(), update(), pop(), setdefault(), and dictionary comprehensions.
# Creating dicts
person = {
"name": "Alice",
"age": 25,
"skills": ["Python", "SQL"]
}

# Accessing values
print(person["name"]) # Alice
print(person.get("age")) # 25
print(person.get("job", "N/A")) # N/A (default)

# Modifying
person["age"] = 26 # update
person["job"] = "Engineer" # add new
del person["skills"] # delete

# Iterating
for key in person:
print(f"{key}: {person[key]}")

for key, value in person.items():
print(f"{key} → {value}")

# Keys & values
print(list(person.keys()))
print(list(person.values()))
#====================================================
# Dictionary methods
d = {"a": 1, "b": 2, "c": 3}

# pop — remove & return
val = d.pop("b")
print(val, d) # 2 {'a': 1, 'c': 3}

# update — merge dicts
d.update({"c": 30, "d": 4})
print(d) # {'a': 1, 'c': 30, 'd': 4}

# setdefault
d.setdefault("e", 5) # adds if missing
d.setdefault("a", 99) # keeps existing
print(d)

# Dict comprehension
squares = {x: x**2 for x in range(6)}
print(squares) # {0:0, 1:1, 2:4, ...}

# Nested dict
students = {
"s1": {"name": "Bob", "grade": "A"},
"s2": {"name": "Eve", "grade": "B"},
}
print(students["s1"]["name"]) # Bob

# Check existence
print("a" in d) # True
print(5 in d.values()) # True
#=========================================================
Sets — Unique Collections
Unique Elements
Sets automatically remove duplicates. Unordered, so no indexing. Elements must be hashable (immutable).
🔗Set Operations
Union (|), Intersection (&), Difference (-), Symmetric Difference (^) — just like mathematical sets.
⚡Fast Membership
O(1) lookup time for 'in' checks. Much faster than lists for large collections.
#========================================================# Creating sets
s = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3])
print(from_list) # {1, 2, 3}

# Adding & removing
s.add(6)
s.discard(1) # no error if missing
s.remove(2) # KeyError if missing
print(s) # {3, 4, 5, 6}

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b) # Union: {1,2,3,4,5,6}
print(a & b) # Intersection: {3,4}
print(a - b) # Difference: {1,2}
print(a ^ b) # Symmetric diff: {1,2,5,6}

# Subset & superset
print({1,2}.issubset(a)) # True
print(a.issuperset({1,2})) # True
#=============================================================

# Remove duplicates from a list
nums = [1, 3, 5, 3, 1, 7, 5, 9]
unique = list(set(nums))
print(unique) # [1, 3, 5, 7, 9]

# Find common elements
skills_a = {"Python", "SQL", "ML"}
skills_b = {"Python", "Java", "ML", "Cloud"}
common = skills_a & skills_b
print(common) # {'Python', 'ML'}

# Frozen set (immutable set)
fs = frozenset([1, 2, 3])
# fs.add(4) → AttributeError!

# Set comprehension
evens = {x for x in range(20) if x%2==0}
print(evens)

# Practical: count unique words
text = "the cat sat on the mat"
words = set(text.split())
print(f"{len(words)} unique words: {words}")
