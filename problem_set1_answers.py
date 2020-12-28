'''
Problem Set 1 Answer Key
Written by Adithya Solai

Copyright © 2021 Adithya Solai. All rights are reserved.
You cannot use, modify or redistribute this code without 
explicit permission from Adithya Solai.
'''

## Problem 1 ##
# Find the remainder of 1234 / 10 and print it
x = 1234

# Expected Answer: 4

## Answer ##
print(x % 10)

#-----------------------------------------------------------------------

## Problem 2 ##
# Find the remainder of 1234 / 100 and print it
x = 1234

# Expected Answer: 34

## Answer ##
print(x % 100)

#-----------------------------------------------------------------------

## Problem 3 ##
# Find the remainder of 1234 / 1000 and print it
x = 1234

# Expected Answer: 234

## Answer ##
print(x % 1000)

#-----------------------------------------------------------------------

## Problem 4 ##
# Retrieve the number 3 using /, //, and/or %, and print it
# Number = 1234
x = 1234

# Expected Answer: 3

## Answer ##
ans = x // 10 # ans is 123 at this point
ans = ans % 10 # ans is now just 3
print(ans)

#-----------------------------------------------------------------------

## Problem 5 ##
# Write a floor function for integer division.
# You can't use "//", which basically does this for you.
# `number` and `divisor` will only be integers >= 1.
def floor(number, divisor):
  ans = number / divisor
  ans = int(ans)
  return ans

# Test Cases
assert floor(7,2) == 3
assert floor(18,3) == 6

#-----------------------------------------------------------------------

## Problem 6 ##
# Write a ceiling function for integer division.
# You can't use "//", which would make this much easier.
# `number` and `divisor` will only be integers >= 1.
def ceiling(number, divisor):
  ans = number / divisor

  if number % divisor == 0:
    # If divisor is an factor of number, no
    # need to take the ceiling.
    return int(ans)
  else:
    # `int(ans)` floors `ans` like before
    # add a `+ 1` here to get the ceiling
    ans = int(ans) + 1
    return ans

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
  if champ >= 4 or (champ >= 1 and pts >= 5000 and reb >= 3000):
    return True
  else:
    return False

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
  if yoe > 5 and pc >= 100:
    return "SWE III"
  elif yoe >= 2 and pc > 20:
    return "SWE II"
  else:
    return "SWE I"

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

## Answer ##
ans = 0
for n in range(1,101): # 101 is EXCLUSIVE in the range() function
  ans = ans + n
print(ans)

#-----------------------------------------------------------------------

## Problem 10 ##
# Write a function that sums all of the EVEN numbers from 1 to some given number 'num'.
def sumOnlyEvens(num):
  ans = 0
  for n in range(1, num+1):
    if n % 2 == 0:
      ans = ans + n
  
  return ans

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
  ans = 0
  for n in range(1, num+1):
    if n % 2 == 0:
      ans = ans + n
    else:
      ans = ans - n
  
  return ans

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
  # Take care of edge case when num <= 1 here
  if num <= 1:
    return False

  # For a number to be prime, it should only have
  # exactly 2 factors.
  num_factors = 0

  # Iterate through all the numbers 1 to n, and increment
  # `num_factors` whenever we find a valid factor.
  for factor in range(1, num+1):
    if num % factor == 0: # Checks for valid factors
      num_factors += 1

  # If `num_factors` is still only 2, then num must be prime.
  if num_factors == 2:
    return True
  else:
    return False

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
  # Take care of base case where n = 1 or n = 2 here
  if n == 1 or n == 2:
    return 1

  # Keeps track of the current fibonacci number
  # as we iterate towards the nth fibonacci number
  curr = None
  # n=1 fibonacci number
  prev_prev = 1
  # n=2 fibonacci number
  prev = 1

  for i in range(3, n+1):
    curr = prev_prev + prev

    # Prepare `prev` and `prev_prev` for next iteration
    prev_prev = prev
    prev = curr

  return curr

# Test Cases
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(20) == 6765
assert fibonacci(30) == 832040

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

print("All Challenge Exercises Completed with all Test Cases passed!")