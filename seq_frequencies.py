# find the most frequently occuring items
# in a sequence

words = ['look', 'into', 'eyes',
         'look', 'into', 'my', 'eyes',
         'the', 'eyes', 'the', 'eyes', 'the',
         'eyes', 'not', 'around', 'the', 'eyes']

from collections import Counter

word_counts = Counter(words)

word_counts.most_common(3)

# A from scratch implementation

res = dict((x, words.count(x)) for x in words)

res

# sort the dict by value

from operator import itemgetter

from collections import OrderedDict

res_2 = OrderedDict(sorted(res.items(), key=lambda k: k[1],
                           reverse=True))

res_2.keys()

# make an ordered list in one line

res_3 = OrderedDict((x, words.count(x)) for x in words)

sorted(res_3.items(), reverse=True, key=lambda x: x[1])

# groupby operations

from itertools import groupby

# Filtering sequence elements

lst = [1, 4, 4, 5, 6, 9, 89, 90]

[i for i in lst if i in [1, 4, 5]]

# exceptions, try catch

values = ['1', '2', '3', '5', 'N/A', '5']



def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


list(filter(is_int, values))

# Negation of functions

from functools import wraps


[x for x in list(map(is_int, values))
     if x is False]

# Without using map(logical indexing):

[v for v in values if not is_int(v)]

list(filter(is_int,values))

list(map(is_int, values))


[values[i] for i, y in enumerate(list(map(is_int,values))) if y is False]

# negate filter

list(filter(lambda x: not is_int(x), values))

# filtering with compress

from itertools import compress

counts = [0, 1, 2, 3, 4, 5]

[n>5 for n in counts]

list(compress(counts, [n < 5 for n in counts]))

# Key points

# Need to first make a sequence of booleans.

# compress filters True values

list(compress(values, list(map(lambda x: not
is_int(x), values))))

# compress takes boolean sequence



