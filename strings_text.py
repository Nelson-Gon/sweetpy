# handling strings and text in python
# splitting strings on multiple delimiters
# good old split

line ='asdf fhshah; fgghga, gfh, fhgd, fgg,      foo'

import  re

fields = re.split(r'[;,\s]\s*', line)

# split takes any number of delimiters. splits for every match

values = fields[::2]

values

# caution regarding capture groups

fields = re.split(r'(;|,|\s)\s*', line)
# this also returns the delimiters.
fields

fields[::2]

# delimiters

fields[1::2]

# to remove separator characters in the result

re.split(r'(?:,|;|\s)\s*', line)

# The above uses a non capture group `?:`

# In essence, it captures and uses the delimiters
# but doesnot return them in the output.

re.split(r'(;|\s|,|;)\s*', line)

# vs this
re.split(r'(?:;|\s|,|;)\s*', line)

# Matching text at the start and end of a string

filename = 'test.txt'

filename.endswith(".txt")

# For multiple choices provide a tuple of possibilities
import os
filenames = os.listdir(".")

filenames
[name for name in filenames if name.startswith("hea")]
[name for name in filenames if 'class' in name]
all(name.endswith("py") for name in filenames)

[name for name in filenames if  re.match("cla.*|^hea",name)]

# re an overkill

# Matching strings with shell wildcard patterns

# fnmatch module

from fnmatch import fnmatch, fnmatchcase

fnmatch('foo.txt', 'txt.*')
fnmatch('foo.txt', 'foo*')

# searching for patterns and matching

text = 'yeah, but no, but yeah, but no, but yeah'

text == 'yeah'

text.find('yeah')
re.findall('yeah', text)

test2 = '11/02/2019'



# compile for repeated usage of a regex

datepat = re.compile(r'\d+/\d+/\d+')


# use compiled regex to test for match, split if match

if datepat.match(test2):
    print(re.split(r'/', test2))


datepat.findall(test2)

# regex with groups

matchme = re.compile(r'(\d+)/(\d+)')

matchme.groups

res = matchme.match(test2)

matchme.findall(test2)
matchme.match(test2).group(0)

datepat.findall(test2)

# search and replace

# sub

# using callback functions

from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


# find and replace case insensitive

text ='UPPER PYTHON, lower python, MixedD Python'

re.findall('python', text, flags=  re.IGNORECASE)

re.sub('python', 'snake', text, flags=re.IGNORECASE)

