'''
List Comprehensions
-An even cooler way to iterate through and modify lists!
-A very "Pythonic" tool
'''

# iterating through a list and printing out its values
x = [10, 20, 30, 40, 50]
[print(val) for val in x]

# kind of bends our rule about not being able to modify
# a list using a for-each approach
y = [val * 10 for val in x]
print(y)

# however, this is not an in-place operation
# (since we have to do x= to actually reflect the change)
[val * 10 for val in x]
# x is unchanged
print(x)

# an elegant way to generate lists!
evens = [val for val in range(0, 11, 2)]
odds = [val for val in range(1, 11, 2)]

print(evens)
print(odds)

# Can also incorporate if-else with some awkward syntax
is_even = [(val, True) if val % 2 == 0 else (val, False)
           for val in range(1, 11, 1)]
print(is_even)

# More elegant way to do this:
is_even = [(val, val % 2 == 0) for val in range(1, 11, 1)]
print(is_even)

############ Exercise!! ############
# Square every integer in lst using list comprehensions
# if the integer is a prime number.
# Otherwise, leave the integer as it is
lst = [5099, 4621, 70, 4999, 7371]

# Expected answer: [25999801, 21353641, 70, 24990001, 7371]

# A possible answer


def isPrime(num):
    if num <= 1:
        return False

    num_factors = 0

    for factor in range(1, num + 1):
        if num % factor == 0:
            num_factors += 1

    if num_factors == 2:
        return True
    else:
        return False


lst = [val ** 2 if isPrime(val) else val for val in lst]
print(lst)
