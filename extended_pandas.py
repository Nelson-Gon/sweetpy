import numpy as np
import pandas as pd
# reading and writing data
# read_csv, read_table for \t, read_fwf
# read_clipboard
# read_excel
# read_json/html/pickle, etc

# arguments
# indexing
# type inference and data conversion
# datetime parsing
# iterating
df = pd.read_csv("test.csv")

df

# to read without the header, set header to None ofc

df = pd.read_csv("test.csv", header = None)

df

# set custom names

pd.read_csv("test.csv", names= ['this', 'is', 'a', 'test'])

# set message column as the index

names = ['a', 'b', 'c', 'd', 'message']

pd.read_csv('test.csv', names= names, index_col= 'message')

# Missing data handling

res = pd.read_csv("test.csv")

pd.isnull(res)

pd.DataFrame(np.where(pd.isnull(res), "Yes", "No"))

# na_values option takes a list or set of strings

res = pd.read_csv("test.csv", na_values= ['NULL'])
res

# specify different NAs values for each column in a dict

sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
res

pd.read_csv("test.csv", na_values= sentinels)

# read text files in pieces

pd.options.display.max_rows = 10

result = pd.read_csv("test.csv")

result

# read only a small number of rows

pd.read_csv("test.csv", nrows= 4)

# to read a file in pieces, set a chunksize as number of rows

pd.read_csv("test.csv", chunksize= 5)

# The above returns a TextFileReader that can be iterated over

chunker = pd.read_csv("test.csv", chunksize= 5)

tot = pd.Series([])


for piece in chunker:
    tot = tot.add(piece['message'].value_counts(), fill_value = 0)

tot = tot.sort_values(ascending=False)

tot

# writing data to text format

data = pd.read_csv("test.csv", nrows = 5)

data.loc[2:3,"message"] = "hello"

data.loc[:1,"message"] = np.nan

data
 # write to csv

 data.to_csv('test2.csv')

# use other delimeters

import sys

# use stdout to print to console
data.to_csv(sys.stdout, sep=":")

# missing values appear empty above

# set them to some other sentinel value

data.to_csv(sys.stdout, na_rep= np.nan)

# to prevent rows being written , index = False

data.to_csv(sys.stdout, sep=":",
            index= False, na_rep= "NULL",
            columns = list('abcde'))


# Series has that method too

# working with delimited files

import csv

f = open('sample.csv')

reader = csv.reader(f)

for line in reader:
    print(line)

with open("sample.csv") as f:
    lines = list(csv.reader(f))


header, values = lines[0], lines[1:]

header
values

data_dict = {h:v for h, v in zip(header, values)}

data_dict

# interact with apis

import requests


url = 'https://api.github.com/repos/pandas-dev/pandas/issues'

resp = requests.get(url)

resp

# json method returns a dict containing parsed json

data = resp.json()

data[0]['title']

issues = pd.DataFrame(data, columns= ['number', 'title', 'labels', 'state'])

issues[issues['state'] == 'closed']
# all open

# interact with dbs

import sqlite3

