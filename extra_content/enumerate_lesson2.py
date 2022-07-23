############ enumerate() ############
# need to understand tuples first

# kind of like coordinates
t = (4, 5)

# can use same indexing as lists
print(t[0])
print(t[1])

# a cool way to initialize more than one variable at once
v1, v2 = t

print(v1)
print(v2)

# can also think of them as vectors (more than just 2 elements)
t2 = (-5, 9, 4)
print(type(t2))
print(t2)

# also need to understand enumerate() first
lst = [10, 20, 30, 40, 50]
print(enumerate(lst))

# iterating through lists with enumerate() is very elegant
# we can modify the list using idx
# or just iterate like a for-each loop using val
for idx, val in enumerate(lst):
    print('index: ' + str(idx))  # str() tries to convert input to a string
    print('curr value: ' + str(lst[idx]))
    print('curr value: ' + str(val))
    print()

############ Exercise!! ############
# Convert lst to a list of tuples, where each tuple's
# first value is the index of the value in lst, and
# the second value is the value itself.
lst = [7, -3, 0, 100, 12]

# Expected answer: [(0,7), (1,-3), (2,0), (3,100), (4,12)]

# Possible answer:
for idx, val in enumerate(lst):
    lst[idx] = (idx, val)

print(lst)
