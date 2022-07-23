'''
Lesson 3
Written by Adithya Solai
'''

'''
2-D Lists:
-Lists within lists
-A matrix of dimensions m x n
-Rows & columns

Same operations as 1-D Lists:
-Initializing
-Indexing
-Splicing
-Appending
-Removing
-Iterations w/ For-Loops
'''

# Ex: 2-D List with info about students
# Column 0 (leftmost): Name (a `str`)
# Column 1: Age (an `int`)
# Column 2: Graduating (a `bool`)

# Initialize
import random
students = [["Arjun", 16, True],
            ["John", 18, False],
            ["Jane", 17, True]]
print(students)

############ Multi-Index Indexing ############
# Get all of Arjun's data, who is in row 0
# (Commas in the print statement add a space and print any other object without having to `str` cast)
print("Arjun's Data:", students[0])
# Get all of Jane's data, who is in row 2 (or row -1)
print("Jane's Data:", students[2])
print("Jane's Data:", students[-1])

# Get Arjun's Age, which is row 0, col 1
print("Arjun's Age:", students[0][1])
# Get John's Name, which is row 1, col 0
print("John's Age:", students[1][0])

############ Splicing ############
# Get the data from only the first two rows
print(students[0:2])
# Get John's Age and Graduating only
print(students[1][1:])

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

############ Append ############
# At the end of the day, a 2D list is still a list.
# Be careful to only append more lists.
# Python will allow you to append anything since lists are heterogeneous.

# Ex: Let's add to the Student table
students = [["Arjun", 16, True],
            ["John", 18, False],
            ["Jane", 17, True]]

# Append Damian's data
students.append(["Damian", 15, True])
print(students)

# Append some of Mark's data
students.append(["Mark", 17])
print(students)

# Append Mark's Graduating value to his incomplete row
students[4].append(False)
print(students)

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

############ Iterating 2-D Lists w/ For Loops ############
# Always structure as a nested for-loop.
# Rows in outer loop
# Columns in inner loop

# Ex: Iterating cars table and appending a 5th column (Price) value to
# every row
cars = [["Fiat", "124 Spider", 2017, 35],
        ["Nissan", "2005X", 1996, 26],
        ["BMW", "3 Series", 2015, 33],
        ["Mitsubishi", "3000GT", 1999, 22],
        ["Honda", "Odyssey", 2012, 22],
        ["Toyota", "Camry", 2009, 27]]

for r in range(len(cars)):
    cars[r].append(20000)

print(cars)

# Ex: Iterating cars table and printing every string we find in the table
for r in range(len(cars)):
    for c in range(len(cars[0])):
        if isinstance(cars[r][c], str):
            print(cars[r][c])

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


'''
User Input
-Get input from the user on-the-fly for more dynamic programs
'''

############ input() ############
# Main tool for user input is input()
# input() accepts a str as a parameter,
# and this string is displayed to the user.

# Ex: Capture the user's age and tell them if they can legally drink alcohol


def drinkingAgeProgram():
    user_age = input("What is your age?")
    print("User Age:", user_age)

    # MUST CAST input() RETURN VALUE TO THE TYPE YOU EXPECT IT TO BE.
    # IT IS ALWAYS `str` BY DEFAULT!
    print(type(user_age))
    user_age = int(user_age)

    if user_age >= 21:
        print("You can drink alochol!")
    else:
        print(
            "You must wait",
            21 - user_age,
            "years before you can drink alcohol!")

    return


drinkingAgeProgram()

'''
While Loops
-A condition-based way to iterate through data
-With for-loops, we had to concretely know/use a fixed range/length that we iterate through.
 -Ex: The range() function to use the length of a list
 -Ex: Iterate from 1 to some parameter n in the functions we wrote before like sum from 1 to n
-While loops give more freedom, but are also more tricky.
 -Much more likely to run into INFINITE LOOPS with while loops.
-For-loops took care of the iteration for us. We need to be explicit with that in while loops.
 -Ex: For-loops would always increment row value `r` by 1 after finishing what is in its body
'''

# Ex: Iterate from 1 to 10
i = 1
while i <= 10:
    print(i)
    i = i + 1

# Ex: Iterate through a 2-D List
numbers = [[4, 17, 9, 23],
           [283, 422, 839, 131],
           [36, 111, 113, 739]]

r = 0
while r < len(numbers):
    c = 0
    while c < len(numbers[0]):
        print(numbers[r][c], isPrime(numbers[r][c]))
        c = c + 1
    r = r + 1

############ Exercise ############
# Use a while loop to iterate through the cars data
# and print everytime we encounter a string.

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

############ input() + while-loops ############
# Using while-loops with input() is very powerful,
# and something you can't do with for-loops.
#
# Ex: Play a game with the user.
# User guesses a number from 1-10.
# We generate a random number from 1-10.
#
# If they match, the user wins that round.
# Otherwise, they lose that round.
#
# User can enter 'STOP' when they want to stop playing.


def guessingGame():
    playGame = True
    while playGame:
        user_guess = input(
            "Guess a number from 1 to 10. Type 'STOP' to exit. -->  ")
        if user_guess != 'STOP':
            if int(user_guess) == random.randint(1, 10):
                print("You win this round!")
            else:
                print("You lose this round!")
        else:
            playGame = False
            print("Thank you for playing!")
    return
