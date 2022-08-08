from headers import *

class Board:
    def __init__(self):
        self.board = [[] for i in range(0,45)]
        for i in range(0,80):
            for j in range(0,45):
                self.board[j].append(' ')
        #    walls    
        for i in range (2,4):
            for j in range(2,43):
                self.board[j][i] = '|'
                self.board[j][80-i-1] = '|'
        
        for i in range(2,4):
            for j in range(2,78):
                self.board[i][j] = '_'
                self.board[45-i-1][j] = '_'
    
    def printboard(self):
        for i in range(0,45):
            print(*self.board[i])
        print()

getboard = Board()
