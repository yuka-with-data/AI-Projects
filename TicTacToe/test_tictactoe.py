""" 
Tic tac toe game Pytest
 """
import pytest
from tictactoe import *

# Test initial_state()
def test_initial_state():
    assert initial_state() == [[EMPTY, EMPTY, EMPTY],
                               [EMPTY, EMPTY, EMPTY],
                               [EMPTY, EMPTY, EMPTY]]
    
# Test player()
def test_player():
    assert player([[EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY]]) == X
    assert player([[EMPTY, EMPTY, EMPTY],
                   [EMPTY, X, EMPTY],
                   [EMPTY, EMPTY, EMPTY]]) == O
    
# Test actions()
def test_actions():
    board = [[O, X, X],
             [EMPTY, O, EMPTY],
             [X, EMPTY, EMPTY]]
    assert actions(board) == {(1,0),(1,2),(2,1),(2,2)}

# Test result()
def test_result():
    board = [[X, EMPTY, O],
             [O, EMPTY, EMPTY],
             [EMPTY, X, EMPTY]]
    action = (1,1)
    expected_board = [[X, EMPTY, O],
                    [O, X, EMPTY],
                    [EMPTY, X, EMPTY]]
    result(board, action) == expected_board

# Test winner()
def test_winner():
    board = [[O, X, X],
             [EMPTY, O, EMPTY],
             [X, EMPTY, O]]
    assert winner(board) == O

    board = [[X, X, X],
             [EMPTY, O, O],
             [X, EMPTY, O]]
    assert winner(board) == X

# Test terminal()
def test_terminal():
    board = [[X, EMPTY, O],
             [O, X, EMPTY],
             [EMPTY, O, X]]
    assert terminal(board) == True

    board = [[X, O, O],
             [O, X, X],
             [X, O, O]]
    assert terminal(board) == True

# Test utility()
def test_utility():
    board = [[X, EMPTY, O],
             [O, X, EMPTY],
             [EMPTY, O, X]]
    assert utility(board) == 1

    board = [[O, X, X],
             [EMPTY, O, EMPTY],
             [X, EMPTY, O]]
    assert utility(board) == -1

    board = [[X, O, O],
             [O, X, X],
             [X, O, O]]
    assert utility(board) == 0

# Test minimax()