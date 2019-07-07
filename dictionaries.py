# default dictionaries help map multiple values to a key
# A dict is 1:1


d = {'a': [1, 2, 3], 'b': [4, 5, 6]}

# A default dict on the other hand does 1 to many or
# many to 1 mapping

from collections import defaultdict

d = defaultdict(list)

d['a'].append(2)
d['a'].append(3)

test = defaultdict(list)

[test['x'].append(x) for x in range(5)]

test.items()

test.keys()

# set won't allow dupes
# useful if you want to make remove dupes
test_2 = defaultdict(list)

test_2['b'].append([1, 2, 3])
test_2.items()

test_2.fromkeys(['price', 'shares'], [12, 14])

# default dict provides cleaner code apparently

d = defaultdict(list)

# for key, value in pairs:
#   d[key].append(value)

# Ordering dictionaries
# Problem: You need to control the order of items when
# iterating

from collections import OrderedDict

d = OrderedDict()

d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

[print(key, d[key]) for key in d]

import json

# ordered dict helps control order of items in
# the json file

json.dumps(d)

# Maths with dicts

prices = {'ACME': 45.23,
          'IBM': 456,
          'Apple': 5666666,
          'DELL': 123}

# need to zip
min(zip(prices.values(), prices.keys()))

# sort and zip

sorted(zip(prices.values(), prices.keys()))

# default dict processes keys, not values

print("The minimum key is {!r}".format(min(prices)))

# zip the items

min(zip(prices.items()))

# intersection  between dictionaries

a = {'a': [1, 2, 4],
     'b': [1, 2, 3, 4, 5, 6]}

b = {'a': [1, 2, 4], 'b': [1, 5, 6]}

a.keys() & b.keys()
[item for item in a.values() if  item in b.values()]

a.keys() - b.keys()

# Remove duplicates from a sequence while maintaining
# order

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 4, 5, 6, 6, 1,5 7, 8]

list(dedupe(a))

# For a non-hashable object

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3},
     {'x': 4, 'y': 5}]

list(dedupe(a, key= lambda d: d['x']))

# set doesn't preserve ordering


