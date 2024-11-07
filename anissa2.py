# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 14:30:13 2024

@author: aniss
"""

import os
import time

# Initialisation du plateau de jeu 3x3
board = [[' ' for _ in range(3)] for _ in range(3)]
player = 1  # Le joueur 1 commence
Game = 0  # Jeu en cours
Mark = 'X'  # Le joueur 1 marque 'X'

# Conditions de victoire
Win = 1
Draw = -1
Running = 0

def DrawBoard():
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("-" * 5)
    print(" ")

def CheckPosition(x, y):
    if board[x][y] == ' ':
        return True
    return False

def get_player_input():
    while True:
        try:
            choice = int(input("Enter the position between [1-9] where you want to mark: "))
            row, col = (choice - 1) // 3, (choice - 1) % 3
            if choice < 1 or choice > 9:
                print("Invalid position! Please enter a number between 1 and 9.")
            elif not CheckPosition(row, col):
                print("This position is already taken. Choose another one.")
            else:
                return row, col
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

def CheckWin():
    global Game
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],  # Ligne 1
        [(1, 0), (1, 1), (1, 2)],  # Ligne 2
        [(2, 0), (2, 1), (2, 2)],  # Ligne 3
        [(0, 0), (1, 0), (2, 0)],  # Colonne 1
        [(0, 1), (1, 1), (2, 1)],  # Colonne 2
        [(0, 2), (1, 2), (2, 2)],  # Colonne 3
        [(0, 0), (1, 1), (2, 2)],  # Diagonale 1
        [(0, 2), (1, 1), (2, 0)],  # Diagonale 2
    ]
    
    for condition in win_conditions:
        if board[condition[0][0]][condition[0][1]] == board[condition[1][0]][condition[1][1]] == board[condition[2][0]][condition[2][1]] and board[condition[0][0]][condition[0][1]] != ' ':
            Game = Win
            return

    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        Game = Draw

def main_menu():
    print("Tic-Tac-Toe Game!")
    print("1. Start Game")
    print("2. Exit")
    choice = input("Choose an option: ")
    return choice

def play_game():
    global player, Mark, Game
    while Game == Running:
        os.system('cls')
        DrawBoard()

        if player % 2 != 0:
            print("Player 1's chance (X)")
            Mark = 'X'
        else:
            print("Player 2's chance (O)")
            Mark = 'O'

        row, col = get_player_input()
        board[row][col] = Mark
        player += 1
        CheckWin()

    os.system('cls')
    DrawBoard()
    
    if Game == Draw:
        print("Game Draw!")
    elif Game == Win:
        player -= 1
        if player % 2 != 0:
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")

if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == "1":
            Game = Running
            play_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
