from headers import *
from board import getboard
from alarmexception import AlarmException
from getch import _getChUnix as getChar



class Paddle:
    def __init__(self,x_cood,y_cood,flag,ballx,bally):
        self.x = x_cood
        self.y = y_cood
        self.flag = flag
        self.ballx =  ballx
        self.bally = bally
    
    def set_x(self,x):
        self.x=x
    def show_x(self):
        return self.x
    def set_y(self,y):
        self.y=y
    def show_y(self):
        return self.y

    def createpaddle(self):
        getboard.board[self.show_y()][self.show_x()] = '!'
        getboard.board[self.show_y()][self.show_x()+8] = '!'
        getboard.board[self.show_y()][self.show_x()+4] = 'o'
        for i in range(1,4):
            getboard.board[self.show_y()][self.show_x() + i] = '<'
        for i in range(5,8):
            getboard.board[self.show_y()][self.show_x() + i] = '>'

    def move_paddle(self):

        def alarmhandler(signum, frame):
            """input method"""
            raise AlarmException
        
        def user_input(timeout = 0.1):
            """input method"""
            signal.signal(signal.SIGALRM,alarmhandler)
            signal.setitimer(signal.ITIMER_REAL,timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''


        inp = user_input()

        #move right
        if inp == 'd':
            if getboard.board[self.show_y()][self.show_x()+11] == ' ':
                for i in range(0,9):
                    getboard.board[self.show_y()][self.show_x()+i] = ' '
                self.set_x(self.show_x() + 3)
            if self.flag == 0:
                getboard.board[self.show_y()-1][self.show_x()+1] = ' '
                getboard.board[self.show_y()-1][self.show_x()+4] = 'O'
            if self.flag == 1:
                getboard.board[self.show_y()-1][self.show_x()+4] = ' '
                self.bally = self.show_y()-1
                self.ballx = self.show_x()+4

        
        #move left
        if inp == 'a':
            if getboard.board[self.show_y()][self.show_x()-3] == ' ': 
                for i in range(0,9):
                    getboard.board[self.show_y()][self.show_x()+i] = ' '   
                self.set_x(self.show_x() - 3)
            if self.flag == 0:
                getboard.board[self.show_y()-1][self.show_x()+7] = ' '
                getboard.board[self.show_y()-1][self.show_x()+4] = 'O'
            if self.flag == 1:
                getboard.board[self.show_y()-1][self.show_x()+4] = ' '
                self.bally = self.show_y()-1
                self.ballx = self.show_x()+4
        
        if inp == 'q':
            os.system('clear')
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+"\t\t\t __   __  _______  __   __    _______  __   __  ___   _______ \n" +
              "\t\t\t|  | |  ||       ||  | |  |  |       ||  | |  ||   | |       |\n" +
              "\t\t\t|  |_|  ||   _   ||  | |  |  |   _   ||  | |  ||   | |_     _|\n" +
              "\t\t\t|       ||  | |  ||  |_|  |  |  | |  ||  |_|  ||   |   |   |  \n" +
              "\t\t\t|_     _||  |_|  ||       |  |  |_|  ||       ||   |   |   |  \n" +
              "\t\t\t  |   |  |       ||       |  |      | |       ||   |   |   |  \n" +
              "\t\t\t  |___|  |_______||_______|  |____||_||_______||___|   |___|  \n"+Style.RESET_ALL )
            quit()

        if inp == ' ':
            self.flag=1
            getboard.board[self.show_y()-1][self.show_x()+4] = ' '
            self.bally = self.show_y()-1
            self.ballx = self.show_x()+4

        
        

        getboard.board[self.show_y()][self.show_x()] = '!'
        getboard.board[self.show_y()][self.show_x()+8] = '!'
        getboard.board[self.show_y()][self.show_x()+4] = 'o'

        for i in range(1,4):
            getboard.board[self.show_y()][self.show_x() + i] = '<'
        for i in range(5,8):
            getboard.board[self.show_y()][self.show_x() + i] = '>'
    
    def expandpaddle(self,x,y):
        getboard.board[self.show_y()][self.show_x()] = '!'
        getboard.board[self.show_y()][self.show_x()+10] = '!'
        getboard.board[self.show_y()][self.show_x()+5] = 'o'
        for i in range(1,5):
            getboard.board[self.show_y()][self.show_x() + i] = '<'
        for i in range(6,8):
            getboard.board[self.show_y()][self.show_x() + i] = '>'

    def livesdecreased(self):
        for i in range(0,9):
                    getboard.board[self.show_y()][self.show_x()+i] = ' '
        Paddle(30,38,0,34,37)
        self.createpaddle()

getpaddle = Paddle(30,38,0,34,37)
