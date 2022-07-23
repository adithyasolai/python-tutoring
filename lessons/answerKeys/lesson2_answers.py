############ Exercise!! ############
lst = [8, 0, -6, 79]
# Retrieve the 3rd element in `lst`
# A possible answer
print(lst[2])
# Another possible answer
print(lst[-2])

# Retrieve the last 3 elements in `lst`
# A possible answer
print(lst[1:])

############ Exercise!! ############
lst = [8, 0, -6, 79]  # <- the "original" `lst` in the exercises below

# What is `lst` after the following code?
lst.append([1, 2, 3])
# Answer: [8, 0, -6, 79, [1, 2, 3]]

# What is `lst` after the following code? (using the original `lst`)
lst + [1, 2, 3]
# Answer: [8, 0, -6, 79]

# What is `lst` after the following code? (using the original `lst`)
lst = lst + [1, 2, 3]
# Answer: [8, 0, -6, 79, 1, 2, 3]

############ Exercise!! ############
# Replace every integer in `lst` with the sum
# from 1 to that integer
lst = [1, 7, 100, 5]

# Expected answer: [1, 28, 5050, 15]

# Possible Answer:
for i in range(len(lst)):
    # Apply Gauss' Sum formula.
    lst[i] = (lst[i]) * (lst[i] + 1) // 2

print(lst)

# Possible Answer 2:
lst = [1, 7, 100, 5]
for i in range(len(lst)):
    # Use an inner-loop to find the sum of integers
    # from 1 to the current element of lst
    sum_of_elem = 0
    for j in range(1, lst[i] + 1):
        sum_of_elem += j

    lst[i] = sum_of_elem

print(lst)

############ Exercise!! ############
# Change every value in lst to the string "cat"
# If the value was already a string, don't change it
lst = ["asdf", 1, True, 7.7, "cat", ""]

# Expected Answer: ["asdf", "cat", "cat", "cat", "cat", ""]

# A possible answer
for idx, val in enumerate(lst):
    if isinstance(val, str) == False:
        lst[idx] = "cat"
print(lst)
