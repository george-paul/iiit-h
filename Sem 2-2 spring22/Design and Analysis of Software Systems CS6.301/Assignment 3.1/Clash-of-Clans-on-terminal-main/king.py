import time
import colorama
from colorama import Fore, Back, Style
import math 
# custom modules
from extra import healthCOLOR_king, ROWS, COLS,X0, Y0



class King():

    def __init__(self, village,health, width):
        self.village = village
        self.x = X0  # (x, y) are coordinates of the centre
        self.y = Y0
        self.v = 1
        self.color = Back.BLUE
        self.char = 'B'
        self.attack = False
        self.health = health
        self.color = healthCOLOR_king[health%len(healthCOLOR_king)]
        self.facing = (0,0)
        self.atk = 4
        self.turns =1

    def reset(self):
        self.x = X0
        self.y = Y0

    def moveX(self, dirn=1):
        for i in range(self.turns):
            x = self.x
            self.facing = (dirn,0)
            if (x >= COLS-1  and dirn == 1):
                return
            if (x  <= 1 and dirn == -1):
                return
            if(Fore.GREEN not in (self.village.layout[self.y][self.x + self.v*dirn])):
                return
            self.village.layout[self.y][self.x] = Fore.GREEN +  "_" + Style.RESET_ALL
            self.x += self.v*dirn
    
    def moveY(self, dirn = 1):
        for i in range(self.turns):
            y = self.y
            self.facing = (0,dirn)
            if (y >= ROWS-1  and dirn == 1):
                return
            if (y  < 1 and dirn == -1):
                return
            if(Fore.GREEN not in (self.village.layout[self.y + self.v*dirn][self.x])):
                return


            self.village.layout[self.y][self.x] = Fore.GREEN + "_" + Style.RESET_ALL
            self.y += self.v*dirn


    def display(self):
        y = self.y
        x = self.x
        arr = self.village.layout
        if (x   <= 0):
            x = 0
        elif (x  >= COLS-1):
            x = COLS-1 
        if self.attack:
            self.color = Back.WHITE
        else:
            self.color = healthCOLOR_king[self.health%len(healthCOLOR_king)]
        
        arr[self.y][self.x] = self.color + self.char + Style.RESET_ALL
        self.village.layout = arr
    
    def attacking(self):
        #self.attack = True
        wallobj = self.village.wallarr[0]

        if( "W" in self.village.layout[self.y+ self.facing[1]][self.x+self.facing[0]]):
            print("BOOM")
            #self.attack = False
            for x in self.village.wallarr:
                if x.pos == (self.x+self.facing[0],self.y+ self.facing[1]):
                    print("i found it!")
                    wallobj = x
                    break

            wallobj.hit(self.atk)
        elif( "h" in self.village.layout[self.y+ self.facing[1]][self.x+self.facing[0]]):
            print("BOOM")
            #self.attack = False
            for x in self.village.hutArr:
                if x.pos == (self.x+self.facing[0],self.y+ self.facing[1]):
                    print("i found it!")
                    wallobj = x
                    break

            wallobj.hit(self.atk)
        
        elif( "T" in self.village.layout[self.y+ self.facing[1]][self.x+self.facing[0]]):
            print("BOOM")
            #self.attack = False
            self.village.townHall.hit(self.atk)

        elif( "C" in self.village.layout[self.y+ self.facing[1]][self.x+self.facing[0]]):
            print("BOOM")
            #self.attack = False
            for x in self.village.canonArr:
                if x.pos == (self.x+self.facing[0],self.y+ self.facing[1]):
                    print("i found it!")
                    canonobj = x
                    break

            canonobj.hit(self.atk)

    def destroyed(self):
        if self.health <= 0:
            self.char = "_"
            return True
        return False

    def hit(self):
        if self.health:
            self.health -=1

        if self.health >= 0:
            self.color = healthCOLOR_king[self.health%len(healthCOLOR_king)]

    def leviathan(self):
        faces = [(1,0), (-1,0), (0,1), (0,-1)]
        storage = self.facing

        for i in range(-5,5):
            for j in range(-5,5):
                self.facing = (i,j)
                self.attacking()
        self.facing = storage
    

    
             
        
class Barbarian(King):

    def __init__(self, village,health, width,x,y):
        super().__init__(village,  health,  width)
        #self._color = healthCOLOR_wall[health]
        self.char = 'b'
        self.x = x  # (x, y) are coordinates of the centre
        self.y = y
        self.atk = 1

    def pathFinder(self):

        if not self.village.totalBuildingsarr:
            return
        min =1000
        target = self.village.totalBuildingsarr[0]
        for i in self.village.totalBuildingsarr:
            dist = math.sqrt((self.x - i.x)**2 + (self.y - i.y)**2)
            if min > dist:
                min = dist
                target = i
        
        if(self.x < target.x):
            self.moveX()
        elif(self.x> target.x):
            self.moveX(-1)

        if(self.y< target.y):
            self.moveY()
        elif(self.y> target.y):
            self.moveY(-1)
        
   




            


     

    