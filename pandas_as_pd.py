# Wes McKinney, pandas as pd
# Essential libraries: numpy, pandas, matplotlib
# scipy scikit-learn statsmodels(like R, yay!),
# seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels as sm

# A few jargons
# munge, wrandle: manipulation
# pseudocode : as usual
# syntactic sugar : syntax with no new features
# Generators
some_dict = {'a': 1, 'b' : 2, 'c' : 3, 'd': 4}

for key in some_dict:
    print(key)

[ k for k,v in some_dict.items()]

# using a generator to achieve the same
dict_iter = iter(some_dict)

list(dict_iter)

# An iterator is a python object that will yield objects when used in
# a for loop context.
# generator: concise way to construct a new iterator object
def squares(n=10):
    print("Generating squares from  1 to {0}".format(n**2))
    for i in range(1, n+1):
        yield i**2

# On first call of squares no code is executed first.
gen  = squares()

# rather a generator object is created.

gen

# proceed to request objects from the generator.

for x in gen:
    print(x, end= ' ')

# Writing generators with generator expressions

# similar to list, dict, set comprehensions
# uses () instead of []

gen  = (x** 2 for x in range(100))

gen

# similar to the more verbose:

def _make_gen():
    for x in range(100):
        yield x**2

gen = _make_gen()

list(gen)

dict((i, i**2) for i in range(5))

# itertools

# collection of generators for many common tasks

# groupby from itertools

import itertools

first_letter = lambda x: x[0]

names = ['Alan', 'Peter', 'Wes', 'Will', 'Albert']

# The key is a function computing a key value for each element.
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names)) #names a generator

# Errors and exceptions

float('1.2345')

def attempt_float(x):
    try:
        return float(x)
    except:
        raise TypeError


attempt_float('1.234')

attempt_float("Somestuff")

# use raise instead of return for a more meaninful error

# suppress ValueError
def attempt_float(x):
    try:
        return float(x)
    except ValueError:
        return x

attempt_float((1,2))

# catch multiple exception types by writing a tuple off exception types

def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x

attempt_float("Something")

# finally for files and the like

# Files and OS: the basics

path = '~/path_to_file/file.txt'

f = open(path)

# Defaults to r no rwx
# close explicitly with f.close()
# use with to make life easier

# Numpy basics: Arrays and vectorized computation

# Numpy: the num is for numerical, the py is for pie(not)

# common: ndarray: a multidimensional array for fast
# array oriented arithmetic
# Main focus: fast vectorized array operations for data munging and cleaning
# common array algorithms like sort, unique, set
# efficient stats andd aggregating/summarizing data
# data alignment and relational data manipulations
# if -elof
# group-wise operations
import numpy as np

my_array = np.arange(100)

my_list = list(range(100))

# Computational differences
import time

# = time.time()
start = time.time()
my_arr2 = my_array *2
end = time.time()

print(end-start)

start = time.time()

my_list = my_list * 2

end = time.time()
print(end-start)

# Numpy operations generally faster
#nd array : n dimension array
# np.random.randn : random floats
# random floats 2 * 3

data = np.random.rand(2,3)

data

data* 10

data + data

# nd array is a generic multi dimensional container
# for homogenous data
# shape, tuple showing arrays size(dim)
# dtype(data types).

data.shape

data.dtype

# Apparently understanding numpy is the path to a py guru

# creating ndarrays

data1 = [1, 2, 3, 4, 4, 5, 5]

# creating an ndarray from a sequence like object(arrays included)

arr1 = np.array(data1)

arr1

arr1.shape

# using nested sequences

data2 = [[1,2,3], [4, 5, 6]]

arr2 = np.array(data2)

arr2
arr2.shape
reshaped = arr2.reshape((3,2))
reshaped.shape
reshaped.ndim

# Numpy infers dtypes unless specified explicitly

arr1.dtype
arr2.dtype

# zeros, ones: 0s and 1s respectively

# empty creates an array with no initial values

np.zeros((2,3), dtype=np.int64)

# To create higher dimensional arrays, pass a tuple
# for the shape

np.zeros(shape= (5,2))

# arange is an array-valued version of the built-in
#c python range function.

np.arange(15)

arr1.astype(np.int32)
# convert an array of numeric strings to real numerics

numeric_strings = np.array(['1', '2', '3'], dtype=np.string_)

numeric_strings.astype(float)

# Arithmetic with numpy arrays

arr = np.array([[1., 2., 3.], [4., 5. , 6. ]])

arr * arr

# transpose

a = np.array([[2,4], [5,3]])
b = np.array([[3,6], [-1,9]])
a
b
b.transpose()
a * (b.transpose())

# Basic indexing and slicing

arr = np.arange(10)

arr[::2]
arr[::-1]
arr[1::2]

# higher dimensional arrays
# provide more variety

arr2d = np.array( [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr2d

arr2d[2]

arr2d[(1,2)]

arr2d[::-1]

 # odd slices
arr2d[1::2]

# even slices( zero included)

arr2d[::2]


# Assigning to slices

arr2d[:, :1] =0
arr2d[:, :1]


# Boolean indexing

names = np.array(["Bob", "Mary", "Will", "Jones"])

data = np.random.randn(4,4)

names
data
# Assumption: Each name corresponds to a row in the data

# Aim: Select all rows with the name Bob


names == "Bob"

# yields a boolean array

from itertools import compress

list(compress(data, names=="Bob"))

Or simply

data[names=="Mary", 1]

data[names !="Bob"]

# map purrr style
# except this is negation not a true map per se
data[~(names=="Bob")]


data[(names=="Bob") | (names =="Mary")]

# Fancy Indexing

arr = np.empty((8,4))

for i in range(8):
    arr[i] = i

arr

# subset rows in a particular order

arr[[0,2,4]]

arr[[-1,-3,-2]]


# transpose and swap axes

arr = np.arange(15).reshape((3,5))

arr

# inner product

arr = np.random.randn(6, 3)

arr

# transposing done with .T

np.dot(arr.T, arr)

# .T a special case of swapping axes.
# ndarray.swapaxes takes a pair of axis numbers
# and switches the indicated axes to rearrange the data

arr.shape
arr
arr.swapaxes(0,1)

# universal funcrtions: fast-elemntwise array functions

# a ufunc performs element-wise operations on data in
# ndarrays

arr = np.arange(10)

arr

np.sqrt(arr)

np.exp(arr)

# above are unary ufuncs
# others eg min max etc take on binary arrays
# binary ufuncs

x = np.random.rand(8)
y = np.random.randn(8)
x
y
np.maximum(x, y)

# The above is a parallel maximum
np.maximum.reduce((x,y))

