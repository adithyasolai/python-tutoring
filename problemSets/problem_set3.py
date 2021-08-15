'''
Problem Set 3
Written by Adithya Solai

Copyright © 2021 Adithya Solai. All rights are reserved.
You cannot use, modify, or redistribute this code without 
explicit permission from Adithya Solai.
'''

## Problem 1 ##
# Insert a column in the middle of the data set below with all 0s
# Hint: Use Python's built-in insert() function for lists. (Google this if you don't know it.)
# You must use a for loop!
data = [[  1,   7, 23,  43],
        [ 90,  -6, 23, -56],
        [-99, -73, 69,  29],
        [100,  71, 18,  88]]

# Write code here

# Store your final 2-D list in `studentAnswer` for the assert below
studentAnswer = None

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
# You must use a for loop!

data = [[ 1,     7,   0,  23,  43],
        [ 90,   -6,   0,  23, -56],
        [-99,  -73,   0,  69,  29],
        [100,   71,   0,  18,  88],
        [ 77,   34, -43, -88,   0]]

# Write code here

# Store your final 2-D list in `studentAnswer` for the assert below
studentAnswer = None

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

# Store your final 2-D list in `studentAnswer` for the assert below
studentAnswer = None

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

# Store your final 2-D list in `studentAnswer` for the assert below
studentAnswer = None

answer = -3915

assert studentAnswer == answer

#-----------------------------------------------------------------------

## Problem 5 ##
# Use input() + while-loops to design a Rock-Paper-Scissors game.
# Randomly-generate a move for the computer.
# The student can decide how to format the user input, and can expect that 
# the user will always follow that format.
#
# This will be evaluated manually by just playing the game a bunch of times.
import random

def RPS():
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
# Read More: https://www.mathsisfun.com/algebra/matrix-multiplying.html
#

def matrix_mult(A, B):
    return 0

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

## Challenge Problem 2 ##
# Use input() + while-loops to design a Blackjack game.
# Read the rules of Blackjack here: https://bicyclecards.com/how-to-play/blackjack/
# Play a few rounds here to get a feel for the game: https://games.washingtonpost.com/games/blackjack
#
# Notes:
# -You only need to account for Hit and Stand. You don't need to implement splitting and doubling bets
# -User starts with $1000. You must remember and update this value as the user plays more rounds.
# -If the user ever hits $0, you must immediately stop the game.
# -Assume every round the user bets $100. If they win, the user gets an additional $100 to their total.
#  If they lose, they lose $100. If they tie, they don't lose or gain any money.
# -You can keep it simple and count Ace only as 11, instead of both 1 and 11 like in real Blackjack.
# -You don't need to worry about printing suits (Clubs, Spades, Diamonds, Hearts) and ranks (Jack, Queen, King, Ace). 
#  You can just use the integer values to represent the cards:
#  2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, and 11. (There are four 10s b/c 10, Jack, Queen, and King all have a value of 10)
#
# ** This will be evaluated manually by playing a bunch of rounds and reading your code. **
# 
#
# EXTRA CHALLENGE:
# Implement the things that you didn't have to worry about before (Suits, Ranks, Ace dual-values, Splitting & Double-Bet, etc.)
# These new features will likely require using Object-Oriented design with user-defined classes. This will be covered in Lesson 4.

#-----------------------------------------------------------------------

print("All Challenge Exercises Completed with all Test Cases passed!")