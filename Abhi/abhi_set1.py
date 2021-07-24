'''
Abhi Set 1
Written by Adithya Solai

Copyright © 2021 Adithya Solai. All rights are reserved.
You cannot use, modify, or redistribute this code without 
explicit permission from Adithya Solai.
'''

'''
!!! REMEMBER !!!
COUNT HOW MANY TIMES YOU RUN YOUR CODE. DON'T RUSH! 
THE FEWER TIMES YOU RUN YOUR CODE, THE BETTER!
'''

'''
!!! REMINDERS !!!

As you work through these problems, make a new file called abhi_set1_scratch.py.
Do your coding and testing on that file. Make sure to use print() statements to help
with testing & debugging!

Copy-paste the test cases from the assert statements for each problem below
into your scratch file. Use print() statements to verify that these test cases work
in your scratch file. Once everything works in your scratch file, copy-paste your
solution back into this file to pass the assert statements.

The comments and examples below show you how to use a scratch file for coding, testing,
and debugging.

'''

# Example of a function that just adds three to the input and returns that as output.
def addThree(x):
  return x + 3

# Example of a assert statement for this function
assert addThree(7) == 10 # 7 + 3 should equal 10

# Put this in your scratch file to test your code.
print(addThree(7)) 

# Click Run in your scratch file and look at the Terminal output at the bottom of your screen
# to make sure the output is what you expect (10 in this case)

# After confirming your code works in your scratch file, copy-paste your code
# back into this file. Click Run and look at the Terminal output at the bottom of your screen.
# If your code is right for the addThree() function, there should be an AssertionError 
# for some OTHER function's test cases, not an addThree() function test case.

# When you complete all problems and pass all the assert test cases, you should see a
# message in your Terminal output that reads: "All Normal Exercises Completed with all Test Cases passed!"
# (and no AssertionErrors).

#-----------------------------------------------------------------------

## Problem 1 ##
# Write a function that takes a list `lst` as input.
# `lst` is guaranteed to only contain positive integers.
# The function will return a new list that only contains the ODD
# integers from the original `lst`.
#
# Hint: Make a new empty list at the start of your function. Use the append()
# function to add odd integers to that new list. Finally, return that
# new list after you have gone through all of the integers in `lst`.
def oddsOnly(lst):
  return 0

assert oddsOnly([7, 10, 12, 9]) == [7, 9]
assert oddsOnly([80, 10, 12, 24]) == []

#-----------------------------------------------------------------------

## Problem 2 ##
# Write a function that takes a list `lst` as input.
# `lst` is guaranteed to only contain positive integers.
# The function will return the total number of EVEN integers in `lst`
def numEvens(lst):
  return 0

assert numEvens([7, 10, 12, 9]) == 2
assert numEvens([80, 10, 12, 24]) == 4
assert numEvens([87, 11, 13, 21]) == 0

#-----------------------------------------------------------------------

## Problem 3 ##
# Write a function that takes two variables as input: `a` and `b`.
# a & b are guaranteed to be positive integers.
# The function will return a list of all ODD integers between a & b 
# (and also include a & b in the list if they are ODD).
#
# Hint: Similar to Problem 1. Start with a new empty list inside the function.
# Do a for loop from a to b, and build up the new empty list with append()
# as you go through the for loop. Return the new list at the end of the function.
def allOddsBetween(a, b):
  return 0

assert allOddsBetween(10, 17) == [11, 13, 15, 17]
assert allOddsBetween(19, 20) == [19]

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

print("All Normal Exercises Completed with all Test Cases passed!")