from headers import *
from board import getboard
from brick import getbrick
from colors import *
from powerup import *
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from paddle import *
class Ball:

    def __init__(self, x, y, Vx, Vy,lives,score):
        self.x = x
        self.y = y
        self.xv = Vx
        self.yv = Vy
        self.lives = lives
        self.score = score
    
    
    def set_x(self,x):
        self.x=x
    def show_x(self):
        return self.x
    def set_y(self,y):
        self.y=y
    def show_y(self):
        return self.y
    def set_xv(self,x):
        self.xv=x
    def show_xv(self):
        return self.xv
    def set_yv(self,y):
        self.yv=y
    def show_yv(self):
        return self.yv
    
    def get_distance(self,x,y):
        return self.x+self.y
    
    def createball(self):
        getboard.board[self.show_y()][self.show_x()] = 'O'
    flag = 0
    
    def explodable(self):
        for i in range(21,56):
            getboard.board[14][i] = ' '
        for i in range(16,36):
            getboard.board[13][i] = ' '
        for i in range(41,61):
            getboard.board[13][i] = ' '
        for i in range(16,31):
            getboard.board[12][i] = ' '
        for i in range(46,61):
            getboard.board[12][i] = ' '
        for i in range(16,26):
            getboard.board[11][i] = ' '
        for i in range(51,61):
            getboard.board[11][i] = ' '
        for i in range(26,51):
            getboard.board[15][i] = ' '
        for i in range(31,46):
            getboard.board[16][i] = ' '
        for i in range(36,41):
            getboard.board[17][i] = ' '
        

    
    
    def collision(self):
        #collision
        if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.LIGHTGREEN_EX+"("+Back.RESET or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.LIGHTGREEN_EX+")"+Back.RESET or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.LIGHTGREEN_EX+"$"+Back.RESET or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.LIGHTCYAN_EX+"("+Back.RESET or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.LIGHTCYAN_EX+")"+Back.RESET or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.LIGHTCYAN_EX+"$"+Back.RESET or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.RED+"("+Back.RESET or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.RED+")"+Back.RESET or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.RED+"$"+Back.RESET or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.BLACK+"("+Back.RESET or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.BLACK+")"+Back.RESET or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.BLACK+"$"+Back.RESET :
            
            reminder = (self.show_x() + self.show_xv()) % 5
            if reminder == 0:
                reminder = reminder + 5
            
            if getbrick.power[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv() + 5 - reminder] > 0:
                if getbrick.power[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv() + 5 - reminder] <= 3:
                    self.score = self.score + 10*getbrick.power[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv() + 5 - reminder]
                getbrick.power[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv() + 5 - reminder] = getbrick.power[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv() + 5 - reminder]  - 1
                if getbrick.power[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()+ 5 - reminder] == 1:
                    for i in range(0,5):
                        getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv() - i+ 5 - reminder]=' '
                    getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()+ 5 - reminder]=Back.LIGHTGREEN_EX+")"+Back.RESET
                    getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()+ 5 - reminder-4]=Back.LIGHTGREEN_EX+"("+Back.RESET
                    for i in range(1,4):
                        getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()+ 5 - reminder - i]=Back.LIGHTGREEN_EX+"$"+Back.RESET
                if getbrick.power[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()+ 5 - reminder] == 2:
                    for i in range(0,5):
                        getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv() - i+ 5 - reminder]=' '
                    getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()+ 5 - reminder]=Back.LIGHTCYAN_EX+")"+Back.RESET
                    getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()-4+ 5 - reminder]=Back.LIGHTCYAN_EX+"("+Back.RESET
                    for i in range(1,4):
                        getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv() + 5 - reminder- i]=Back.LIGHTCYAN_EX+"$"+Back.RESET
                if getbrick.power[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()+ 5 - reminder] == 3:
                    for i in range(0,5):
                        getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv() - i+ 5 - reminder]=' '
                    getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()+ 5 - reminder]=Back.RED+")"+Back.RESET
                    getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()-4+ 5 - reminder]=Back.RED+"("+Back.RESET
                    for i in range(1,4):
                        getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv() - i+ 5 - reminder]=Back.RED+"$"+Back.RESET
                if getbrick.power[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv() + 5 - reminder] == float("inf"):
                    for i in range(0,5):
                        getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv() - i+ 5 - reminder]=' '
                    getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()+ 5 - reminder]=Back.BLACK+")"+Back.RESET
                    getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()+ 5 - reminder-4]=Back.BLACK+"("+Back.RESET
                    for i in range(1,4):
                        getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()+ 5 - reminder - i]=Back.BLACK+"$"+Back.RESET
                if getbrick.power[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()+ 5 - reminder] == 0:
                    for i in range(0,5):
                        getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv() - i+ 5 - reminder]=' '
                
            if self.show_xv() > 0 and self.show_yv() > 0:
                self.set_xv(1*abs(self.show_xv()))
                self.set_yv(-1*abs(self.show_yv()))
            if self.show_xv() > 0 and self.show_yv() < 0:
                self.set_xv(1*abs(self.show_xv()))
                self.set_yv(1*abs(self.show_yv()))
            if self.show_xv() < 0 and self.show_yv() > 0:
                self.set_xv(-1*abs(self.show_xv()))
                self.set_yv(-1*abs(self.show_yv()))
            if self.show_xv() < 0 and self.show_yv() < 0:
                self.set_xv(-1*abs(self.show_xv()))
                self.set_yv(1*abs(self.show_yv()))    
                    
        if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.YELLOW+"("+Back.RESET or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.YELLOW+")"+Back.RESET or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == Back.YELLOW+"$"+Back.RESET :
            self.score = self.score + 100
            self.explodable()

            #Expand(self.show_x()+ self.show_xv(),self.show_y()+ self.show_yv(),1)
            if self.show_xv() > 0 and self.show_yv() > 0:
                self.set_xv(1*abs(self.show_xv()))
                self.set_yv(-1*abs(self.show_yv()))
            if self.show_xv() > 0 and self.show_yv() < 0:
                self.set_xv(1*abs(self.show_xv()))
                self.set_yv(1*abs(self.show_yv()))
            if self.show_xv() < 0 and self.show_yv() > 0:
                self.set_xv(-1*abs(self.show_xv()))
                self.set_yv(-1*abs(self.show_yv()))
            if self.show_xv() < 0 and self.show_yv() < 0:
                self.set_xv(-1*abs(self.show_xv()))
                self.set_yv(1*abs(self.show_yv()))

        



                



