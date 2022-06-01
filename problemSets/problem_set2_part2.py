'''
Problem Set 2 Part 2
Written by Adithya Solai
'''

## Problem 1 ##
# For some integer `num`, determine which integers in some list
# `lst` are divisible by `num`.
# Ex: num = 4, lst = [3, 8, 4, 2]. Return the list [False, True, True, False]
# since 8 and 4 are divisible by 4, but 3 and 2 are not.
#
# Ex 2: num = 1, lst = [10, 70, 23, 4]. Return the list [True, True, True, True]
# since every number is divisible by 1.
#
# You can assume the lst will only contain positive integers and num will only be positive integer.
def findFactors(num, lst):
  return 0

# Test Cases
assert findFactors(4, [3,8,4,2]) == [False, True, True, False]
assert findFactors(1, [10,70,23,4]) == [True, True, True, True]

#-----------------------------------------------------------------------

## Problem 2 ##
# Given a list of integers, return the index of the first odd number in the list.
# If the list has no odd numbers, return -1.
# You can assume the list only has positive integers.
def findFirstOdd(lst):
  return 0

# Test Cases
assert findFirstOdd([6,2,90,64]) == -1
assert findFirstOdd([10, 60, 7, 0]) == 2
assert findFirstOdd([9, 13, 70, 5]) == 0

#-----------------------------------------------------------------------

## Problem 3 ##
# Given a string and a list, return True if the list contains the string.
# (Note: Not every element in the list is guaranteed to be a str. 
#  Use isinstance() to check the data type of each element.)
# (Note: You can use == to see if two strings are equal.)
def listContainsString(s, lst):
  # s is a string
  # lst is a list
  return True

# Test Cases
assert listContainsString("asdf", [7, -22, True, [88, 10]]) == False
assert listContainsString("asdf", ["cat", 7, "ball", -9.7, "asdf"]) == True

#-----------------------------------------------------------------------

print("All Normal Exercises Completed with all Test Cases passed!")