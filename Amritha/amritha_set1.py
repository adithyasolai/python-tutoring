'''
Amritha Set 1
Written by Adithya Solai

Copyright © 2021 Adithya Solai. All rights are reserved.
You cannot use, modify, or redistribute this code without 
explicit permission from Adithya Solai.
'''

'''
!!! REMINDERS !!!

As you work through these problems, make a new file called amritha_set1_scratch.py.
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
# Write a function that takes an input called `x`.
# The function will divide x by 2 and return the result.
# You can assume x will always be a number (an int or a float).
def halfOfX(x):
  return 0

assert halfOfX(10) == 5
assert halfOfX(30) == 15

#-----------------------------------------------------------------------

## Problem 2 ##
# Write a function that takes two inputs: `x` & `y`.
# Both x and y will be numbers (an int or a float).
# The function returns whichever number is larger.
# (Hint: Use an if-else statement!)
def largerNum(x, y):
  return 0

assert largerNum(7, 9) == 9
assert largerNum(10, 6) == 10

#-----------------------------------------------------------------------

## Problem 3 ##
# Write a function that takes three inputs: `reading`, `writing`, `math`.
# The function calculates and returns the total SAT score of a student 
# based on the three inputs.
#
# SAT score is just the sum of the Reading, Writing, and Math scores.
# The `reading` and `writing` input variables will be an int between 0 and 400.
# The `math` input variables will be an int between 0 and 800.
def SATScore(reading, writing, math):
  return 0

assert SATScore(360, 300, 790) == 1450
assert SATScore(400, 400, 800) == 1600


#-----------------------------------------------------------------------

## Problem 4 ##
# Write a function that takes two inputs: `height` and `wingspan`
# Height and wingspan are both ints (and the unit is inches).
# The function will return the str "lanky" if wingspan > height,
# "normal" if wingspan equals height, and "stocky" otherwise.
#
# Hint: Review if-elif-else statements.
# Hint: To return a str, just type: return "whatever string you want in quotes"
#
# YOU WILL HAVE TO WRITE YOUR OWN FUNCTION FROM SCRATCH! CALL IT wingspanCompare.


assert wingspanCompare(70, 70) == "normal"
assert wingspanCompare(75, 70) == "lanky"
assert wingspanCompare(65, 70) == "stocky"

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

print("All Normal Exercises Completed with all Test Cases passed!")