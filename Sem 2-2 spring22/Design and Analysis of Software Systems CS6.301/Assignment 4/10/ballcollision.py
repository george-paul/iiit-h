from headers import *
from ball import *

class Ballcollision(Ball):

    def __init__(self,x,y,Vx,Vy,lives,score):
        self.x = x
        self.y = y     
        self.xv = Vx
        self.yv = Vy
        self.lives = lives
        self.score = score
        Ball.__init__(self, x, y, Vx, Vy,lives,score)
    
    def get_lives():
        return self.lives
    
    def hit_wall(self,xv,yv,xv1,yv1):
        if abs(self.xv)>1 :
            self.xv=xv1
        else:
            self.xv = xv1*abs(self.xv)
        self.yv=yv1*abs(self.yv)
    
    def move_ball(self,xv,yv,xv1,yv1):
        self.xv = xv1*self.xv
        self.yv = yv1*self.yv
    
    def hit_paddle(self,xv,yv,xv1,yv1,flag):
        if flag==1:
            self.xv = xv1 + abs(self.xv)
            self.yv = yv1*abs(self.yv)
        if flag == 0:
            self.xv = xv1 - abs(self.xv)
            self.yv = yv1*abs(self.yv)

    def decreaselives(self):
        self.lives -= 1
        getboard.board[self.show_y()][self.show_x()] = ' '
                #getpaddle.livesdecreased()
        self.set_x(34)
        self.set_y(37)
        self.set_xv(1)
        self.set_yv(-1)
        if self.lives == 0:
            #os.system('clear')
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     "+Style.RESET_ALL)                 
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "  _____                         ____                 "+Style.RESET_ALL)                 
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ " / ____|                       / __ \                "+Style.RESET_ALL)              
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ "+Style.RESET_ALL)
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +"| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|"+Style.RESET_ALL)
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +"| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   "+Style.RESET_ALL)
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +" \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   "+Style.RESET_ALL)
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     "+Style.RESET_ALL)                 
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     "+Style.RESET_ALL)                 
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     "+Style.RESET_ALL)
            quit()
        else:
            BALL = Ball(getpaddle.show_x(),getpaddle.show_y(),1,-1,2,0)

    def moveball(self):
        

        if self.show_xv() > 0 and self.show_yv() < 0 and self.show_x()+ self.show_xv()<=77 and self.show_x()+ self.show_xv()>=3 :
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == ' ':
                self.move_ball(self.show_xv(),self.show_yv(),1,1)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '|':
                self.hit_wall(self.show_xv(),self.show_yv(),-1,-1)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '_' or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == 'o':
                self.hit_wall(self.show_xv(),self.show_yv(),1,1)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '<' or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '>':
                self.hit_paddle(self.show_xv(),self.show_yv(),1,1,1)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '!':
                self.hit_paddle(self.show_xv(),self.show_yv(),2,1,1)
        if self.show_xv() > 0 and self.show_yv() > 0 and self.show_x()+ self.show_xv()<=77 and self.show_x()+ self.show_xv()>=3 :
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == ' ':
                self.move_ball(self.show_xv(),self.show_yv(),1,1)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '|':
                self.hit_wall(self.show_xv(),self.show_yv(),-1,1)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '_':
                self.decreaselives()
            if  getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == 'o':
                self.hit_wall(self.show_xv(),self.show_yv(),1,-1)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '<' or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '>':
                self.hit_paddle(self.show_xv(),self.show_yv(),1,-1,1)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '!':
                self.hit_paddle(self.show_xv(),self.show_yv(),2,-1,1)
        if self.show_xv() < 0 and self.show_yv() < 0 and self.show_x()+ self.show_xv()<=77 and self.show_x()+ self.show_xv()>=2 and self.show_y() + self.show_yv()<=42  and self.show_y()+ self.show_yv()>=2:
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == ' ':
                self.move_ball(self.show_xv(),self.show_yv(),1,1)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '|':
                self.hit_wall(self.show_xv(),self.show_yv(),1,-1)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '_' or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == 'o':
                self.hit_wall(self.show_xv(),self.show_yv(),-1,1)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '<' or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '>':
                self.hit_paddle(self.show_xv(),self.show_yv(),-1,1,0)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '!':
                self.hit_paddle(self.show_xv(),self.show_yv(),-2,1,0)
        if self.show_xv() < 0 and self.show_yv() > 0 and self.show_x()+ self.show_xv()<=77 and self.show_x()+ self.show_xv()>=2  and self.show_y() + self.show_yv()<=42  and self.show_y()+ self.show_yv()>=2:
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == ' ':
                self.move_ball(self.show_xv(),self.show_yv(),1,1)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '|' :
                self.hit_wall(self.show_xv(),self.show_yv(),1,1)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '_':
                self.decreaselives()
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == 'o':
                self.hit_wall(self.show_xv(),self.show_yv(),-1,-1)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '<' or getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '>':
                self.hit_paddle(self.show_xv(),self.show_yv(),-1,-1,0)
            if getboard.board[self.show_y()+ self.show_yv()][self.show_x()+ self.show_xv()] == '!':
                self.hit_paddle(self.show_xv(),self.show_yv(),-2,-1,0)
        
        if self.show_x()+ self.show_xv()>77:
            if self.show_xv() > 0 and self.show_yv() > 0 :
                self.set_xv(-1*self.show_xv())
                self.set_yv(1*self.show_yv())
            if self.show_xv() > 0 and self.show_yv() < 0 :
                self.set_xv(-1*self.show_xv())
                self.set_yv(-1*self.show_yv())
        if self.show_x()+ self.show_xv()<2:
            if self.show_xv() < 0 and self.show_yv() < 0 :
                self.set_xv(1*self.show_xv())
                self.set_yv(-1*self.show_yv())
            if self.show_xv() < 0 and self.show_yv() > 0 :
                self.set_xv(1*self.show_xv())
                self.set_yv(1*self.show_yv())            

        if self.show_x()+ self.show_xv()<=77 and self.show_x()+ self.show_xv()>=2  and self.show_y() + self.show_yv()<=42 and self.show_y()+ self.show_yv()>=2:
            self.collision()   #collision
            getboard.board[self.show_y()][self.show_x()] = ' '
            self.set_x(self.show_x()+ self.show_xv())
            self.set_y(self.show_y()+ self.show_yv())
            getboard.board[self.show_y()][self.show_x()] = 'O'
    
getballcollision = Ballcollision(34,37,1,-1,5,0)

