# cleaning data and preparation

# Missing data: NaN
# NaN is a sentinel value
import pandas as pd
import numpy as np
string_data = pd.Series(['awk','sed', 'grep', np.nan,'sub'])

string_data

string_data.isnull()

# pandas copies R to represent missing data as NA

# None is NA

string_data[0] = None

string_data.isnull()
# negate na with notnull
# fill na to fill with a number ffill or bfill

# dropna

# filtering out missing data

from numpy import nan as NA

data = pd.Series([1, NA, 3.5, NA, 7])

data.dropna()

# More complex with DataFrames
data = pd.DataFrame([[1., 6.,5., 4.], [1, NA, NA],
                     [NA, NA, NA], [NA, 6.5, 3.]])

data

cleaned = data.dropna()

cleaned

# control with how
# this all is equivalent to complete.cases
# is drop all rows with all NAs
data.dropna(how="all")

# drop columns by passing axis = 1

data.dropna(how="all", axis= 1)
# filter nas greater than 2
data[data.isnull().sum() >  2]

# filter out DataFrame rows with only a certain number
# of observations

df = pd.DataFrame(np.random.randn(7, 3))

df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
df

df.dropna(thresh= 2)

# filling in missing values

df.fillna("Missing")

# call fillna with a dict for different values per column

df.fillna({1:0.5, 2: 0})

# modify in place

_ = df.fillna(0, inplace= True)

# reindexing ca also be used to fillna

df = pd.DataFrame(np.random.randn(6, 3))

df.iloc[2: , 1] = NA
df.iloc[4:, 2] = NA
df

df.fillna(method= "ffill")

df.fillna(method= "bfill", limit= 2)

# replace with the mean

df.fillna(data.max())
df.fillna(data.apply(max))

#dit = {"Size": ["0", "0", "5mm", "12-15mm", "3mm-10mm"]}
#dt = pd.DataFrame(data=dit)
#dt["max_size"] = dt["Size"].str.replace(r".*-|mm$", "")

# data transformation

# Removing duplicates

data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 2, 1,1, 2,4,4]})

data

data.duplicated()

data.drop_duplicates()

# above considers all the columns
# specify a subset

data ['v1'] = range(7)

data.drop_duplicates(['k1'])

# defaults to keep first, keep last

data.drop_duplicates(['k1'], keep= 'last')

# Data transformation with func or map

data = pd.DataFrame({'food': ['bacon', 'pulled pork',
                              'bacon', 'corned beef', 'Bacon',
                              'pastrami', 'Pastrami', 'honey ham',
                              'nova lox'],
                     'ounces': [4, 3, 12, 4, 6.7, 8,3,5, 6]})

data

# aim add a column indicating the type of animal each food
# came from
meat_to_animal = {'bacon': 'pig',
                  'pulled pork': 'pig',
                  'pastrami': 'cow',
                  'honey ham': 'pig',
                  'nova lox': 'salmon'}

lowercased = data['food'].str.lower()

lowercased

data['animal']  = lowercased.map(meat_to_animal)

data

# pass a function that does all the work

data['food'].map(lambda x: meat_to_animal[x.lower()])
# key error

# replacing values

data = pd.Series([1., -999., -2, -999., -1000., 3. ])

# suppose -999 is supposed to be missing data

data.replace(-999, np.nan)

data.replace([-999, -1000], np.nan)

# can be a dict

# dt.replace differnt from data.str.replace on Series

# Renaming axis indexs

data = pd.DataFrame(np.arange(12).reshape(3, 4),
             index = ['Ohio', 'Chicago', 'New York'],
                    columns = ['one', 'two', 'three', 'four'])

transform = lambda x: x[:4].upper()

data.index.map(transform)
# assign to index hence modifying in place

# create a modified data set

data.rename(index=str.title, columns = str.upper)

# rename + dict

data.rename(index = {'Ohio': 'INDIANA'},
            columns = {'three': 'transformr'})

# Discretization and binning

ages = [20, 22, 25, 27, 21, 23, 31, 61, 31, 45, 12, 34, 89]

bins = [18, 25, 35, 60, 100]

cats = pd.cut(ages,bins, right= False)

cats
# Categorical Object(factor?)

cats.categories
cats.codes

pd.value_counts(cats)

# pass labels to bins
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']

pd.cut(ages, bins, labels= group_names)

# pass an integer number of bins

data = np.random.randn(20)

pd.cut(data, bins = 4, precision= 2)

# qcut bins based on sample quantiles

data = np.random.randn(1000) #random normal

cats = pd.qcut(data, 4) #cut into quartiles

cats


# pass own quartile numbers 0-1 inclusive

pd.qcut(data, [0, 0.1, 0.5, 0.9, 1], labels= ['one', 'two','three', 'four'])

# Detecting and filtering outliers

data = pd.DataFrame(np.random.randn(1000, 4))

data.describe()

# Aim find values in one of the values exceeding 3 in an
# absolute manner

col = data[2]

col[np.abs(col) > 3]

# select all rows having  a value exceeding 3 or -3

data[(np.abs(data) > 3). any(1)]

# set values based on these criteria

data[np.abs(data) > 3] = np.sign(data)* 3
data.describe()

# no.sign() produces 1 and -1 values based on whether the values
# in data are positive or negative

np.sign(data).head()

# permutation and random sampling

df = pd.DataFrame(np.arange(5* 4).reshape(5,4))
sampler = np.random.permutation(5)

sampler

df.take(sampler)

# select a random subset without replacement

df.sample(n=3)

# sample with replacement, replace = True

choices = pd.Series([5, 7, -1, 6, 4])

draws = choices.sample(n=10, replace= True)
draws

# Dummy Variables/ indicators

df = pd.DataFrame({'key':['b', 'b', 'a', 'c', 'a', 'b'],
                   'data1': range(6)})

df
pd.get_dummies(df['key'])
# to add a prefix to the dummies

dummies = pd.get_dummies(df['key'], prefix= "key")

df_with_dummy = df[['data1']].join(dummies)

df_with_dummy

# if  a row belongs to multiple catgories, more complex
# MovieLens 1M data set

mnames = ['movie_id', 'title', 'genres']

movies =pd.read_csv('movies.dat', sep= "::",
                      header=None,names= mnames)
movies.head()
movies.columns


all_genres = []

for x in movies.genres:
    all_genres.extend(x.split('|'))

genres = pd.unique(all_genres)
genres

# cosnstruct a zeros matrix
len(genres)
len(movies)
zero_matrix = np.zeros((len(movies), len(genres)))

dummies = pd.DataFrame(zero_matrix, columns= genres)
dummies.head()
