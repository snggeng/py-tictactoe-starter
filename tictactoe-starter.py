# Tic Tac Toe

import random

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)


def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    # the first element in the tuple is the player's letter, the second is the computer's letter.


def whoGoesFirst():
    # Randomly choose the player who goes first.

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.


def makeMove(board, letter, move):


def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.


def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.

def getPlayerMove(board):
    # Let the player type in his move.

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.


def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.


    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move


    # Check if the player could win on his next move, and block them.


    # Try to take one of the corners, if they are free.


    # Try to take the center, if it is free.


    # Move on one of the sides.


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.

    # Reset the board
    # Check playing conditions
            # Player's turn.
            # Computer's turn.
