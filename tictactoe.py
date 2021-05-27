"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_count = 0
    o_count = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] == X:
                x_count += 1
            elif board[x][y] == O:
                o_count += 1
    if(x_count > o_count):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for x in range(3):
        for y in range(3):
            if board[x][y] == EMPTY:
                actions.add((x,y))
    
    if(len(actions) == 0):
        print("NONE!")
        return None
                
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if(board[action[0]][action[1]] != None):
        raise Exception()
    player1 = player(board)
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player1
    # print(new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check columns and rows
    for x in range(3):
        if(board[x][0] == board[x][1] and board[x][0] == board[x][2]):
            return board[x][0]
        elif(board[0][x] == board[1][x] and board[0][x] == board[2][x]):
            return board[0][x]
    
    #check diagonals
    if(board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        return board[0][0]
    if(board[2][0] == board[1][1] and board[2][0] == board[0][2]):
        return board[2][0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if(winner(board) != None):
        return True
    for x in range(3):
        for y in range(3):
            if(board[x][y] == None):
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    utility = winner(board)
    if(utility == X):
        return 1
    if(utility == O):
        return -1
    else:
        return 0

def minimize(board, move):
    if(terminal(board)):
        return utility(board), move
    v = [2, move]
    for action in actions(board):
        maxvalue = maximize(result(board,action),action)
        if(maxvalue[0] == -1):
            return [-1, action]

        v[0] = min(v[0],maxvalue[0])
        if(v[0] == maxvalue[0]):
            v[1] = action
    return v

def maximize(board, move):
    if(terminal(board)):
        return utility(board), move
    v = [-2, move]
    for action in actions(board):
        minvalue = minimize(result(board,action),action)
        
        if(minvalue[0] == 1):
            return [minvalue[0], action]
        v[0] = max(v[0],minvalue[0])

        if(v[0] == minvalue[0]):
            v[1] = action
      
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(player(board) == X):
        move = maximize(board, None)[1]
        return move
    elif(player(board) == O):
        move = minimize(board, None)[1]
        return move

