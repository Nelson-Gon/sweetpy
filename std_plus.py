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



