'''
Lesson 1
Written by Adithya Solai
'''

'''
The main types of data we will work with for this lesson:
- int -> Integers
- float -> Real Numbers
- string -> Text
- boolean -> True/False
'''
print("hi")
print(5)
print(5.5)
print(True)

print(type("hi")) # string
print(type(5)) # int
print(type(5.5)) # float
print(type(True)) # boolean

'''
Variables:
-Variables are dynamic: Can change a variable from one data type to another with no problem!
'''
x = 5

print(x)
print(type(x))

# can change x from int to str with no problems
x = "abc"

print(x)
print(type(x))

'''
Operators:
All of these are binary operators in this form:
x ? y

+ (Addition)
- (Subtraction)
* (Multiplication)

------------

// (Integer Division)
/ (Float Division)
** (Exponent)
% (Modulo)
'''

print(5.5 - 5)

print(2.3 * 2)

# Booleans are weird! They are calculated as ints!
# True -> 1
# False -> 0
print(7 + True)
print(7 + False)

# Store results of an operation in a variable
x = 1 + 1
print(x)

# Do operations with variables
x = 9
y = 3
print(x // y)

# EXPLORE THESE ON YOUR OWN !
# / 
# //
# **
# %

# Answers
# / is float divide (it keeps decimal remainders)
# the result of using / is always a float
print(3/2)

# // is integer divide (it chops off decimal remainders)
# the result of using // is always an int
print(3//2)

'''
Functions
-Give input, get some output
-Can use functions repeatedly; no need to re-write code
'''
# Ex: Square an input number
def square(x):
  # x can be an int or float, and this would work
  return x ** 2

print(square(5)) # x is an int
print(square(4.5)) # x is a float

# Ex: Fahren to Celsius calculator
# We can dictate PEMDAS ourselves with parantheses:
def fahrenToCelsius(f):
  # f can be an integer or float, and this would work
  return (f-32) * (5/9)

print(fahrenToCelsius(100))


############ Exercise!! ############
# Write a function for Celsius to Fahrenheit!
def celsiusToFahren(c):
  return 0

# Test Cases
print(celsiusToFahren(0)) # Should be 32 deg Fahren
print(celsiusToFahren(37)) # Should be 98.6 deg Fahren
print(celsiusToFahren(-20)) # Should be -4 deg Fahren

# A Possible Answer
def celsiusToFahren(c):
  return (c * (9/5)) + 32

############ Exercise!! ############
# Write a function for the Weighted Average Cost of Capital
# WACC = [% Equity * Cost of Equity ($)] + 
#        [% Debt * Cost of Debt * (1- Corp. Tax %)]
# `pctEquity` is % Equity, and it is a float between 0 and 1
# `cEquity` is Cost of Equity, and it is any positive int
# `pctDebt` is % Debt, and it is a float between 0 and 1
# `cDebt` is Cost of Debt, and it is any positive int
# `corpTaxRate` is Corp. Tax Rate, and it is a float between 0 and 1
def WACC(pctEquity, cEquity, pctDebt, cDebt, corpTaxRate):
  return 0

# Test Cases
print(WACC(0.5, 500, 0.5, 500, 0.25)) # Should be 437.5
print(WACC(0.9, 10000, 0.1, 5000, 0.2)) # Should be 9400

# A Possible Answer
def WACC(pctEquity, cEquity, pctDebt, cDebt, corpTaxRate):
  return (pctEquity * cEquity) + (pctDebt * cDebt * (1 - corpTaxRate))

'''
if, else-if, else statements
-Use if, elif, and else statements to make the computer only do
 something if some condition is met

Tools needed for if, else-if, else conditionals:
- Comparators 
- Logical Operators
- Parentheses
'''

############ Comparators ############
# >, >=, <, <=, ==, !=

# Ex: Obesity Calculator Function
def isObese(weight, height):
  # weight is a float
  # height is a float

  # calculate BMI
  BMI = (703 * weight) / (height ** 2)

  # return True if the person is obese
  if BMI >= 30:
    return True
  else: # False otherwise
    return False

# Test Cases
print(isObese(185, 65))
print(isObese(185, 72))

# == vs =
# == is a comparator
if 1 == 1:
  print("hi")

# = is used for assignment
y = "hi"
print(y)

############ Logical Operators ############
# `and` and `or` logical operators
print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)

# Ex: Combine comparators and logical operators with if-else
def canDrive(age, hasPermit):
  # age is an int
  # hasPermit is a bool
  if age >= 17 or hasPermit == True: # (Pythonic way: just omit == True)
    return True
  else:
    return False

# Test Cases
print(canDrive(16, True))
print(canDrive(16, False))
print(canDrive(21, False))

############ Exercise!! ############
# Write a function that returns True if P/E ratio > 10 OR Market Cap > 10000
def isOverValued(pe, market_cap):
  # pe is float
  # market cap is an int
  return 0

# A Possible Answer
def isOverValued(pe, market_cap):
  if pe > 10 or market_cap > 10000:
    return True
  else:
    return False

# Test Cases
print(isOverValued(15, 15000)) # True. PE & Market Cap Conditions Met
print(isOverValued(10, 15000)) # True. Only Market Cap Condition Met
print(isOverValued(15, 10000)) # True. Only PE Ratio Condition Met
print(isOverValued(3, 5000)) # False. No Conditions Met

############ Parentheses ############
# Allows for more complex if-else conditionals

# Ex: You are eligible for a loan if you can 
# provide AT LEAST $4,000 down-payment AND 
# you are AT LEAST 18 years old OR your parents 
# take responsibility for paying the loan.
def loanEligible(downpayment, age, parent):
  # downpayment is an int
  # age is an int
  # parent is a bool
  if downpayment >= 4000 and (age >= 18 or parent == True):
    return True
  else:
    return False

# Need test cases
print(loanEligible(8000, 17, True)) # True
print(loanEligible(8000, 17, False)) # False


############ Exercise!! ############
# Write a function to determine if someone should get a special
# credit card. A person qualifies for this credit card if they
# are already a customer of the bank OR has a net worth of AT LEAST 
# $100000 AND has $0 in debt
def specialCreditCard(member, networth, debt):
  # member is a bool
  # networth & debt are integers
  return 0

# A Possible Answer
def specialCreditCard(member, networth, debt):
  if member == True or (networth >= 100000 and debt == 0):
    return True
  else:
    return False

# Need test cases
print(specialCreditCard(False, 90000, 0)) # False

############ else-if ############
# Allows for even more control of logical flow in code.
# Use else-if when you have 3+ logical cases that each
# require different code.

# Ex: Determining an exam grade using letter grade cutoffs
# Note: Use `elif` (not `else-if`) when coding this.
# Note: Always need an `else` case even when you have
# `elif` cases.
def examGrade(grade):
  if grade >= 90:
    return "A"
  elif grade >= 80:
    return "B"
  elif grade >= 70:
    return "C"
  elif grade >= 60:
    return "D"
  else:
    return "F"

# Need test cases

# (You can practice using else-if in Problem #8 of Problem Set 1.)

'''
For-Loops
-Make the computer do something repeatedly for
 some defined # of iterations.
'''

############ range() ############
# format: range(start, end, step)
# start & step are optional

# only specify end
# start is auto-set to 0
# end is exclusive
print(range(5)) # range type, not a list
print(list(range(5))) # use list() to convert to list

# specify start & end
# start is inclusive, end is exclusive (like list splicing)
print(list(range(4, 7)))

# specify start, end, & step
print(list(range(1, 28, 3)))
# can also have negative step
print(list(range(100, 0, -25)))
print(range(5))
print(range(1,11,2))

############ For-loop over a range() ############
# Ex: Print all numbers from 1 to 5
for num in range(1,6):
  print(num)

# Ex: Finding the product of all numbers from 1 to 5
product = 1
for num in range(1, 6):
  product = product * num
print(product)

############ Exercise!! ############
# Write a function that sums all of the numbers from 1 to some given number 'num'.
def sumUpFromOne(num):
  return 0

# A Possible Answer
def sumUpFromOne(num):
  total = 0
  # explain why to use `n` instead of `num`
  for n in range(1, num+1):
    total = total + n

  return total

  t = 1
  for x in range(1,26):
    t *= x

  print(t)