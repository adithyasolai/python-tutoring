############ Exercise!! ############
# Apply the indexing & splicing operations on the following
# data to get the appropriate output.
#
# Column 0: Car Maker
# Column 1: Model
# Column 2: Year
# Column 3: Miles per Gallon

cars = [["Fiat", "124 Spider", 2017, 35],
        ["Nissan", "2005X", 1996, 26],
        ["BMW", "3 Series", 2015, 33],
        ["Mitsubishi", "3000GT", 1999, 22]]

# Retrieve the bottom two rows
# (BMW & Mitsubishi)

# Possible Answers:
print(cars[2:])
print(cars[2:4])

# Retrieve the miles per gallon for the 2nd row (or row 1, or the Nissan row)

# Possible Answers:
print(cars[1][3])


############ Exercise!! ############
# Append data to the cars dataset from before
#
# Column 0: Car Maker
# Column 1: Model
# Column 2: Year
# Column 3: Miles per Gallon (or mpg)

cars = [["Fiat", "124 Spider", 2017, 35],
        ["Nissan", "2005X", 1996, 26],
        ["BMW", "3 Series", 2015, 33],
        ["Mitsubishi", "3000GT", 1999, 22],
        ["Honda", "Odyssey"]]

# Add the following Car to the table:
# Toyota Camry 2009, 27 mpg

# Possible Answers
cars.append(["Toyota", "Camry", 2009, 27])

# Add the year 2012 and the mpg 22 to the Honda Odyssey row
# Do it with appends. Then do it again with concatenation

# Possible Answers
cars[4].append(2012)
cars[4].append(22)

# cars[4] += [2012, 27]
print(cars)

############ Exercise!! ############
# Iterate the 2-D list of integers below and convert the cell
# to True if the integer is a prime number, and False otherwise
numbers = [[4, 17, 9, 23],
           [283, 422, 839, 131],
           [36, 111, 113, 739]]

# Possible Answer:


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


for r in range(len(numbers)):
    for c in range(len(numbers[0])):
        numbers[r][c] = isPrime(numbers[r][c])

# Expected Answer:
# [[False, True, False, True], [True, False, True, True], [False, False, True, True]]

print(numbers)

############ Challenge Exercise!! ############
# Do the same task as above with list comprehensions!
numbers = [[4, 17, 9, 23],
           [283, 422, 839, 131],
           [36, 111, 113, 739]]

# Possible Answer
numbers = [[isPrime(num) for num in row] for row in numbers]
print(numbers)

############ Exercise ############
# Use a while loop to iterate through the cars data
# and print every string.

cars = [["Fiat", "124 Spider", 2017, 35],
        ["Nissan", "2005X", 1996, 26],
        ["BMW", "3 Series", 2015, 33],
        ["Mitsubishi", "3000GT", 1999, 22],
        ["Honda", "Odyssey", 2012, 22],
        ["Toyota", "Camry", 2009, 27]]

# Possible Answer
r = 0
while r < len(cars):
    c = 0
    while c < len(cars[0]):
        if isinstance(cars[r][c], str):
            print(cars[r][c])
        c = c + 1
    r = r + 1
