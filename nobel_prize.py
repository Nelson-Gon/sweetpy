# Looking at the basics of reading and writing files aka i/o

# Can use open(filename,mode ie rw or r+)
# Best used in conjuction with with to avoid the much harder to debug tr-catch blocks
# with open('file_name') as f:
#    read_data = f.read()

# Without with, manually close f with f.close
# Reading from another directory requires a relative path.
import os
# os has important tools, somehow changing the directory from the terminal won't work.
# Need to change directory with os tools
os.getcwd()

os.chdir('newpath')
# list all directories in cd
os.listdir(#null or relaive path)
with open('somefile.txt') as f:
    read_path = f.read()

f.closed
read_path
os.listdir()
f = open('somefile.txt')
f.closed
# read reads the entire file
f.read()
# readline reads the first line
f.readline()

for line in f:
    print(line, end= '')

# Read all lines with readlines
list(f)
os
f.closed
f.readline()
from os import read
# check that with really closes the file once done.

# read_path should return the file albeit in a funny way.
# Methods of file objects
# Taken from SO, lists as package modules.
import scipy
import pkgutil
package = scipy
for importer,  modname, ispkg in pkgutil.walk_packages(path=None, onerror =lambda x: None):
    print(modname)

# List for specific package:
for importer, modname, ispkg in pkgutil.walk_packages(path=package.__path__, prefix=package.__name__+'.' , onerror=lambda x: None):
    print(modname)

f = open('somefile.txt','r+')

# For some reason most os methods are not available, not even in the docs
# seek, realines and the like

# Dealing with json
# Deserialize: reconstruct data from str repr
# Serialize: make a str repr of the data
import json

json.dumps([1, 'simple', 'list'])

# dump dumps to  a text file
f.read()
json.dump({'Hi':'boy'},f)

# load decodes JSON

json.load(f)
import pickle
