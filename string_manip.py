# manipulation of strings with pandas

import pandas as pd

import numpy as np

import re

# strings have builtin methods.
# regex support

val = 'a, b,   guido'

# split the above based on a comma

val.split(",")

# split plus strip

pieces = [ x.strip() for  x in val.split(",")]

# concatenate substrings with a two colon delimeter
# use +

first, second, third = pieces

# add two colon delimeter to concatenate them

'::'.join(pieces)

# locate substrings

'guido' in val

[val.index(x) for x in ['a', 'b']]

# 3 for b due to , and spaces

val.find('b')

# find vs index
# index raises an exception if th string isn't found
# find return s -1

val.index(':')

val.find(":")

# count occurrences of a string or pattern

len([val.find(x) for x in ['a', 'b']])


# use builtin
val.count(',')
sum([val.count(x) for x in ['a','b']])

# replacements

val.replace(",", ":")

# regex

text = 'foo bar\t baz \tqux'
# won;t work with builtin split
text.split('\s+')

# try with re.split

re.split('\s+', text)
# \t == \s+

# compiled regex
regex = re.compile('\s+')

regex.findall(text)

# to avoid escaping, use r, r for raw

# compiled regex saves CPU cycles.

text = "Dave dave@google.com" \
       " Steve steve@gmail.com" \
       " Rob rob@yahoo.com" \
       " Ryan ryan@gmail.com"

pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex= re.compile(pattern)

regex.findall(text)

# above fails, possible IDE issue. Point is compile


# vectorised string functions in pandas

data = {'Dave': 'dave@google.com',
        'Steve': 'steve@gmail.com',
        'Rob': 'rob@yahoo.com',
        'Wes': np.nan}

data = pd.Series(data)

data.isnull()

# use str methods on Series

data.str.contains("gmail")

pattern = '[a-zA-Z0-9]+@.*'

# use vectorized element retrieval

matches = data.str.match(pattern)

dir(matches).count('__bool__')

matches.dtypes

# str.get won't work with boolean

matches[0::2]

data.str.get(1)
data.str.isupper()
data.str.findall("^[A-Z]")
data.T.str.replace(r"@","No")
data.str.split("@")
