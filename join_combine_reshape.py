# Merging

# Hierarchial indexing
# allows multiple(toww or more) index levels
# on an axis
import pandas as pd
import numpy as np

data = pd.Series(np.random.randn(9),
                 index = [['a','a', 'a',
                           'b', 'b',

                           'c', 'c','d',
                           'd'],
                 [1,2 ,3 , 1, 3,
                  1, 2, 2,3]])

# np.repeat useful

dir(pd.options)
pd.options.display.max_rows = 5

data

# prints a simplified version of
# a Series with MultiIndex as index.
# partial indexing possible on hierarchically indexed
# objects
#pd.options.display.max_rows
data ['b']

data.index
# MultiIndexed
data

data.loc[:,2]

data.unstack().fillna("0")

data.unstack().stack()

# With a DataFrame, either axis can have a hierachial index.

frame = pd.DataFrame(np.arange(12).reshape(4,3),
                     index = [['a', 'b', 'b','b'],
                              [1, 2, 1,2 ]],
                     columns= [['Ohio', 'Chicago',
                                'Ohio'],
                               ['Green', 'Red',
                                'Blue']])

frame

# Give names to hierachial levels

frame.index.names = ['key1', 'key2']

frame.columns.names = ['state', 'color']

frame

# partial index

frame ['Ohio']


# Reordering and sorting levels

frame.swaplevel('key1', 'key2')

# sort_index sorts values ie alters values unlike above

frame.sort_index(level = 1)

frame.swaplevel(0, 1).sort_index(level = 0)

# Summary stats by level

frame.sum(level = 'key2')
# bad idea
#frame.apply(lambda x: [x.sum(level='key2'),
#            x.max(level='key1')])


# Index witha  DataFrame's columns

frame = pd.DataFrame({'a': range(7),
                      'b': range(7, 0, -1),
                      'c': ['one','one','one',
                            'two', 'two', 'two',
                            'two'],
              'd': [0, 1, 2, 0, 1, 2, 3]})

frame

# set_index

# creates a new DataFrame using one or more ofits columns
# as the index

frame2 = frame.set_index(['c', 'd'])

frame2.index

frame2

# to leave the columns in

frame.set_index(['c', 'd'], drop=False)
frame2

#pd.reset_option("display")

frame2

# Combine and merge data sets.

# pandas.merge
# connects rows in DataFrames based on one or more
# keys
# ie join
# db style DataFrame joins

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c'],
                    'data1': range(4)})


df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})

df2

# many to one join

pd.merge(df1, df2)

# specify joining columns

pd.merge(df1, df2, on ='key')

# same result, using on good practice

# if columns names are different,
#  specify right/left_on

df3 = pd.DataFrame({'lkey': ['b', 'b', 'a'],
 'data1': range(3)})

df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})

pd.merge(df3, df4, left_on='lkey',
         right_on='rkey')

# outer, inner, left

pd.merge(df1, df2, how= "inner")
pd.merge(df1, df2, how="outer")
df1

# many to many merges

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c',
                    'a', 'b'],
                    'data1': range(6)})

df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b',
                            'd'],
                    'data2': range(5)})

df1

df2

pd.merge(df1, df2, on = 'key', how= 'left')

# many to many form Cartesian product of the rows

# ie 3 X 2 = 6 bs
# for inner joins

pd.merge(df1, df2, on='key', how = 'inner')


# overlapping column names. suffix

# merge on index

left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a',
                              'b', 'c'],
                      'value': range(6)})

right1 = pd.DataFrame({'group_val': [3.5, 7]},
                      index= ['a', 'b'])

left1

right1

pd.merge(left1, right1, left_on="key", right_index=True)

# defaults to an intersection
# can form a union with outer
# set how = "outer"

