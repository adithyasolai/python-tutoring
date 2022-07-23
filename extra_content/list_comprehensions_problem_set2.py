## Problem 10 ##
# Use list comprehensions to replace every integer in a list with its
# fibonacci number (1's fibonacci number is 1, 2's is 1, 3's is 2, 4's is 3, etc)
# (Use the fibonacci function from Problem Set 1 to help!)
# If the integer is even, do not replace it with its fibonacci number and leave it as
# it is. You are guaranteed that every value in the list is a positive integer >= 1.
#######################################################
# You need to define the function yourself for this one.
#######################################################

# Test Cases
assert fibonacci_convert([4, 1, 8, 9]) == [4, 1, 8, 34]
assert fibonacci_convert([102, 17, 59]) == [102, 1597, 956722026041]

# -----------------------------------------------------------------------
