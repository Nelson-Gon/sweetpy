# data wrangling with pandas

# pandas, numpy, scipy -trio
# statsmodels, matplotlib.

import pandas as pd

from pandas import Series, DataFrame

# pandas data structures: an intro

# Series
# A 1d array-like object containing a sequence
# of values similar to NumPy's arrays
# data labels: indices(index)

# simplest Series

obj = pd.Series([4, 7, -5, 3])

obj

# the above prints a str repr of the Series
# index on the left, values on the right
# default index 0 to N-1 N=len(Series)
obj.values
obj.index

# create Series with userr-defined labels(index)

obj2 = pd.Series([4, 5, 6], index = ['a', 'b', 'c'])

obj2

# indices make selection easier unlike NumPy arrays

obj2['b']

obj2[obj2 >= 5]

obj2 * 2


import numpy as np
np.exp(obj2)

'b' in obj2

# Create a Series from a python dict

my_dict = {'a': 1, 'b': 2, 'c': 3}

pd.Series(my_dict)

# deafult index is dict keys in sorted order

# override by passing keys in user_defined order

my_keys = ['c', 'a', 'b']

pd.Series(my_dict, index = my_keys)

# NaN for missing values
# detect missingness with isnull and notnull


obj2[obj2.isnull()]

obj2[obj2.notnull()]

# Series and index have a name attribute
# attribute integrates other key areas of pandas
# functionality
obj2.name = 'test'
obj2.index.name = 'another_test'

# Series' index can be altred in-place by assignment

obj2.index = ["Hi", "This", "Test"]
obj2

# DataFrame

# rectangular table of data.
# ordered collection of columns, each with
# a different value type
# row and column indices(index)
# ie dict of Series sharing the same index.

# Constructing  a DataFrame

# from a dict of equal-length lists or Numpy arrays

data = {'state': ['Ohio', 'Nevada', 'Ohio', 'Nevada', 'Ohio','Nevada'],
        'year': [2000,  2001, 2002, 2003, 2002, 2002],
        'pop': [1.5, 1.7, 1.6, 1.5, 1.2, 1.6]}

frame = pd.DataFrame(data)
frame

frame.head()

# rearrange by specifying a sequence of columns

pd.DataFrame(data, columns= ['year', 'pop', 'state'])

# passing a column not in dict, appear as missing values

frame2 = pd.DataFrame(data, columns = ['year', 'pop', 'state','Notin'],
                      index = ['one', 'two', 'three', 'four', 'five', 'six'])

frame2

# retrieve rows by position using loc

frame2.loc['two']
frame2.loc['one']

# modify columns by assignment

frame2['pop'] = 16.5

frame2

frame2['pop'] = np.where(frame2.year==2002, 1, 0)
frame2

# working with nested dicts

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = pd.DataFrame(pop)
frame3

# Transpose with .T syntax

frame3.T
np.transpose(frame3)

# Index objects
# hold axis labels and other metadata ie attributes
obj = pd.Series(range(3), index= ['a', 'b', 'c'])
index = obj.index
index
index[1:]
# index objects are immmutable.
# cannot do this
index[1]="No way"
# enables sharing index objects among data structures.

labels = pd.Index(np.arange(3))
labels

obj2 = pd.Series([1.5, 2.3 , 5.6 ], index= labels)

obj2

# index also like fixed size sets

0 in obj2.index

'Test' in obj2.index

# pandas index can contain duplicate labels

dup_labels = pd.Index(['foo', 'bar', 'foo', 'bar'])

dup_labels


obj2

# essentials

# reindexing

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index = ['d', 'b', 'c', 'a'])

obj

# reindex with reindex

obj.reindex(obj.index.sort_values())

# The above is not in place

#  for ordered data like time series, do some interpolation
# eg ffill when reindexing
obj3 = pd.Series(['blue', 'purple', 'yellow'], index = [0,2, 4 ])

obj3

obj3.reindex(range(6), method = "ffill")

# reindex columns

obj4 = pd.DataFrame(obj3)
obj4.columns
obj4.rename(columns={0:'Col'})

# indexing, filtering and selection

obj = pd.Series(np.arange(4), index = ['a', 'b', 'c', 'd'])

# similar to numpy arrays
# can use index labels instead of the indices themselves

obj ['a']

obj[:4]

# slicing with labels, end point inclusive

obj['b':'c']

# Can set with slicing

obj['b': 'c'] = 5

data = pd.DataFrame(np.arange(16).reshape(4,4),
                    index = ['Ohio', 'Colorado',
                  'Utah', 'NewYork'],
                    columns= ['one', 'two', 'three', 'four'])


data

# select with label based slicing

data['two']
data
# select rows
data[:2]
data[:2] = np.where(data[:2] > 2, True, False)

data


# select multiple columns

data[['two', 'three']]


# selection with loc and iloc

data.index
data
# reshapes it(weirdly)

data.loc['Colorado',['one', 'two']]

# perfrom similar selections with iloc

data.iloc[2, [3, 0, 1]]


# index with labels

data.loc[:'Utah', 'two']

# transpose the above Series with pd.Series.transpose

data.loc[:'Colorado', ['four', 'three', 'two','one']].transpose()


# can also use .T


# data.to_dict()

# index with slices in addition to single labels or lists of labels

data.iloc[: , 3][data.three > 5]


# Integer indices


ser = pd.Series(np.arange(3.))

ser

ser[::-1]

ser2 = pd.Series(np.arange(3.), index= ['a', 'b', 'c'])

ser2[-1]

# loc and iloc

# loc for labels, iloc for integer(the i is for integer I guess labels)

ser.loc[:1]

ser.loc[:1]

# Arithmetic and data alignment

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index= ['a','c','d', 'e'])

s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1],
                index = ['a', 'c', 'e', 'f', 'g'])

s1

s2

# outer join on index labels

# ie when adding objects together, if any index pairs are not the same,
# the respective index in the result will be the union of the

# index pairs


[x for x in s1.index if x in s2.index]

# union is a c e

s1 + s2

# others  are filled with NaN ie outer join

# For a DataFrame, alignment is done on both rows and columns

df1 = pd.DataFrame(np.arange(9.).reshape(3, 3),
                   columns=list('bcd'),
                   index = ['Ohio', 'Colorado', 'Denver'])

df2 = pd.DataFrame(np.arange(12.).reshape(4, 3),
                   columns = list('bde'),
                   index= ['Utah','Texas', 'Oregon', 'Ohio'])

df2
df1

df1 + df2

# adding DataFrame objects with no column or row labels results in all nulls

df1 = pd.DataFrame({'A': [1, 2]})

df2 = pd.DataFrame({'B': [3, 4]})

df1 + df2

# filling with values

df1 = pd.DataFrame(np.arange(12.).reshape(3, 4),
                   columns=list('abcd'))

df2 = pd.DataFrame(np.arange(20.).reshape(4, 5),
                   columns=list('abcde'))

df2.loc[1, 'b'] = np.nan

df1
df2
# adding them results in NaN in non overlapping locations

df1 + df2

# Use add with a fill_value arg

df1.add(df2, fill_value = 0)


# Operations between DataFrame and Series

# Difference between a 2D array and its rows

arr = np.arange(12.).reshape(4, 3)

arr[0]

arr - arr[0]

# subtraction is done once for each row

frame = pd.DataFrame(np.arange(12.).reshape(4, 3),
                     columns= list('bde'),
                     index= ['Utah', 'Colorado', 'Texas', 'Oregon'])


series = frame.iloc[0]
frame

series

frame - series

# if no index value found in either df or ser, objects will be reindexed
# to form the union

series2 = pd.Series(np.arange(3), index= ['b', 'e', 'f'])

series2

frame + series2

# to broadcast over the columns, matching on the rows

# use arithmetic methods ie add, sub, pow, etc

series3 = frame['d']

frame

series3

# this sub is not sub sub but sub subtract
# This is matching rows(index)
# can also use axis numbers ie axis = 0 or axis = 1 for
# row and column respectively
frame.sub(series3, axis= 'index')

# mapping functions eg numpy's ufuncs

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                     index= ['Utah', 'Ohio', 'Texas', 'Oregon'])

frame


# find th absolute value

np.abs(frame)

# try using an arithmetic function
frame.abs()

# it actually works

# apply a lambda function to each column or row

f = lambda x: x.max() - x.min()

# good old apply

frame.apply(f, axis= 0)

# column wise

frame.apply(f, axis=1).transpose()

# apply not necessary, methods already defined

# Using a function that returns a Series

def f(x):
    return pd.Series([x.min(), x.max()], index= ['min', 'max'])

frame.apply(f, axis = 1)

# using element wise python functions too

# aim: format a string from a floating-point value in frame

# apply map to the rescue

format_1 = lambda x: '%.2f' % x

frame.applymap(format_1)

# sorting and ranking

obj = pd. Series(range(4), index = ['d', 'a', 'b', 'c'])

obj.sort_index()

# With a DataFrame, can sort by index on either axis

frame = pd.DataFrame(np.arange(8).reshape(2, 4),
                     index= ['three', 'one'],
                     columns=['d', 'a', 'b', 'c'] )


frame.sort_index(axis= 0, ascending= False).T

# sort a Series by its values
# use sort_values() method
# Missing values sorted to the end by default

obj = pd.Series([4, np.nan, -3, 2])

obj.sort_values()

# on a DataFrame, use the data in one or more columns as the sort key

frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})

frame.sort_values(by= "b", ascending= False)

# sort by multiple columns, provide a list

frame.sort_values(by= ['a', 'b'])

# Ranking assigns ranks fromone to len(data) in an array.

# default rank breaks ties by assigning each group a mean rank

obj = pd.Series([7, -5, 7, 4, 2, 0, 4])

obj.rank()

# ranking according to the order in which they're observed  in the data

obj.rank(method= 'first')

# above breaks ties by order of appearance

# assign ties the maximum value

obj.rank(method="max")

# available:average, min, max, dense, first

# dense == min except increases by 1 in between groups rather than
# the number of equal elements in a group

# Axis indices(Indexes) and dupes

obj = pd.Series(range(5), index = ['a', 'a', 'a', 'b', 'c'] )

obj

obj.index.is_unique
import  re
# re actually not needed
# in seems more like a grep
[x for x in dir(obj.index) if  'is_uniq' in x]

obj['a']


# applies to DataFrame indexing as well

df = pd.DataFrame(np.random.randn(4, 3), index= list('aabb'))

df

# use loc for labeled ie non int index as stated earlier

df.loc['b']


# summarizing anc computing descriptive stats

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                   index = ['a', 'b', 'c', 'd'],
                   columns = ['one', 'two'])

df

df.sum(axis = 1)

# NAs excluded unless the entire slice is NA. disable using skipna

df.mean(axis = 'columns', skipna= False)

# idmax and idmin return index values ie which.max()

df.idxmax(axis=0)

df.cumsum()

df.describe()

df.mad()

df.diff()


# correlation and covariance

# need pandas-datareader
#import pandas_datareader.data as web
# The above somehow fails

# can always learn that later

# unique values, value counts and membership

obj = pd.Series(['c', 'a', 'd','a', 'b', 'b'])

dir(obj)

uniques = obj.unique()

uniques.sort()

uniques

sorted(set(obj))

obj.value_counts() <=1

from itertools import compress

list(compress(obj, obj.value_counts() <=1 ))

# value_counts sort in descending order

pd.value_counts(obj.values, sort=False)

# isin performs vectorised set membershi checks

obj[obj.isin(['b', 'c'])]

# isin similar to Index.get_indexer

to_match = pd.Series(['c', 'b', 'a', 'c', 'a', 'b'])

unique_vals = pd.Series(['c', 'b', 'a'])

pd.Index(unique_vals).get_indexer(to_match)

