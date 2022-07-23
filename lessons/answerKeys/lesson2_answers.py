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
