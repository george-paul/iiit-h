from headers import *
from board import getboard
from paddle import * 
class Powerup:
    def __init__(self,x,y,yv):
        self.x = x
        self.y = y
        self.yv = yv
    def setx(self, x):
        self._x=x
    def sety(self,y):
        self._y=y
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def decidepowerup(self):
        valrand = 1

#valrand=1
#yv = 1
class Expand():
    def __init__(self,x,y,yv):
        self.x = x
        self.y = y
        self.yv = yv
        #Powerup.__init__(self,x,y,yv)
        valrand=1
        if valrand == 1:
            getboard.board[self.y][self.x]='%'
            if self.y + self.yv < 52:
                if getboard.board[self.y+self.yv][self.x]==' ':
                    getboard.board[self.y][self.x]='%'
                    self.y = self.y + self.yv
                getboard.board[self.y][self.x]='%'
                if getboard.board[self.y+self.yv][self.x] == '!' or getboard.board[self.y+self.yv][self.x] == 'o' or getboard.board[self.y+self.yv][self.x] == '<' or getboard.board[self.y+self.yv][self.x] == '>':
                    Paddle.expandpaddle(self.x,self.y+self.yv)





