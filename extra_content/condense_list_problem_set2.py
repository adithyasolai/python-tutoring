## Problem 9 ##
# Condense list of lists into a single list
# Not every element in the list is a list (see the second test case)
#######################################################
# You need to define the function yourself for this one.
#######################################################

# Test Cases
assert condense([[12, 3], ["asdf"], [True, 7]]) == [12, 3, "asdf", True, 7]
assert condense([27, ["list in a list"]]) == [27, "list in a list"]

# -----------------------------------------------------------------------
