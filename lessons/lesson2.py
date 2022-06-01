'''
Lesson 2
Written by Adithya Solai
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
-Still follow 0-indexing as we did before
'''
print(x[0:2])
print(x[3:5])

# Can also just leave the second value blank to get the rest of the list:
print(x[1:])

############ Exercise!! ############
lst = [8, 0, -6, 79]
# Retrieve the 3rd element in `lst`
# A possible answer
print(lst[2])
# Another possible answer
print(lst[-2])

# Retrieve the last 3 elements in `lst`
# A possible answer
print(lst[1:])

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

############ Exercise!! ############
lst = [8, 0, -6, 79] # <- the "original" `lst` in the exercises below

# What is `lst` after the following code?
lst.append([1,2,3])
# Answer: [8, 0, -6, 79, [1, 2, 3]]

# What is `lst` after the following code? (using the original `lst`)
lst + [1, 2, 3]
# Answer: [8, 0, -6, 79]

# What is `lst` after the following code? (using the original `lst`)
lst = lst + [1, 2, 3]
# Answer: [8, 0, -6, 79, 1, 2, 3]

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

############ Exercise!! ############
# Replace every integer in `lst` with the sum 
# from 1 to that integer
lst = [1, 7, 100, 5]

# Expected answer: [1, 28, 5050, 15]

# Possible Answer:
for i in range(len(lst)):
    # Apply Gauss' Sum formula.
    lst[i] = (lst[i]) * (lst[i] + 1) // 2

print(lst)

# Possible Answer 2:
lst = [1, 7, 100, 5]
for i in range(len(lst)):
    # Use an inner-loop to find the sum of integers
    # from 1 to the current element of lst
    sum_of_elem = 0
    for j in range(1, lst[i]+1):
        sum_of_elem += j

    lst[i] = sum_of_elem
    
print(lst)

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

# Can check the type of an object/variable with isinstance()
y = 5
if isinstance(y, int):
    print("True")
else:
    print("False")

if isinstance(y, str):
    print("True")
else:
    print("False")

############ Exercise!! ############
# Change every value in lst to the string "cat"
# If the value was already a string, don't change it
lst = ["asdf", 1, True, 7.7, "cat", ""]

# Expected Answer: ["asdf", "cat", "cat", "cat", "cat", ""]

# A possible answer
for idx, val in enumerate(lst):
    if isinstance(val, str) == False:
        lst[idx] = "cat"
print(lst)