'''
Problem Set 4
Written by Adithya Solai

Copyright © 2021 Adithya Solai. All rights are reserved.
You cannot use, modify, or redistribute this code without 
explicit permission from Adithya Solai.
'''

## Problem 1 ##
# Find the most frequent character in a given string
# (Hint: Use dictionaries to keep track of character frequencies)
# In the case of a tie, it doesn't matter which character you return.

def mostFrequentChar(s):
  return 0

assert mostFrequentChar("ababcbacadefegdehijhklij") == 'a'
assert mostFrequentChar("yyqakaaeiflcwyyyqspaqy") == 'y'
assert mostFrequentChar("wvvw") in ['w', 'v']

#-----------------------------------------------------------------------

## Problem 2 ##
# Determine if two strings are anagrams using dictionaries.
# Anagrams are two strings that use the same characters and same frequency
# of each character. Look at the test cases for examples.

def isAnagram(s1, s2):
  return 0

assert isAnagram("aalss", "salsa") == True
assert isAnagram("laap", "pal") == False
assert isAnagram("listen", "silent") == True

#-----------------------------------------------------------------------

## Problem 3 ##
# Design a Pokedex class that stores data about Pokemon.
#
# Data that you receive about each Pokemon:
# -Pokedex ID (unique to each Pokemon) (int)
# -Name (string)
# -Number of Moves (int)
# -Evolutions (list of Pokedex IDs)
# -Pre-volutions (list of Pokedex IDs)
#
# Functionality that your Pokedex must support:
# -Add a Pokemon
# -Edit a Pokemon's Number of Moves
# -Remove a Pokemon
# -Get a Pokemon's Number of Moves (int)
# -Get the names of all evolutions for a given Pokemon (list of strings)
# -Get the names of all pre-volutions for a given Pokemon (list of strings)
#
# Since there are different ways to implement this, testing will be done manually
# by the instructor.

class Pokedex():
  def __init__(self):
    return 0

# Data format: [Pokedex ID, Name, # of Moves, Evolutions, Pre-volutions]
# Add this data to the Pokedex:
# [4, "Charmander", 40, [5, 6], []]
# [5, "Charmeleon", 55, [6], [4]]
# [6, "Charizard", 67, [], [4, 5]]
# [417, "Pachirisu", 33, [], []]
# [163, "Hoothoot", 25, [164], []]
# [164, "Noctowl", 50, [], [163]]
#
# Some actions to try out after adding the data:
# 1. Print the names of all of Charmander's (ID 4) evolutions (should be Charmeleon & Charizard)
# 2. Remove Charizard (ID 6) from the database
# 3. Repeat step 1, Charizard should be gone.
# 4. Print Pachirisu's (ID 417) # of moves, change it to something else, and print again to check
# 5. Print the names of Noctowl's (ID 163) pre-volutions (should be just Hoothoot)

#-----------------------------------------------------------------------

print("All Normal Exercises Completed with all Test Cases passed!")

#-----------------------------------------------------------------------

## Challenge Problem 1 ##
# Given a string of characters, figure out the maximum number of partitions
# of this string such that each unique character only appears in one partition.
#
# Ex: Given string S = "ababcbacadefegdehijhklij"
#
# One possible partition of the string is:
# p1 = "ababcbacadefegde"
# p2 = "hijhklij"
# This partition is valid because 'a' is only in p1, 'h' is only in p2, etc.
#
# However, the correct answer is:
# p1 = "ababcbaca"
# p2 = "defegde"
# p3 = "hijhklij"
#
# The second group of partitions follow the same rules about unique characters only
# being in one partition. However, the second group has 3 partitions, and the first
# group only has 2 partitions, so the second grouping is correct.

def partitionString(s):
  return 0

assert partitionString("ababcbacadefegdehijhklij") == ["ababcbaca", "defegde", "hijhklij"]
assert partitionString("abcdefgghijh") == ["a", "b", "c", "d","e", "f", "gg", "hijh"]
assert partitionString("wwfv") == ["ww", "f", "v"]

#-----------------------------------------------------------------------

print("All Challenge Exercises Completed with all Test Cases passed!")