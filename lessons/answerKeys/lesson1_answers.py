# EXPLORE THESE ON YOUR OWN !
# /
# //
# **
# %

# Answers
# / is float divide (it keeps decimal remainders)
# the result of using / is always a float
print(3 / 2)  # Should be 1.5

# // is integer divide (it chops off decimal remainders)
# the result of using // is always an int
print(3 // 2)  # Should be 1

# ** is the exponent operator. In a ** b, `a` is the base,
# and `b` is the exponent.
print(3 ** 2)  # Should be 9

# % is the modulo operator. a % b returns the remainder leftover
# after dividing `a` by `b`.
print(15 % 7)  # Should return 1 because 15 divided by 7 is 2 remainder 1.

##########################################################

############ Exercise!! ############
# Write a function for Celsius to Fahrenheit!


def celsiusToFahren(c):
    return (c * (9 / 5)) + 32

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
    return (pctEquity * cEquity) + (pctDebt * cDebt * (1 - corpTaxRate))


############ Exercise!! ############
# Write a function that returns True if P/E ratio > 10 OR Market Cap > 10000
def isOverValued(pe, market_cap):
    if pe > 10 or market_cap > 10000:
        return True
    else:
        return False

############ Exercise!! ############
# Write a function to determine if someone should get a special
# credit card. A person qualifies for this credit card if they
# are already a customer of the bank OR has a net worth of AT LEAST
# $100000 AND has $0 in debt


def specialCreditCard(member, networth, debt):
    if member or (networth >= 100000 and debt == 0):
        return True
    else:
        return False

############ Exercise!! ############
# Write a function that sums all of the numbers from 1 to some given
# number 'num'.


def sumUpFromOne(num):
    total = 0
    # explain why to use `n` instead of `num`
    for n in range(1, num + 1):
        total = total + n

    return total
