"""
Tic Tac Toe Player
"""

import math
import copy
import sys

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    no_of_Os = 0
    no_of_Xs = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                no_of_Xs += 1
            elif board[row][col] == "O":
                no_of_Os += 1
    
    if no_of_Os == 0 and no_of_Xs == 0:
        return "X"
    elif no_of_Os > no_of_Xs:
        return "X"
    elif no_of_Os == no_of_Xs:
        return "X"
    elif no_of_Xs > no_of_Os:
        return "O"
    
    return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] != "X" and board[row][col] != "O":
                possible_moves.add((row, col))
    
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action

    if (row > 2 or row < 0) and (col > 2 or col < 0):
        raise ValueError(f"The given values of action {action}, are out of range for the board!")
    elif board[row][col] != EMPTY:
        raise ValueError(f"The location {action} is not EMPTY!")
    
    player_to_move = player(board)

    copied_board = [[cell for cell in rows] for rows in board]

    copied_board[row][col] = player_to_move

    return copied_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    res = winner(board)

    if res != None:
        return True
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    response = winner(board)

    if response == "X":
        return 1
    elif response == "O":
        return -1
    else:
        return 0

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -sys.maxsize - 1
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = sys.maxsize
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    # Means we are maximizing
    if current_player == "X":
        best_value = -sys.maxsize -1
        best_action = None

        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
    elif current_player == "O":
        best_value = sys.maxsize
        best_action = None

        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_action
