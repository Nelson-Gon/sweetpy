# handling strings and text in python
# splitting strings on multiple delimiters
# good old split

line ='asdf fhshah; fgghga, gfh, fhgd, fgg,      foo'

import  re

fields = re.split(r'[;,\s]\s*', line)

# split takes any number of delimiters. splits for every match

values = fields[::2]

values

# caution regarding capture groups

fields = re.split(r'(;|,|\s)\s*', line)
# this also returns the delimiters.
fields

fields[::2]

# delimiters

fields[1::2]

# to remove separator characters in the result

re.split(r'(?:,|;|\s)\s*', line)

# The above uses a non capture group `?:`

# In essence, it captures and uses the delimiters
# but doesnot return them in the output.

re.split(r'(;|\s|,|;)\s*', line)

# vs this
re.split(r'(?:;|\s|,|;)\s*', line)

# Matching text at the start and end of a string

filename = 'test.txt'

filename.endswith(".txt")

# For multiple choices provide a tuple of possibilities
import os
filenames = os.listdir(".")

filenames
[name for name in filenames if name.startswith("hea")]
[name for name in filenames if 'class' in name]
all(name.endswith("py") for name in filenames)

[name for name in filenames if  re.match("cla.*|^hea",name)]

# re an overkill

# Matching strings with shell wildcard patterns

# fnmatch module

from fnmatch import fnmatch, fnmatchcase

fnmatch('foo.txt', 'txt.*')
fnmatch('foo.txt', 'foo*')

# searching for patterns and matching

text = 'yeah, but no, but yeah, but no, but yeah'

text == 'yeah'

text.find('yeah')
re.findall('yeah', text)

test2 = '11/02/2019'



# compile for repeated usage of a regex

datepat = re.compile(r'\d+/\d+/\d+')


# use compiled regex to test for match, split if match

if datepat.match(test2):
    print(re.split(r'/', test2))


datepat.findall(test2)

# regex with groups

matchme = re.compile(r'(\d+)/(\d+)')

matchme.groups

res = matchme.match(test2)

matchme.findall(test2)
matchme.match(test2).group(0)

datepat.findall(test2)

# search and replace

# sub

# using callback functions

from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


# find and replace case insensitive

text ='UPPER PYTHON, lower python, MixedD Python'

re.findall('python', text, flags=  re.IGNORECASE)

re.sub('python', 'snake', text, flags=re.IGNORECASE)

# Specifying a regex of the shortest match

# Aim find shortest possible
str_pat = re.compile(r'\"(.*)\"')

text1 = 'Computer says "no."'
str_pat.findall(text1)

text2 = 'Computer says "no." Phone says "yes."'

str_pat.findall(text2)

# * greedy, add ? to match exact ie make it non greedy

str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2)

# Multiline regex

# Typical usage when using regex involving dot(.)

# dot matches anything but a new line
# Matching C style comments
comment = re.compile(r'/\*(.*?)\*/')

text1 = '/* This is a comment */'
text2 = '''/* This is a 
 multiline comment */'''

comment.findall(text1)
comment.findall(text2)
# Fails to match text2

# Use a non capture group
comment = re.compile(r'/\*((?:.| \n)*?)\*/')
comment.findall(text2)

# Normalize Unicode Text to  std repr
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

s1
s2
# s1 U + 00F1
# s2 U + 0303

# import unicodedata
import unicodedata

t1 = unicodedata.normalize("NFC", s1)
t2 = unicodedata.normalize("NFC", s2)
t1
t2

print(ascii(t1))
# More like iconv
# NFC and NFD
# Unicode meets regex
num =  re.compile('\d+')
# ascii digits
num.match('123')
# arabic
num.match('\u0661\u0662\u0663')

# strip unwanted charcaters from strings
s = ' hello world \n'
s
# lstrip removes leading white space
s.lstrip()
# lagging whitespace removed

s.rstrip()

t = '---hello====='

t.lstrip('-')
t.rstrip("=")
t.strip("=-")

# Use replace to remove white space in the middle

s = ' hello       world    \n'

s.strip()
s.replace('\s+','')
# terrible regex to achieve the same
re.sub('\s(?=\s)|^\s|\n+','',s)
re.sub('\s+','',s)
s
re.sub('\s(?=\s)|\s(?<=\w)|\n','',s)

# sanitizing and cleaning up text
script_kiddie = 'pýtĥöñ'
script_kiddie
# normalise with data.normalise

# use str.translate

s = 'pýtĥöñ\fis\tawesome\r\n'
s
# Make a translation table
# ord returns unicode for a character string
remap = {ord('\t'): ' ',
         ord('\f'): ' ',
         ord('\r'): None
}

a = s.translate(remap)
a
# None equivalent to NULL?
# Building bigger tables
import sys
cmb_chrs = dict.fromkeys(c
        for c in range(sys.maxunicode)
                if unicodedata.combining(chr(c)))

cmb_chrs
b = unicodedata.normalize("NFD", a)
b.translate(cmb_chrs)

# text alignment

text = 'Hello World'

text.ljust(20)
text.rjust(20)
text.center(15,"=")
#fill character accepted
text.rjust(12,"*")
format(text, '>20')
format(text, '<20')
format(text, '^20')
format(text, '=^20')

'{:>10s} {:>10s}'.format('Hello', "World")

format(1.23345, '>10.2f')

# string concantentation

parts = ['Is', 'Chicago', 'Not', 'Chicago?']

''.join(parts)
','.join(parts)
' '.join(parts)
"  ".join(parts)
# use +
print('{} {}'.format("Is Chicago","Not Chicago?"))
# + inefficient memory wise
data = ["IBM", 50, 190]
','.join(repr(d) for d in data)

print(1,2,3,sep=":")
