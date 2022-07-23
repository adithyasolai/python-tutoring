'''
Problem Set 3 Answer Key
Written by Adithya Solai
'''

## Problem 1 ##
# Insert a column in the middle of the data set below with all 0s
data = [[  1,   7, 23,  43],
        [ 90,  -6, 23, -56],
        [-99, -73, 69,  29],
        [100,  71, 18,  88]]

# Write code here

for row in data:
  row.insert(2, 0)

# Store your final 2-D list in `studentAnswer` for the assert below
studentAnswer = data

answer = [[  1,   7, 0, 23,  43],
          [ 90,  -6, 0, 23, -56],
          [-99, -73, 0, 69,  29],
          [100,  71, 0, 18,  88]]

assert studentAnswer == answer

#-----------------------------------------------------------------------

## Problem 2 ##
# Change all integers on the main diagonal (top left to bottom right) to 999
# Change all integers on the minor diagonal (top right to bottom left) to -999
# (Make the intersection of the diagonals at the center equal to 1000)
# (See the `answer` 2-D list below for more clarity)
# (Hint: Use Python's built-in insert() function for lists)

data = [[ 1,     7,   0,  23,  43],
        [ 90,   -6,   0,  23, -56],
        [-99,  -73,   0,  69,  29],
        [100,   71,   0,  18,  88],
        [ 77,   34, -43, -88,   0]]

# Write code here
for r in range(len(data)):
  for c in range(len(data[r])):
    if r == c:
      # Main Diagonal
      data[r][c] = 999
    elif len(data[r]) - r - 1 == c:
      # Minor Diagonal
      data[r][c] = -999

    if r == c and r == len(data) // 2 and c == len(data[r]) // 2:
      data[r][c] = 1000

# Store your final 2-D list in `studentAnswer` for the assert below
studentAnswer = data

answer = [[ 999,     7,    0,   23, -999],
          [  90,   999,    0, -999,  -56],
          [ -99,   -73, 1000,   69,   29],
          [ 100,  -999,    0,  999,   88],
          [-999,    34,  -43,  -88,  999]]

assert studentAnswer == answer

#-----------------------------------------------------------------------

## Problem 3 ##
# Transpose the 2-D list below. (Flipping Rows & Columns)
# (Read more here: https://mathinsight.org/matrix_transpose)
data = [[ 999,     7,    0,   23, -999],
        [  90,   999,    0, -999,  -56],
        [ -99,   -73, 1000,   69,   29],
        [ 100,  -999,    0,  999,   88],
        [-999,    34,  -43,  -88,  999]]

# Write code here
transposed = []

for c in range(len(data[0])):
  new_row = []
  for r in range(len(data)):
    new_row.append(data[r][c])
  transposed.append(new_row)

# Store your final 2-D list in `studentAnswer` for the assert below
studentAnswer = transposed

answer = [[ 999,    90,  -99,  100, -999],
          [   7,   999,  -73, -999,   34],
          [   0,     0, 1000,    0,  -43],
          [  23,  -999,   69,  999,  -88],
          [-999,   -56,   29,   88,  999]]

assert studentAnswer == answer

#-----------------------------------------------------------------------

## Problem 4 ##
# Return the sum of all non-main-diagonal integers in the matrix below.
# The main diagonal runs from top-left to bottom-right.
data = [[ 999,     7,    0,   23, -999],
        [  90,   999,    0, -999,  -56],
        [ -99,   -73, 1000,   69,   29],
        [ 100,  -999,    0,  999,   88],
        [-999,    34,  -43,  -88,  999]]

# Write code here
total = 0
for r in range(len(data)):
  for c in range(len(data[r])):
    if r != c:
      total += data[r][c]

# Store your final 2-D list in `studentAnswer` for the assert below
studentAnswer = total

answer = -3915

assert studentAnswer == answer

#-----------------------------------------------------------------------

## Problem 5 ##
# Use input() + while-loops to design a Rock-Paper-Scissors game.
# Randomly-generate a move for the computer
# The student can decide how to format the user input, and can expect that 
# the user will always follow that format.
#
# This will be evaluated manually by just playing the game a bunch of times.
import random

def RPS():
  playGame=True
  while playGame == True:
    user_guess = input("Rock, Paper, or Scissors? Type 'STOP' to exit. -->  ")
    if user_guess != 'STOP':
      computer_num = random.randint(1,3)

      # Convert number to a RPS move
      computer_guess = None
      if computer_num == 1:
          computer_guess = "Rock"
      elif computer_num == 2:
          computer_guess = "Paper"
      else: # Scissors
          computer_guess = "Scissors"

      # Decide winner of the round
      if user_guess == computer_guess:
          print("Tie!")
      elif (user_guess == "Rock" and computer_guess == "Scissors") or (user_guess == "Paper" and computer_guess == "Rock") or (user_guess == "Scissors" and computer_guess == "Paper"):
          print("You win! Computer picked", computer_guess)
      else:
          print("You lose! Computer picked", computer_guess)
    else:
        playGame = False
        print("Thank you for playing!")
  return

#-----------------------------------------------------------------------

print("All Normal Exercises Completed with all Test Cases passed!")

#-----------------------------------------------------------------------

## Challenge Problem 1 ##
# Write a function for matrix multiplication A * B.
# You can assume matrix A has dimensions m x n,
# and matrix B has dimensions n x p, where m, n, and p >= 1.
# Matrix A & B are represented using 2-D lists.
#
# Example of Matrix Multiplication:
# A = [[2, 4, 6],
#      [1, 1, 1],
#      [5, 5, 5]]
#
# B = [[5, 7],
#      [1, 0],
#      [0, 2]]
#
# A * B = 
#
# Linear Combination of Row 0 of Matrix A with Col 0 of Matrix B:
# (2 x 5) + (4 x 1) + (6 x 0) = 14
# ^^ 14 is now the value at Row 0 Col 0 of the resulting Matrix ^^
#
# Linear Combination of Row 0 of Matrix A with Col 1 of Matrix B:
# (2 x 7) + (4 x 0) + (6 x 2) = 26
# ^^ 26 is now the value at Row 0 Col 1 of the resulting Matrix ^^
#
# Linear Combination of Row 1 of Matrix A with Col 0 of Matrix B:
# (1 x 5) + (1 x 1) + (1 x 0) = 6
# ^^ 6 is now the value at Row 1 Col 0 of the resulting Matrix ^^
#
# Linear Combination of Row 1 of Matrix A with Col 1 of Matrix B:
# (1 x 7) + (1 x 0) + (1 x 2) = 9
# ^^ 9 is now the value at Row 0 Col 0 of the resulting Matrix ^^
#
# Linear Combination of Row 2 of Matrix A with Col 0 of Matrix B:
# (5 x 5) + (5 x 1) + (5 x 0) = 30
# ^^ 30 is now the value at Row 0 Col 0 of the resulting Matrix ^^
#
# Linear Combination of Row 2 of Matrix A with Col 1 of Matrix B:
# (5 x 7) + (5 x 0) + (5 x 2) = 45
# ^^ 45 is now the value at Row 0 Col 0 of the resulting Matrix ^^
#
# Final Result: A 3 x 2 matrix
#
# [[14, 26],
#  [ 6,  9],
#  [30, 45]]
#

def matrix_mult(A, B):
  m = len(A)
  n = len(A[0])
  p = len(B[0])

  # Initialize an empty result matrix
  C = []
  for r in range(m):
    C.append([0] * p)

  for r in range(len(A)):
    for c in range(len(B[0])):
      # linear combination of row r in A and col c in B
      cell_val = 0
      for i in range(n):
        cell_val += A[r][i] * B[i][c]

      C[r][c] = cell_val

  return C


A = [[2, 4, 6],
     [1, 1, 1],
     [5, 5, 5]]

B = [[5, 7],
     [1, 0],
     [0, 2]]

answer = [[14, 26],
          [6,   9],
          [30, 45]]

assert matrix_mult(A,B) == answer

A = [[ 5, -3,  2],
     [-2,  0,  1],
     [-2,  8, -3]]

B = [[ 1,  0,  1],
     [-1,  3,  0],
     [ 2,  1, -3]]

answer = [[ 12, -7,  -1],
          [  0,  1,  -5],
          [-16, 21,   7]]

assert matrix_mult(A,B) == answer

print("All Challenge Exercises Completed with all Test Cases passed!")