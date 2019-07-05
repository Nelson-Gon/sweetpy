# Finding the largest or smallest N items.
# Use heapq
import heapq
# heapq useful for finding nlargest and nsmallest
# nlargest gets the largest n items and nsmallest the smallest
# n items.
nums = [1, 8, 2, 21, -5,-5,87, 43,2]
# object must be iterable
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(4, nums))
nums.sort(reverse= True)
print(heapq.nlargest(5, nums))

# For complex data structures, key argument useful
# akin to dplyr's top_n I guess.
portfolio = [{'name': 'IBM', 'shares': 100, 'price': 91.1},
             {'name' : 'AAPL', 'shares': 560,
              'price': 989,
              'name': 'YHOO', 'shares': 5000,
              'price': 890}]

type(portfolio)
# requires a lambda call in this case.
heapq.nsmallest(3, portfolio, key= lambda k: k['shares'])

# If N is smaller than the number of items, data is converted to a list
# first and items ordered as a heap eg
test = [1, 6, 6, 78, 90, 72, 33, 44, 5565, 666, 3223, 6665]
heap = list(test)
# heapify turns list into a heap
heapq.heapify(heap)
heap

# Features of a heap
# heap[0] always the smallest item.
# heappop  pops off the first item and replaces it with the next
# smallest item.
heapq.heappop(heap)
# First smallest is 1, next smallest should be 6.
heapq.heappop(heap)
# Next is 6 too
heapq.heappop(heap)
# Then next
heapq.heappop(heap)

# Calling it like so is not very efficient, try to automate.
for i in range(3):
    print(heapq.heappop(heap))

# Attempted automation to get the first three
# smallest numbers.
def last_n(my_list, n):
    """This returns the
    last_n values of a list"""
    import sys
    if 'heapq' in sys.modules:
        import heapq
        heaps = list(my_list)
        heapq.heapify(my_list)
        for i in range(n):
            print(heapq.heappop(heaps))


# nlargest and nsmallest for small number of items

heapq.nlargest(2, [1, 2, 3])

# merge similar to purrr/ plyr list merge
list(heapq.merge([1 , 2 , 3], [1, 2, 3], reverse=False))

# single smallest and single largest faster and easier found with
# min and max respectively.

# Implementing a priority queue
# Problem: Implement a queue that sorts items by a given priority
# and always returns the item with the highest priority on top.
# class that uses heapq to achieve the same.
class Priorityqueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue,
                       (-priority,self._index,item))

    def pop(self):
        return heapq.heappop(self._queue)[-1]



# The above in use:

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = Priorityqueue()

q.push(Item('foo'),1)
q.push(Item('bar'), 5)

q.pop()

# First pop returns item with highest priority
# heappop always returns the smallest item
# Above uses tuples of the form (-priority, index, item)
# - priority sorts from highest to lowest
# sample priority item tuple
# The r in  Item is a conversion flag.
# From the docs:
# !s calls str on value, !r calls repr !a calls ascii
'you are: {!r}'.format("cute")
# above calls repr
'you are: {!s}'.format("cute")

a = (1, 0, Item("foo"))
b = (2, 1, Item("bar"))
a > b
# returns false since 2>1, others never checked.

# mapping keys to multiple values in a dictionary

# Make a dict that maps keys to more than one value

d = {'a': [1, 2, 3], 'b': [4, 5, 6],
     'c': [7, 8, 9]}

# list vs set
# use a list if order preservation is necessary
# set to eliminate dupes
# defaultdict from collections can easily create a multidict
# feature of defaultdict:
# auto initializes first value to simplify appending

from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['b'].append(2)
d['b'].append(3)

d.items()

d= defaultdict(set)
d.items()
# add for append
d['a'].add(1)
d['a'].add(2)
d['b'].add(3)
d.items()
# No dupes, 2 is deleted.
