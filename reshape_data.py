# More data reshaping with pandas
import pandas as pd
import numpy as np
# pivoting from long to wide ie spread
data = pd.read_clipboard()
# save data
data.to_csv("test5.csv")

# Time series data
data.head()
data.columns = data.columns.str.replace(r'\\', 'm1')
data.head()
data = pd.DataFrame(data)
# drop missing values
data.dropna(inplace = True)
data
pd.PeriodIndex(year=data.year, quarter=data.quarter)
columns = pd.Index(['realgdp', 'realinv'], name='item')
data = data.reindex(columns = columns)
data.head()
# Periods to timestamp
# stack
# wide to long
# ie gather/melt
ldata = data.stack().reset_index().rename(columns= {0: 'value'})

# Dealing with data stored in relational databases like MySQL

# ie multi key data
ldata.columns
ldata.index

# assume item as the primary index
ldata[:10]

# pivot
# spread/dcast/cast
pivoted = ldata.pivot("level_0","item")
# multiple fill values
ldata['value2'] = np.random.randn(len(ldata))
ldata

pivoted = ldata.pivot("level_0","item")
pivoted[:3]
# Above is a Hierarchial column df
pivoted['value'][:4]
# pivot similar to creating a hierachial index with set_index and unstack

unstacked = ldata.set_index(['level_0','item']).unstack('item')
unstacked

# pivoting wide to long

# pandas.melt

# Merges multiple columns into one

df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})

df
# Perhaps key is a group indicator

melted = pd.melt(df, ["key"])
# key is a group indicator
melted

# using pivot to reshape back
reshaped = melted.pivot("key", "variable")

# specify a subset of columns to use as value columns

pd.melt(df, id_vars= ["key"], value_vars= ["A", "B"])

# use without grouping ie just melt

pd.melt(df)

pd.melt(df, value_vars= ['A', 'B', 'C'])

