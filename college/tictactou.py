# Define the game board
import tkinter
from tkinter import *

board = [' ' for i in range(9)]
5

# Print the game board
def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

# Function to check if a player has won
def check_win(player):
    if board[0] == board[1] == board[2] == player:
        return True
    elif board[3] == board[4] == board[5] == player:
        return True
    elif board[6] == board[7] == board[8] == player:
        return True
    elif board[0] == board[3] == board[6] == player:
        return True
    elif board[1] == board[4] == board[7] == player:
        return True
    elif board[2] == board[5] == board[8] == player:
        return True
    elif board[0] == board[4] == board[8] == player:
        return True
    elif board[2] == board[4] == board[6] == player:
        return True
    else:
        return False

# Function to play the game
def play_game():
    player = 'X'
    while True:
        print_board()
        move = input("It's " + player + "'s turn. Enter a number between 1 and 9: ")
        move = int(move) - 1
        if board[move] == ' ':
            board[move] = player
            if check_win(player):
                print_board()
                print(player + ' has won!')
                break
            if ' ' not in board:
                print_board()
                print('The game is a tie!')
                break
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        else:
            print('That space is already taken!')

# Play the game
play_game()
# Define the game board
board = [' ' for i in range(9)]

# Print the game board
def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

# Function to check if a player has won
def check_win(player):
    if board[0] == board[1] == board[2] == player:
        return True
    elif board[3] == board[4] == board[5] == player:
        return True
    elif board[6] == board[7] == board[8] == player:
        return True
    elif board[0] == board[3] == board[6] == player:
        return True
    elif board[1] == board[4] == board[7] == player:
        return True
    elif board[2] == board[5] == board[8] == player:
        return True
    elif board[0] == board[4] == board[8] == player:
        return True
    elif board[2] == board[4] == board[6] == player:
        return True
    else:
        return False

# Function to play the game
def play_game():
    player = 'X'
    while True:
        print_board()
        move = input("It's " + player + "'s turn. Enter a number between 1 and 9: ")
        move = int(move) - 1
        if board[move] == ' ':
            board[move] = player
            if check_win(player):
                print_board()
                print(player + ' has won!')
                break
            if ' ' not in board:
                print_board()
                print('The game is a tie!')
                break
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        else:
            print('That space is already taken!')

# Play the game
play_game()
