import datetime
print("These exercises are based on https://pynative.com/python-data-structure-exercise-for-beginners/ as of ",
      datetime.datetime.now())
# Actually today is 18/06/2019. :)

# Given two lists, create a third list by picking an
# odd- index element from the first list and an even index element from the second.

list_one = [3, 6, 9, 12, 15, 18, 21]
list_two = [4, 8, 12, 16, 20, 24, 28]

filtered_list = []
for i in list_one:
    if list_one.index(i) % 2 != 0:
        filtered_list.append(i)
for j in list_two:
    if list_two.index(j) % 2 == 0:
                filtered_list.append(j)


filtered_list

# Solution from website:
list_three = list()

# This gets elements at odd indices from list one.
res_3 = list_one[1::2]
# The above goes from 1 to the end of the array by two steps.
# Example of such a usage
# test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# test[1:]
# Now add a step
# test[1::2]
# test[1::1]

# test[0::2]
# This gets elements at even indices from list two. Erroneously referred to as odd indices on the site.

res_2 = list_two[0::2]

# Create an empty list
res = []
res.extend(res_2)
res.extend(res_3)
res
# Compare with filtered list
filtered_list.sort(reverse=True)
sorted(filtered_list)
sorted(res)
# To check if they are equal more programmatically
if  res.sort() == filtered_list.sort():
    print("Both solutions yield the same result")

# Question 2.
# Given an input list, remove elements at index 4 and
# add it to position 2 plus end of list.
# The answer given on the site is actually wrong.
# The site assumes indexing from 1 yet indexing starts from 0 in python.
test_list = [54, 44, 27, 79, 91, 41]

# Use a for loop
# This might be computationally expensive.
# test_list[:]

modified_list = test_list[:]
for elem in test_list:
    if test_list.index(elem) == 4:
       modified_list.pop(test_list.index(elem))
       modified_list.insert(2,elem)
       modified_list.insert(len(modified_list),elem)

modified_list

# Using enumerate
mod_list = test_list[:]
for i, j in enumerate(mod_list):
    if i == 4:
        del mod_list[i]
        mod_list.insert(2, j)
        mod_list.insert(len(mod_list), j)

mod_list

if mod_list == modified_list:
    print("Same result withe either method")

mod_list

# The answer on the site was wrong.

# Question 3.
# Given a list, slice it into three equal chunks
# and reverse each list.

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a_list

# This copied and pasted from https://pythonprinciples.com/ask/how-do-you-split-up-a-list-into-chunks-of-the-same-size/
# Mainly for learning purposes
def chunks(l, chunk_size):
    res = []
    chunk = []
    for item in l:
        chunk.append(item)
        if len(chunk) == chunk_size:
            res.append(chunk)
            chunk = []
    # returns remainders
    if chunk:
        res.append(chunk)
    return res

chunks(a_list, 2)

# Question 5, iterate a list and count the occurrence
# of each element, append to dict

b_list = [10, 20, 30, 10, 20, 40, 50]

# Can use extractor previously defined.
# Or rewrite as below

dict([(j, b_list.count(j)) for (i , j) in enumerate(b_list)])

# Using a loop
ind_count = []
ind_keys = []
final_dict = dict()
for elem in b_list:
    ind_count.append(b_list.count(elem))
    ind_keys.append(elem)
    if len(ind_keys) == len(b_list):
        final_dict = dict(zip(ind_keys, ind_count))


final_dict

# Solution from website:
countDict = dict()
for item in b_list:
    if item in countDict:
        countDict[item] += 1
    else:
        countDict[item] = 1
print("Returning counts ", countDict)

# Question 5.
# Given two lists of equal size, create a set that shows elements from both lists
# in pairs.

list_a = [1 , 2, 3, 4, 6, 9]

another_list = [1, 2, 3, 5, 6, 7]


def identical(object_a, object_b):
    """This tests for equal lengths not equal elements"""
    if len(object_a) == len(object_b):
        print("Feasible")
    else:
        raise ValueError("Not Feasible, check lengths")

# from random import randint
identical(list_a, another_list)

identical([1,2], [12,12,34])

# proceed with our problem
# Actually not possible with a set since it removes duplicates
# Use a tuple instead or list.
[(i, j) for i in another_list for j in list_a if i==j ]

# test on lists from site
firstlist= [1, 2, 3, 4, 5]
secondList = [10, 20, 30, 40, 50]
identical(firstlist, secondList)

[(i, j) for i in firstlist for j in secondList if i==j]

# Poorly worded question.Actually just needs printing both elements not intersection

for i,j in enumerate(firstlist):
    print({j, secondList[i]})

# Using a from scratch for loop

for i in range(len(firstlist)):
    print({firstlist[i], secondList[i]})

# Solution from site:
# uses zip, for some reason I abandoned it
print(set(zip(firstlist,secondList)))

# Question 6:
# Given two sets, find their intersection and discard from first set

firstSet = {10, 30, 40, 60, 45}
secondSet = {20, 50, 10, 40, 55}
new_set = set()
 for x in firstSet:
     if not x in secondSet:
         new_set.add(x)

new_set

# use builtins
{firstSet.discard(x) if x in secondSet}

firstSet

# Solution from site

# Find intersecion and discard
intersection = firstSet.intersection(secondSet)
for item in intersection:
    firstSet.remove(item)

firstSet

# Question 7

# Given two sets check if one set is a subset or superset of another set
# If subset, delete all elements form that set

set_one = {27, 43, 34}
set_two = {34, 93, 22, 27, 43, 53, 48}

if len(set_one.intersection(set_two)) == len(set_one) :
    set_one.clear()

set_one

# The above does the job.
# However, it's not well automated.

def check_subset(my_set, my_other_set):
    if len(my_set) > len(my_other_set):
        print("Set one is a superset of set two")
    else:
        print("Set one is a subset of set two")


def check_mate(my_set,my_other_set):
    discard_set = False
    if(len(my_set)<len(my_other_set)):
        discard_set = True
        if discard_set ==True and  len(my_set.intersection(my_other_set))==len(my_set):
            print("Set one discarded")
            my_set.clear()
            return my_set
    else:
        if discard_set== False and len(my_other_set) == len(my_other_set.intersection(my_set)):
            print("Set two discarded")
            my_other_set.clear()
            return my_other_set





check_mate(set_one,set_two)
check_mate(set_two,set_one)
# The above will discard if no intersection
# Test it on other sets
set_a = {1, 2, 3, 4, 5, 6, 7, 8}
set_b = {4, 5, 7, 8, 8, 9, 10, 12, 2, 1 }

set_a = {1,2,3}
set_b = {1,2,3,4,5}
check_mate(set_a,set_b)

set_b

# Test on site's data
firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}

check_mate(firstSet,secondSet)

# solution from site uses builtin superset
firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}
check_subset(firstSet,secondSet)
firstSet.issubset(secondSet)
