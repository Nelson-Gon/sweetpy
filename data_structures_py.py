# Data structures
# Still solely based on https://www.cse.unsw.edu.au/~en1811/python-docs/python-3.6.4-docs-pdf/tutorial.pdf
# With a few additions in and there.

# Lists
x = [1, 2, 3, 4]

# appending really does add to the end of a list.
x.append(34)
# Doesn't show(ie returns None, inplace appending.
# insert takes a postional argument and a value
x.insert(2, 45)
# Also inplace
x.extend([2, 3])
# extend requires an iterable
x.remove(2)
# removes first occurrence of an item in the list.
x.pop(2)
# Takes on an index
# x.clear() really does that.
x.index(2)
# Extraction via list.index
for elem in x:
    print(x.index(elem))

def extractor(my_list: list, *elem: int) -> int:
    """
    Return the index and count given a list.
    If several indices, returns the first index.
    :param my_list: A list
    :param elem: Integers(for now).
    """
    [[print("Element: ", elem,
            "Index: ", my_list.index(elem),
            "Count: ", my_list.count(elem),
            end="\n")
      for elem in elem]]


extractor(x, 34, 45, 2)

# sort does indeed sort the values.
x.sort()
x.reverse()
x.copy()
# x.copy similar to x[:]
x[:]

# Lists as stacks
stack = [2, 3, 4, 2,4]

stack.append(3)
extractor(stack, 2, 3, 4)

from collections import deque

# Using Lists as Queues
# dequeue creates a mutable sequence

queue = deque(["Eric", " John", "MIcheal"])
queue.append("Peter")
# popleft deletes from the left
queue.popleft()

# List comprehensions

squares = []
for x in range(10):
    squares.append(x**2)

squares

# Achieve the same with a one line comprehension

squares = []
[[squares.append(x**2) for x in range(20)]]

squares

# or simply
cubes = []

cubes = [x**3 for x in range(90)]

cubes

# Use map lambda

squares = list(map(lambda x: x**2, range(10)))

squares

# pasting with list comprehension

[(x, y) for x in [1, 2, 3]
 for y in [3, 1 , 4] if x != y]
x=[1,2,3]
extractor(x,3,2)

vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]
[x for x in vec if x>0]
[abs(x) for x in vec]

freshfruit = [' banana', ' loganberry ', 'passion fruit']

[weapon.strip() for weapon in freshfruit]

# strip removes white space.
# parens to form a tuple

[(x,x**2) for x in range(6)]

from math import pi

[str(round(pi,i)) for i in range(1,6)]

# Nested List comprehension

matrix = [[1, 2, 3, 4], [5, 6, 7, 8],
           [9, 10, 11, 12] ]
matrix
[[row[i] for row in matrix] for i in range(2)]

# transpose rows and columns
[[row[i] for row in matrix] for i in range(3)]
matrix

# del
a = [-1, 1, 66.25, 333, 1234.5]
del a[2]
a.pop(2)

# Tuples and sequences.

t = 12345, 54321, 'hello'

t[0]

# tuple: values separated by commas.

t

# prints with parens
# Immutable unlike lists
x = [1, 2, 3]
x[2] = 6

# Now try that with tuples
y = 123, 567, 'Hello tuple'

y[0] = 7

# zero / one item tuples requires parens and a trailing comma
empty = ()

singleton = 'hello',

len(empty)
len(singleton)
singleton

# tuple packing/ sequence unpacking
# packing
t = 123, '567', 'pacman'
# Sets
# unordered collection, no dupes
# membership tests, dupe elimination
# use {} . Empty set() not {}, {} creates an empty dict

basket = {'hi', 'I am', 'a', 'set', 'cannot', 'contain', 'a', 'dupe', 'set' }

basket
# Duplicates dropped

# Membership tests

'hi' in basket

90 in basket

a = set('abrcadabra')
b = set('alcazam')

# Set comprehensions, yay!
a = { x for x in 'abracadabra' if x not in 'abc' }

a

# Dictionaries
# Associative arrays or associative memories
# Indexed by keys, keys must be immutable eg str, int, etc
# Tuples as keys if they contain only strings, numbers or tuples.
# Mutable object containing tuples used directly or indirectly, not as keys
# Dict unordered key: value pairs set
# del deletes a pair
# Use sorted to sort sets and dicts.
sorted(b)

tel = {'jack': 890, 'sape': 897 }
tel['guido'] = 807
# Mutability
del tel['sape']
tel.pop('jack')
tel
tel['add_me'] = 8900
list(tel.keys())
'John' in tel.keys()
8900 in tel.values()

# dict builds dictionaries directly from sequences of key-value pairs.
dict([( 'sape', 567), ('guido', 890) ])

# dict comprehension to create dictionaries from arbitrary key-value expressions

{x: x**2 for x in (2,4,6)}

dict(sape=789, guido= 789, jack= 8970)
# easier for strings

# Looping techniques
# Use items to get the corresponding key-value pairs
knights = {'galland': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k, v)

# For a sequence, the position index and corresponding value can be got
# using enumerate
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

[print("Index: ", i, "Element:", v)
 for i, v in enumerate(x)]


# Looping over two or more sequences at the same time, use zip:

questions = ['name', 'quest', 'favorite', 'color']

answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}'.format(q, a))

# Looping in reverse
# Range really is seq(x,y,by)
for i in reversed(range(1,10,2)):
    print(i)

# loop on a sorted seq
basket = {'Hello', " I am ", "not ", "yet", "sorted"}
for f in sorted(basket, reverse=True):
    print(f)
# Space takes lead

# Avoid list changing, create a new list instead.
import math
raw_data = [56.2, float('NaN'), 54.8, 908.90,float('NaN')]

filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data


