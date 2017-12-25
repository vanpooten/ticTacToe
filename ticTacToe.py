# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:38:34 2017

@author: vboyl
"""

def inputSize():
    '''
    prompts user to input integer for LxW of tic tac toe board
    returns: None if entry is invalid or integer n representing dimension of board
    '''
    try:
        n = int(input("What size board to you want to play? (3x3, 4x4, etc.): "))
    except (TypeError, ValueError):
        print("Must input an integer of 3 or more.")
        return None
    if n < 3:
        print("Must input an integer of 3 or more.")
        return None
    
    return n

def createBoard(n):
    '''
    n: integer that represents LxW of board
    returns: nested list representing board
    '''
    # 'p' represents placeholder
    board = [(['p'] * n) for i in range(n)]        
    return board

def printBoard(board):
    '''
    board: nested list representing tic tac toe board
    returns: None, prints tic tac toe board in a nice format
    '''
    padding = 3 * len(board) + (len(board) - 1)
    rowLen = len(board) + (len(board) - 1)
    
    for i in range(rowLen):
        if i % 2 == 1:
            print()
            print('{:-^{padding}}'.format('-', padding=padding))
            continue
        else:
            for j in range(rowLen):
                if j % 2 == 0:
                    # center padding '-' by padding determined above
                    if board[i//2][j//2] == 'p':
                        print('{:^3}'.format(' '), end='')  
                    else:
                        print('{:^3}'.format(board[i//2][j//2]), end='')
                else:
                    print('|', end='')
                    
def updateBoard(board, turn, x, y):
    '''
    board: nested list represent tic tac toe board
    turn: integer tracking number of turns in game
    x: row where user wants to place character, starting at 1
    y: column where user want to place character, starting at 1
    returns: None, mutates nested list in place
    '''
    if turn % 2 == 1:
        board[x-1][y-1] = 'X'
    else:
         board[x-1][y-1] = 'O'
         
def playerMove(board, turn):
    '''
    prompts user for row and column to place X or O
    board: nested list representing tic tac toe board
    turn: integer tracking number of turns in game
    returns: None if move invalid, or x and y as the row and column if move is valid
    '''
    if turn % 2 == 1:
        player = '1'
    else:
        player = '2'

    try:
        x, y  = [int(char) for char in input("Player {} enter a row, column (separated by a comma): ".format(player)).split(',')]
    except TypeError:
        print("Row and column must be integers, try again")
        return None
    except ValueError:
        print("Please be sure to separate row and column with a comma!")
        return None
    
    if x < 1 or y < 1:
        print("Row and column must be 1 or greater")
        return None
    if x > len(board) or y > len(board):
        print("This row or column doesn't exist! Try again")
        return None
    if board[x-1][y-1] != 'p':
        print("There's already a marker here! Try again.")
        return None
    
    return x, y
    
def validateWin(board, turn, x, y):
    '''
    board: nested list that represents board
    turn: number of turns taken so far
    returns: win, bool representing whether game is won or not
    '''
    if turn % 2 == 1:
        marker = 'X'
    else:
        marker = 'O'
    
    length = len(board)    
    win = False
    x -= 1
    y -= 1
    
    # loop row of marker
    for i in range(length):
        if board[x][i] != marker:
            break
        if i == length-1:
            win = True
    # loop column of marker
    for i in range(length):
        if board[i][y] != marker:
            break
        if i == length-1:
            win = True
    # loop left diagonal
    for i in range(length):
        if board[i][i] != marker:
            break
        if i == length-1:
            win = True
    # loop right diagonal
    for i in range(length):
        if board[i][length-1-i] != marker:
            break
        if i == length-1:
            win = True
        
    return win
    
def fullBoard(board):
    '''
    board: nested list that represents board
    tie: a bool representing if the game is tied or not
    '''    
    for row in board:
        if 'p' in row:
            return False

    return True

def game():
    '''
    master function that runs the tic tac toe game
    returns: int representing player that won the game
    '''
    turn = 1
    gameover = False
    full = False
    tie = False
    dimension = inputSize()
    
    while dimension == None:
        dimension = inputSize()
        
    gameBoard = createBoard(dimension) 
    print("Ok, let's begin!")
    
    while gameover == False and full == False:
        print("Here is the current board: \n")
        printBoard(gameBoard)
        print()
        
        move = playerMove(gameBoard, turn)
        while move == None:
            move = playerMove(gameBoard, turn)
        
        updateBoard(gameBoard, turn, move[0], move[1])
        gameover = validateWin(gameBoard, turn, move[0], move[1])
        full = fullBoard(gameBoard)

        turn += 1
    
    printBoard(gameBoard)
    print()
    
    player = 1
    if (turn-1) % 2 != 1:
        player = 2
    
    if full and not gameover:
        print("CATS. Nobody wins :(")
        tie = True
    else:
        print("Game over, player {} wins!".format(player))
        
    return player, tie
        
def multipleGames():
     
    cont = True
    player1wins = 0
    player2wins = 0
    gamesTied = 0
    gamesPlayed = 0
    
    while cont:
        win, tie = game()
        gamesPlayed += 1

        if tie:
            gamesTied += 1
        elif win == 1:
            player1wins += 1
        else:
            player2wins += 1
            
        userInput = input("Do you want to contiue (y/n)? ")
        
        while userInput != 'y' and userInput != 'n':
            print("Please enter 'y' or 'n'.")
            userInput = input("Do you want to contiue (y/n)? ")
            
        if userInput == 'n':
            print("Thanks for playing!")
            print("Games played: {}".format(gamesPlayed))
            print("Player 1 wins: {}".format(player1wins))
            print("Player 2 wins: {}".format(player2wins))
            print("Games drawn: {}".format(gamesTied))
            cont = False
        
multipleGames()
        
            
    
    

   
                    
