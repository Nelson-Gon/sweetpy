# virtual envs
# virtual environments enable one to circumvent issues with
# having to use different versions of the same package due to
# library dependencies differing.
# venv: a self contain directory with a py installation of
# a particular version python version.
# venv creates virtual environments.
# creating a venv
# at the terminal:
# python3 -m venv my-env
# activate the venv:
# source my-env/bin/activate
# pip installs packages from pypi
# pip search good for finding models

# Data Structures python cookbook 3rd edition
# Unpacking a sequence into separate variables.

# Problem: N element tuple to be unpacked into a collection of N variables.


p = (4, 5)

# Solution
# Requires that the number of variables and struct match the
# sequence
x, y = p

x

y

data = ["ACME", 50, 91.1, (2012, 12, 4)]

name , sales, price , date = data

name
sales

# Unpacking general, not just tuples or lists. As long as
# object is iterable, can be unpacked.

s = 'Hello'

# rpy2 to use r

len(s)

a, b, c, d, e =s

a

# Unpack and discard.
# Uses the special case _

_, shares, price, _ = data


# Unpacking N elements from an iterable with arbitrary
# length.

# Use star expressions
# Eg drop first and last hw grades
import math

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

# Similar to keywrd args and args

# User records consist of name and email address followed bu arbitrary
# number of phone numbers. Unpack as so:

record = ('Dave', 'dave@example.com', '999-911-233', '678-898-778')

name, email, *phone_numbers = record

name


email

phone_numbers

# Extended iterable unpacking

records = [('foo', 1, 2), ('bar', 'hello',),
           ('foo', 3, 4)]




def do_foo(x,y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag =='foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# Using *args with splitting.

line = 'nobody:*:-2:-2:unprivileged User:/var/empty:' \
       '/usr/bin/false'

uname, *fields, homedir, sh = line.split(':')

uname
fields
homedir
sh

# star unpacking meets list processing

items = [1, 2, 3, 4, 5, 6]

head, *tail = items
head

tail

# what if I set both to *
# Not allowed
# Algorithm behind this is somewhat confusing imho

#*head, *tail =items

head, *middle, tail =items


head
tail
middle

# It seems each non star element takes at most
# one element.

# Recursion with iterable unpacking.

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

sum(items)
items

# Python has an inherent recursion limit.

# Keeping the last n terms.

# collections.deque keeps a limited history

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
            previous_lines.append(line)


if __name__ == '__main__':
    with open('test.txt') as f:
        for line, prevlines in search(f,'this', 5):
            for pline in prevlines:
                print(pline, end="")
            print(line, end="")
            print("-"*20)


# Generator function uses yield

# deque(maxlen=) creates a fixed sized queue.
# New items are added and queue is full, old items
# are auto removed.

q = deque(maxlen=3)
q

q.append(2)

q.append(3)
q.append(4)
# 4 is dropped, oldest dropped.
q.append(5)
q

# In general, useful when unbounded eg

p = deque()

p.append(4)
p.append((1,2))

p.append(2)
p
p.popleft()
p.appendleft(4)
p

# Finding the largest or smallest N items in a collection.

import heapq
