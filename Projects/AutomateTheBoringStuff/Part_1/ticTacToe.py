
# This program represents the data structure representing a Tic-Tac-Toe board

theBoard = {'top-L': 'O', 'top-M': 'X', 'top-R': 'X',
            'mid-L': 'X', 'mid-M': 'O', 'mid-R': 'O',
            'low-L': 'X', 'low-M': 'X', 'low-R': 'O'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)