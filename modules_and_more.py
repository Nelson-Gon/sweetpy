# Module
# A file with a script containing a long python program
# Definitions from other modules can be imported into the main module


def fib(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        print()



def fibo2(n):
    result = []
     a, b = 0,1
    while b < n:
    result.append(b)
    a, b = b, a+b
    return result

# Save the file as fibo.py and import fibo

# That didn't quite work out as expected but the idea holds.

from python_functions import extractor
a = [1, 2, 3]

extractor(a, 2,1)

[("Index:", i, "Element: ", j ) for i, j in enumerate(a)]

# Executing modules as scripts.

# Add the following script to replace __name__ with __main__
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

# The file can then be run as a script using
# python  mod_name arguments
# sys.argv[1] indicates that fib takes a single argument.
# Relates to  argc and argv from C++

# Module search path:
# Standard modules
import sys

# strangely ps1 and ps2 not found.
# This seems to be a bug as shown in issue https://bugs.python.org/issue7957

# The above was supposed to change >>>> to >C
# Cannot be recognised
# sys.path determines the interpreter's search path
# sys.path.append
# The above modifies the search path.
# dir() find which names a module defines
dir(sys)
import python_functions
dir()
# No arguments lists the names you have currently defined.
# Packages
# A package is a collection of modules.
# Create top package, sub package and add to sys.path
# Search is made along the path.
# To  treat as package requires __init__.py files
# import from x * requires a list named  __all__
# __path__ allows packages in multiple directories
# Output formatting
# fancier
s = 'Hello World'
# Can be printed with `str` or `repr`
import string
# repr returns canonical representation of a strinf
eval(repr(s))
# This seems to be similar to eval(parse(...)) from R
repr(s)
# eval(repr) returns the same print format as str
str(s)
# eval(repr()) dangerous like eval(parse())
repr((90, 35 , ('spam', 'eggs')))

# A simple way to write a table of squares and cubes
for x in range(1, 11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=" ")
    print(repr(x*x*x).rjust(4))

# Alternatively:
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

# str.format basic usage:
print('We are the {} who say "{}!"'.format('knights','Ni'))

# {} format fields
# number in brackets to refer to position
print('{0} and {1}'.format('spam','eggs'))
# Adf **keywd dict key-value pairs
print('This {food} is {adjective}.'.format(food='spam', adjective = 'horrendous'))

# colon and format  specifier
import math
print("The value of pi is approximately {0:.3f}".format(math.pi))

# More usage
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in  table.items():
    print('{0:10} ==> {1:10d}'.format(name,phone) )

# adding a digit represents how wide it should be( the character with, stw

# Old format
print("The value of pi is approximately %5.3f." % math.pi)