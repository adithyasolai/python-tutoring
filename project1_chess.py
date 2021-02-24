'''
Project 1: Chess
Written by Adithya Solai

Copyright © 2021 Adithya Solai. All rights are reserved.
You cannot use, modify, or redistribute this code without 
explicit permission from Adithya Solai.
'''

'''
In this project, students will model a chess board and chess piece movements using Python. 
This will require using all of the concepts learned in Lessons 1-3. Students are
recommended to use a 2-D list to model the chess board, and functions to organize the logic for
the movement patterns of each type of chess piece (Queen, King, Rook, etc.). However, the
implementation is left up to the student.

After modeling the chess board and chess pieces, the student’s code will take simple user input
that will attempt to place chess pieces on the chess board. The student’s code should remember
which pieces have been placed so far and figure out whether the user’s current piece can be
placed at the indicated square. If the indicated square is empty, the student’s code will place the
new piece on that square and remember that the square is occupied for future user input. At this
point, the student’s code will also calculate and print how many squares the new piece can move
based on its location, its piece type, and the vacancy of other squares on the chess board.

User input will be received in this format:
"<Piece Color> <Piece Name> <Square>"

Possible Piece Colors: White, Black
Possible Piece Names: Pawn, Knight, Bishop, Rook, Queen, King
Possible Squares: E4, G5, A7, etc 
(read how Chess square names work: https://en.wikipedia.org/wiki/Algebraic_notation_(chess) )

Example of User's interaction with the chess program:

What piece would you like to place, and where? --> White Bishop F2
White Bishop at F2 can move to 9 unique squares.
What piece would you like to place, and where? --> White Pawn A2
White Bishop at A2 can move to 2 unique squares.
What piece would you like to place, and where? --> Black Rook A1
Black Rook at A1 can move to 8 unique squares.
What piece would you like to place, and where? --> STOP
Thank you for playing!

Some more notes:
-You will always start off with an empty board every time the user starts your program.
-As you can see above, you need to factor in the cases where white pieces and black pieces
 can capture each other. Pieces with the same color can't capture each other. This will impact
 how many moves a given piece on the board can make. On an empty board, the Black Rook at A1
 should be able to move to 14 unique squares. However, the White Pawn on A2 is in its way,
 which limits the Rook's movement. However, the Rook can still capture the pawn, which should
 count as a move. If the Pawn was Black instead of White, the Rook would not be able to capture
 it, and would only have 7 possible moves.
-Read up on how Pawns move. They are the weirdest piece:
 -Pawns capture diagonally, but move straight forward. 
 -Pawns can not be placed on the top-most or bottom-most rows for this program, as that would
  involve promotion in some cases, which is more complex than we need to get.
 -https://en.wikipedia.org/wiki/Pawn_(chess)
-You can assume your user will always follow the format indicated above. They will either give
 a valid chess piece placement request, or type STOP.
-You don't need to worry about limiting the number of times a certain Piece is placed. In real
 chess, there can only be 2 White Rooks. In your program, it is fine if the user places more than
 2 White Rooks on the board.

CHALLENGE:
Add functionality for allowing users to move pieces that are already placed on the board.
You can decide how you want the user to format their input to indicate that they are moving an existing
piece instead of placing a new one. You can assume that the user will always follow your format.

'''
