'''
Problem Set 1
Written by Adithya Solai

Copyright © 2021 Adithya Solai. All rights are reserved.
You cannot use, modify or redistribute this code without 
explicit permission from Adithya Solai.
'''

## Problem 1 ##
# Find the remainder of 1234 / 10 and print it
x = 1234

# Expected Answer: 4

#-----------------------------------------------------------------------

## Problem 2 ##
# Find the remainder of 1234 / 100 and print it
x = 1234

# Expected Answer: 34

#-----------------------------------------------------------------------

## Problem 3 ##
# Find the remainder of 1234 / 1000 and print it
x = 1234

# Expected Answer: 234

#-----------------------------------------------------------------------

## Problem 4 ##
# Retrieve the number 3 using (/, //, or %), and print it
# Number = 1234
x = 1234

# Expected Answer: 3

#-----------------------------------------------------------------------

## Problem 5 ##
# Write a floor function for integer division.
# You can't use "//", which basically does this for you.
# `number` and `divisor` will only be integers >= 1.
def floor(number, divisor):
    return None

# Test Cases
assert floor(7,2) == 3
assert floor(18,3) == 6

#-----------------------------------------------------------------------

## Problem 6 ##
# Write a ceiling function for integer division.
# You can't use "//", which would make this much easier.
# `number` and `divisor` will only be integers >= 1.
def ceiling(number, divisor):
    return None

# Test Cases
assert ceiling(7,2) == 4
assert ceiling(18,3) == 6

#-----------------------------------------------------------------------

## Problem 7 ##
# Write a function that determines if an NBA player is eligible
# for the Basketball Hall of Fame.
#
# You are given three variables about the NBA players:
# Number of Championships Won (`champ`, an int)
# Number of Points Scored (`pts`, an int)
# Number of Rebounds (`reb`, an int)
#
# A player is eligible for the Basketball Hall of Fame if they have
# won at least 4 championships OR have at least 1 championships won,
# at least 5000 points scored, and at least 3000 rebounds.
def basketballHOF(champ, pts, reb):
  return None

# Test Cases
assert basketballHOF(4, 4000, 2500) == True
assert basketballHOF(3, 7000, 3000) == True
assert basketballHOF(10, 20000, 10000) == True
assert basketballHOF(0, 10000, 5000) == False

#-----------------------------------------------------------------------

## Problem 8 ##
# Write a function that returns the employee level of a given
# Software Engineer (SWE) at a large tech company.
# 
# You are given two variables about the Software Engineer:
# Years of Experience (`yoe`, an int)
# Projects Completed (`pc`, an int)
#
# Return "SWE III" if the Software Engineer has more then 5 years of
# experience and has completed at least 100 projects
#
# Return "SWE II" if the Software Engineer has at least 2 years of
# experience and has completed more than 20 projects
#
# Return "SWE I" otherwise
def sweLevel(yoe, pc):
  return None

# Test Cases
assert sweLevel(5, 100) == "SWE II"
assert sweLevel(8, 150) == "SWE III"
assert sweLevel(2, 20) == "SWE I"
assert sweLevel(0, 0) == "SWE I"
assert sweLevel(3, 50) == "SWE II"

#-----------------------------------------------------------------------

## Problem 9 ##
# Find and print the sum of the first 100 integers: 1 + 2 + 3 + ... + 100
# (No function needed. Just write the code and print the final result.)

# Expected Answer: 5050

#-----------------------------------------------------------------------

## Problem 10 ##
# Write a function that sums all of the EVEN numbers from 1 to some given number 'num'.
def sumOnlyEvens(num):
  return 0

# Test Cases
assert sumOnlyEvens(100) == 2550
assert sumOnlyEvens(3) == 2
assert sumOnlyEvens(5000) == 6252500

#-----------------------------------------------------------------------

## Problem 11 ##
# Write a function that sums all EVENS and subtracts all ODDS from 1 to some number 'num'
# Ex: num = 5
# -1 + 2 - 3 + 4 - 5 = -3
def sumEvensSubtractOdds(num):
  return 0

# Test Cases
assert sumEvensSubtractOdds(1) == -1
assert sumEvensSubtractOdds(5) == -3
assert sumEvensSubtractOdds(10) == 5
assert sumEvensSubtractOdds(100) == 50
assert sumEvensSubtractOdds(5000) == 2500

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

print("All Normal Exercises Completed with all Test Cases passed!")

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

## Challenge 1 ##
# Write a function that determines if an integer is prime.
def isPrime(num):
  return 0

# Test Cases
assert isPrime(1) == False
assert isPrime(2) == True
assert isPrime(1667) == True
assert isPrime(7841) == True
assert isPrime(439482) == False
assert isPrime(15) == False

#-----------------------------------------------------------------------

## Challenge 2 ##
# Write a function that returns the nth fibonacci number
# Fibonacci Seq: 1, 1, 2, 3, 5, 8, 13, ...
# if n = 4, return 3.
def fibonacci(n):
  return 0

# Test Cases
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(20) == 6765
assert fibonacci(30) == 832040

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

print("All Challenge Exercises Completed with all Test Cases passed!")