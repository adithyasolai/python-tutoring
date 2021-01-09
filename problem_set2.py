'''
Problem Set 2
Written by Adithya Solai

Copyright © 2021 Adithya Solai. All rights are reserved.
You cannot use, modify, or redistribute this code without 
explicit permission from Adithya Solai.
'''

## Problem 6 ##
# Retrieve the 1st element in the list below.
lst = [7, 43, -2]

# Expected Answer: 7

#-----------------------------------------------------------------------

## Problem 7 ##
# Retrieve the 2nd element in the list below.
lst = [7, 43, -2]

# Expected Answer: 43

#-----------------------------------------------------------------------

## Problem 8 ##
# Retrieve the first 4 elements of the list below
lst = [9, 4, 3, -5, 6, 4, 54, 34, 23]

# Expected Answer: [9, 4, 3, -5]

#-----------------------------------------------------------------------

## Problem 9 ##
# Show 2 different ways to retrieve the value 5.7 from the list below
lst = [4, 6, "as", 5.7, -49.2, False]

#-----------------------------------------------------------------------

## Problem 11 ##
# Given a positive integer n, return a list of all the factors of n.
def factors(n):
    return None

# Test Cases
assert factors(15) == [1, 3, 5, 15]
assert factors(23) == [1, 23]

#-----------------------------------------------------------------------

## Problem 12 ##
# Find the sum of all the elements in a given list
# List is guaranteed to only have positive integers (0, 1, 2, ...)
def sumList(lst):
    return None

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

# Test Cases
assert largestElem([9, 0, 27, 27]) == 27
assert largestElem([10]) == 10

#-----------------------------------------------------------------------

## Problem 14 ##
# Find the smallest element in a given list.
# List is guaranteed to only have positive integers (0, 1, 2, ...)
# You can assume the list will have at least one element in it.
#######################################################
# You need to define the function yourself for this one.
#######################################################

# Test Cases
assert smallestElem([9, 0, 27, 27]) == 0
assert smallestElem([10]) == 10

#-----------------------------------------------------------------------

## Problem 15 ##
# Condense list of lists into a single list
# Not every element in the list is a list (see the second test case)
#######################################################
# You need to define the function yourself for this one.
#######################################################

# Test Cases
assert condense([[12,3], ["asdf"], [True, 7]]) == [12, 3, "asdf", True, 7]
assert condense([27, ["list in a list"]]) == [27, "list in a list"]

#-----------------------------------------------------------------------

print("All Normal Exercises Completed with all Test Cases passed!")