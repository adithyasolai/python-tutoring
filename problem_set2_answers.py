'''
Problem Set 2 Answer Key
Written by Adithya Solai

Copyright © 2021 Adithya Solai. All rights are reserved.
You cannot use, modify, or redistribute this code without 
explicit permission from Adithya Solai.
'''

## Problem 6 ##
# Retrieve the 1st element in the list below.
lst = [7, 43, -2]

# Expected Answer: 7

## Answer ##
print(lst[0])

#-----------------------------------------------------------------------

## Problem 7 ##
# Retrieve the 2nd element in the list below.
lst = [7, 43, -2]

# Expected Answer: 43

## Answer ##
print(lst[1])

#-----------------------------------------------------------------------

## Problem 8 ##
# Retrieve the first 4 elements of the list below
lst = [9, 4, 3, -5, 6, 4, 54, 34, 23]

# Expected Answer: [9, 4, 3, -5]

## Answer ##
print(lst[0:4])

#-----------------------------------------------------------------------

## Problem 9 ##
# Show 2 different ways to retrieve the value 5.7 from the list below
lst = [4, 6, "as", 5.7, -49.2, False]

## Answer ##
print(lst[3])
print(lst[-3])

#-----------------------------------------------------------------------

## Problem 11 ##
# Given a positive integer n, return a list of all the factors of n.
def factors(n):
    factor_lst = []

    for i in range(1,n+1):
        if n % i == 0:
            factor_lst.append(i)

    return factor_lst

# Test Cases
assert factors(15) == [1, 3, 5, 15]
assert factors(23) == [1, 23]

#-----------------------------------------------------------------------

## Problem 12 ##
# Find the sum of all the elements in a given list
# List is guaranteed to only have positive integers (0, 1, 2, ...)
def sumList(lst):
    total = 0

    for num in lst:
        total = total + num

    return total

# Test Cases
assert sumList([1, 3, 5, 10]) == 19
assert sumList([]) == 0
assert sumList([99]) == 99

#-----------------------------------------------------------------------

## Problem 13 ##
# Find the largest element in a given list.
# List is guaranteed to only have positive integers (0, 1, 2, ...)
# You can assume the list will have at least one element in it.
#######################################################
# You need to define the function yourself for this one.
#######################################################
def largestElem(lst):
    largest = 0

    for num in lst:
        if num > largest:
            largest = num
    
    return largest

# Test Cases
assert largestElem([9, 0, 27, 27]) == 27
assert largestElem([10]) == 10

#-----------------------------------------------------------------------

## Problem 14 ##
# Find the smallest element in a given list.
# List is guaranteed to only have positive integers (0, 1, 2, ...)
#######################################################
# You need to define the function yourself for this one.
#######################################################
def smallestElem(lst):
    smallest = None

    for num in lst:
        if smallest is None or num < smallest:
            smallest = num

    return smallest

# Test Cases
assert smallestElem([9, 0, 27, 27]) == 0
assert smallestElem([10]) == 10

#-----------------------------------------------------------------------

## Problem 15 ##
# Condense a given list of lists into a single list
#######################################################
# You need to define the function yourself for this one.
#######################################################
def condense(lst):
    condensed = []

    for elem in lst:
        if isinstance(elem, list):
            # Concatenate other list on to `condensed`
            condensed = condensed + elem
        else:
            # Just append the non-list element to `condensed`
            condensed.append(elem)

    return condensed

# Test Cases
assert condense([[12,3], ["asdf"], [True, 7]]) == [12, 3, "asdf", True, 7]
assert condense([27, ["list in a list"]]) == [27, "list in a list"]

#-----------------------------------------------------------------------

print("All Normal Exercises Completed with all Test Cases passed!")