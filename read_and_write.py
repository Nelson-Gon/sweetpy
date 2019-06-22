# import os to easily move to target directory
import os
import re
import io
os.getcwd()
os.chdir("..")
os.listdir()

# open a txt file for reading and writing
# https://docs.python.org/3/library/io.html
my_file = open('test.txt', 'r', encoding= "utf-8",
               newline= "\n")
my_file.readlines()
my_file.read(10)
# The above creates a text stream
# TextIOBase provides or overrides data attributes.
# encoding is encoding
# error for the decoder
# newlines
# read has a size parameter at most
# seek changes stream position to the given offset

with open('test.txt') as f:
    for line in f:
        print(line, end = "\n")

# This particular file had some spelling errors.
# Insert the word the wherever the error is.
with open('test.txt') as f:
    for line in f:
        print(re.sub('\s(?=\d+)',' the ',line))


my_file.tell()
my_file.seek(5)
my_file.seek(0,2)
