'''
Lesson 2
Written by Adithya Solai

Copyright © 2021 Adithya Solai. All rights are reserved.
You cannot use, modify, or redistribute this code without 
explicit permission from Adithya Solai.
'''

'''
Lists:
-A way to store data without making a separate variable for
 each data point.
'''
x = [1, -40, 3, 29, 0]
print(x)

'''
List Indexing:
-Get the value at some given position in a list
-Indexed from 0 to n-1, where n is the length of the list
-(let's call this 0-indexing)
'''
print(x[0])
print(x[1])

# can also use negative indexing
# last element in the list has index -1
print(x)
print(x[-1])
# first element in the list has index -(length of the list)
print(x[-len(x)])


'''
List Splicing:
-Get 1 or more values from a list using their position.
-[inclusive, exclusive]
'''
print(x[0:2])
print(x[3:5])

'''
Append
-Add a single value to the end/right of a list.
'''
print(x)
x.append(100)
print(x)

'''
Concatenate
-Add a list of values to the end/right of a list
'''
print(x)
x = x + [-59, 42]
print(x)

# Must use assignment = 
# Concatenate is not "in-place" like append()
print(x)
x + [-99, -999]
print(x)

'''
for-loops + lists
3 tools to iterate over a list:
-range()
-for-each loop
-enumerate()
'''

############ range() ############
# using range() to iterate through a list
print(x)
for i in range(len(x)): # len(x) gives length of list x
    print(i) # range() makes i match perfectly with 0-indexing
    print(x[i]) # use list indexing to access each element
    print()

# use start & end parameters to make more complex for loops through lists
y = list(range(100)) # make a list from 0-99
print(y)
for i in range(0, len(y), 3): # only iterate through every 3rd element
    print(y[i])

############ for-each loops ############
# A LOT simpler than using range
print(x)
for val in x:
    print(val)

# However, we can't modify any elements in our list using for-each loops
y = [1,2,3,4,5]
print(y)
for num in y:
    num = num + 1
    # changes are reflected locally in this scope
    print(num)
print(y) # y is unchanged

# Easier to modify list using for-loops + range() approach
print(y)
for i in range(len(y)):
    y[i] = y[i] + 1
print(y) # everything incremented by 1!

############ enumerate ############
# need to understand tuples first

# kind of like coordinates
t = (4,5)

# can use same indexing as lists
print(t[0])
print(t[1])

# a cool way to initialize more than one variable at once
v1, v2 = t

print(v1)
print(v2)

# can also think of them as vectors (more than just 2 elements)
t2 = (-5, 9, 4)
print(type(t2))
print(t2)

# also need to understand enumerate() first
lst = [10,20,30,40,50]
print(enumerate(lst))

# iterating through lists with enumerate() is very elegant
# we can modify the list using idx
# or just iterate like a for-each loop using val
for idx, val in enumerate(lst):
    print('index: ' + str(idx)) # str() tries to convert input to a string
    print('curr value: ' + str(lst[idx]))
    print('curr value: ' + str(val))
    print()

'''
Lists are heterogenous
(They can contain more than one type of data)
'''
# this is totally fine to have!
x = ['hi', 6, -9.6, True, ["another list inside!"]]

# we can also iterate through it!
for val in x:
    print(val)

# Need to be careful when making modifications
for idx, val in enumerate(x):
    # x[idx] = x[idx] + 1 # <-- will crash for non int or float data types
    x[idx] = 999
print(x)


'''
List Comprehensions
-An even cooler way to iterate through and modify lists!
-A very "Pythonic" tool
'''

# iterating through a list and printing out its values
x = [10, 20, 30, 40, 50]
[print(val) for val in x]

# kind of bends our rule about not being able to modify
# a list using a for-each approach
x = [val * 10 for val in x]
print(x)

# however, this is not an in-place operation
# (since we have to do x= to actually reflect the change)
[val * 10 for val in x]
# x is unchanged
print(x)

# an elegant way to generate lists!
evens = [val for val in range(0, 101, 2)]
odds = [val for val in range(1, 101, 2)]

print(evens)
print(odds)