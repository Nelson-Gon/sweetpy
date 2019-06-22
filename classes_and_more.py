# instantiate


def __init__(self):
    self.data = []


# The above defines a special class limited method ir data is a list.


class MyClass:
    '''A basic class.'''
    i = 12345

    def func(self):
        return "Hello.World"


y = MyClass()

# This creates a new instance of the class
y


# When an __init__ method is defined, instantiation immediately
# invokes the __init__ method


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(4, -6.5)

x.r, x.i

# Instance objects

# Instance objects understand attribute refs

# Two kinds of attributes, methods and data
# data attr are instance vars in Small talk, members in c++(hello old friend)
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2

print(x.counter)

del x.counter
hasattr(x, "counter")
getattr(x, "r")

# Methods
# Function part of a class.
y.func()


# Class and Instance Variables

class Dog:
    kind = 'canine'  # shared by all instances

    def __init__(self, name):
        self.name = name  # unique to each instance


d = Dog('Peter')

d.kind
d.name


class Cat:
    kind = 'Garfield'

    def __init__(self, name):
        """

        :type name: str
        """
        self.name = name
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)


# Create some cat named Sully with some funny trick

Sully = Cat('sully')
Sully.name

Sully.add_tricks("fancy trick here")

hasattr(Sully, "add_tricks")

Sully.add_tricks("Has nothing else")
Sully.tricks

# Inheritance
# Template
# Class DerivedClassName(BaseClassName)

# check inheritance with isubclass
issubclass(float, int)

issubclass(Cat, Dog)


# Inherit new dogs from dog and cat

class NewDog(Cat):
    def __init__(self, name, family):
        Cat.__init__(self, name)
        self.family = family


Sonny = NewDog(family="Ratus", name="Sonny")

Sonny.add_tricks("Hello")


# Cannot inherit all attributes though, weird
# Inherits kind but not name
# super calls NextMethod(yay!)

class Test:
    def __init__(self):
        print("Class Test")


class Test2(Test):
    def __init__(self):
        print("Class Test2")
        super().__init__()


B = Test2()


# try that wit some implementation.

class Student:
    def __init__(self, name):
        self.name = name


class Students(Student):
    def __init__(self, name, gpa):
        Student.__init__(self, name)
        self.gpa = gpa


# The above works, using super is a bit tricky(for now).

Students(gpa=3.2, name="Boy")

# Private variables

# No privates
# Use an _(underscore)
# _ implies non-public part of an API

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update #private copy of iterable



class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__
        for item in zip(key, values):
            self.items_list.append(item)

# Iterators
# for calls iter
s = 'abc'
it = iter(s)
it

# for calls next as shown below
next(it)
next(it)
next(it)
next(it) # No more elements raise StopIteration error

# User defined iterator

class Reverse:
    """ Iterator for looping over a seq backwards"""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]


reve = Reverse('spam')

iter(reve)
for char in reve:
    print(char)

# Generators

# Use yield to return data
# Whenever next is called, generator resumes where it left of(memory cells)

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

# generators auto create iter and next methods
# Generator expressions
# Less versatile
sum(i*i for i in range(10))

data = 'golf'

[data[i] for i in range(len(data)-1,-1,-1)]
