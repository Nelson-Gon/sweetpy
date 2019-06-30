# This is a brief tour of the standard library.
# os, an attempt at implementing the terminal

import os

os.getcwd()

'sweetpy' in os.listdir()

# Get the index of sweetpy in directories
# This is kinda pointless to do,
# merely a check.

for i, j in enumerate(os.listdir()):
    if j == "sweetpy":
        os.chdir(os.listdir()[i])

os.getcwd()

# Using shutil
# A daily file management tool.
import shutil
# Several useful functions.


# Glob
# Uses wildcards
import glob

# CL args
import sys
print(sys.argv)
# errors
sys.stderr.write("huh")
# Simply returns 3 while in a script.
# At the command line, returns the message too.
# ie returns 3 plus huh.
# String pattern matching
import re
re.findall(r'\bd[a-z]+', 'which day is it today')

'tea for too'.replace("too", "two")

# Maths

import math
math.copysign(-2, 5)
math.fabs(-2.5)

sign = lambda x: x if x>0 else{-x if x<0 else 0}

sign(-9.5)

# Random runif etc
import random
random.choice(['apple', 'pear', 'banana'])

# Sample with replacement

random.sample(range(10), 3)

random.random()
# seed sets state for the random float generator.
random.seed(a=2)

# For stats, got to statistics.
import statistics

from numpy import NaN
from numpy import isnan
seq = [1, 2, 3, 4, 5,NaN]

statistics.mean(seq)
 # The above returns nan as expected. How can we exclude
 # Nan values?
# Try to do it in a loop


seq_mod = seq[:]

for ind, val in enumerate(seq_mod):
    if isnan(val):
        del seq_mod[ind]

print(statistics.mean(seq_mod))


# The above works as expected, but is there a builtin?
# Don't reinvent the wheel, they  said.
# There is nanmean in scipy

from numpy import nanmean

nanmean(seq)

# Works as expected.
# Working online
# requests.
# urllib.requests retrieves data fromURLs
# smtplib sends mail
# This requires having https at the start,
# returns unknown url type otherwise.
from urllib.request import urlopen

with urlopen('http://harvard.edu') as response:
    for line in response:

        line = line.decode('utf-8')
        if 'Harvard' in line and 'Lab' in line:
            print(line)

# At time of writing, returned:
# Several decades in the making,
# the Harvard Microbiotics Lab’s Robobee made its first
# solo flight.      </div>

# Working with dates and time.
# datetime.
from datetime import date
to_day = date.today()
print("Today is ", to_day)

# Prettify
to_day.strftime("%A %B %d %Y")

test = "Thursday June"

re.sub(r"(Thur.*)(Jun.*)","\\2 \\1",test)

# The above does it but it is rather hard coded.

# do it with strftime
to_day.strftime("%B %A %Y")
# Not meaningful but does what is expected.
# Date compression.
import zlib
# gzip lzma bz2 tarfile
s = b'witch which has which witches wrist watch'

len(s)
# Now compress

compressed = zlib.compress(s)
len(compressed)

zlib.decompress(compressed)

# Perform a cyclic redundancy check. crc32
zlib.crc32(s)

# Compute speed

from timeit import Timer

Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()

# use pstats to find time critical sections.

# Quality Control.
# Write tests, test them with doctest

def avg(*values):
    '''Returns the mean of a list of values
    >>> print(avg(2,4,6))
    4.0
    '''

    return sum(values) / len(values)

import doctest

doctest.testmod()

# Tests passed, cool feature.

# Manually with unittest

import unittest

class TestStats(unittest.TestCase):

    def test_avg(self):
        self.assertEqual(avg(2,4,6),3)
        self.assertEqual(round(avg(2.5,4,6),1),4.2)
        with self.assertRaises(ZeroDivisionError):
            avg([])
        with self.assertRaises(TypeError):
            avg(34,"ty",89)


# called via CL
# unittest.main()

# Batteries included

# std extended
# Output formatting
# reprlib
import reprlib

reprlib.repr(set("supercaligragilisticexpialidocious"))

# repr provides an abbreviated display
# pprint
import pprint

t =[[["black", "cyan"], "white",
     ["green", "red"]], [["magenta",
                          "yellow"],
                         "blue "]]

pprint.pprint(t, width=30)

# textwrap

import textwrap

doc  = "The wrap() method is just like fill()" \
       "except that it returns a list of strings" \
       "instead of one big string with new lines to" \
       "separate the wrapped lines."

print(textwrap.fill(doc, width= 40))

print(textwrap.wrap(doc, width= 50))

# Access database of culture specific data formats with locale
# with locale

import locale

locale.setlocale(locale.LC_ALL,
                 "English_United States.1252")

["English_United States.1252" in locale.locale_alias.values()]

import re
my_regex = re.compile("en.*")
list(filter(my_regex.findall,
            locale.locale_alias.values()))

# locale.LC_ALL similar to unix LC_ALL and serves to override all
# other locale settings.
# default is C
# POSIX C alias
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
# Returns a mapping of conventions.
conventions = locale.localeconv()
x = 1234567.8

locale.format("%d", x, grouping= True)

# Format strings.

locale.format_string("%s.%f",
                     (conventions['currency_symbol'],
            conventions['frac_digits'],
                 x), grouping= True)

# Templating
# Template in string with a simplified syntax suitable for editing
# by end users. Allows app customization..

from string import Template

t = Template('${village}folk send $$10 to '
             '$cause.')

t.substitute(village= "Nottingham",
             cause = "the ditch fund")

sci = Template('${name} loves to code in ' 
               '$language.')
sci.substitute(name = "Nelson", language= "Python")

# safe_substitute to avoid key name error.

t = Template('Return the $item to the $owner')

d = dict(item = 'unladen swallow')

t.substitute(d)

# KeyError

# Override with safe_substitute
t.safe_substitute(d)

# subclasses can be used to set a custom delimiter for
# instance
import time, os.path

photo_files = ['img_01.jpg', 'img_02.jpg', 'img_03.jpg']

class BatchRename(Template):
    delimiter = "%"

fmt = input('Enter rename style '
            '(%d-date %n-seqnum %f-format): ')

t = BatchRename(fmt)

date = time.strftime("%d%b%y")
date

for i, filename in enumerate(photo_files):
     base, ext = os.path.splitext(filename)
     newname = t.substitute(d=date,
                            n =i, f=ext)
     print('{0} --> {1}'.format(filename,
                                 newname))

# Working with binary data record layouts.
# struct pack and unpack
# Multi threading, useful for I/O while running some other app
# in the background.

# Tools to work with lists.

from array import array

a = array('H', [4000, 10, 700, 22222])

sum(a)
a[1:3]

# collections
from collections import deque

d = deque(["task1", "task2","task3"])

d.append("task4")
d
print("Handling", d.popleft())
# pop is pop right.
d.pop()

import bisect
scores = [(100, 'perl'), (200, 'tcl') , (400, 'lua')]

#insort insert sort
bisect.insort(scores, (300, 'rust'))
scores
# locates the insertion point
bisect.bisect_left(scores, (100000, 'r'))
scores.insert(4,(100000, 'r'))

scores

# heapq implements heaps.

from heapq import heapify, heappop, heappush

data = [1, 3, 4, 5, 8, 9]
# Rearrange into heap order
heapify(data)
data
# git push heappush
heappush(data, -5)
# Fetch last three smallest entries.
[heappop(data) for i in range(3)]

# Decimal floating point arithmetic.
from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)
round(.70 * 1.05, 2)
getcontext().prec