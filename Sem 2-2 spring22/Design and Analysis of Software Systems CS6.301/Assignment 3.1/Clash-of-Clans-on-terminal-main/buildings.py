import colorama
from colorama import Fore, Back, Style
import math
from extra import healthCOLOR_hut, healthCOLOR_town, healthCOLOR_wall
deathCheck = 0


def winCondition():
    if deathCheck == 6:
        return True
    
        
class Buildings:
    def __init__(self, village, x, y, health, character, width, height):
        self.health = health
        self.pos = (x,y)
        self.char = character
        self._color = healthCOLOR_town[health]
        self.w = width
        self.h = height
        self.y = y
        self.x = x
        self.village = village
    
    def display(self):
        
        w=self.w
        h=self.h
        arr = self.village.layout
        for x in range(self.x, self.x+w):
            for y in range(self.y, self.y +h):
                arr[y][x] = self._color + self.char + Style.RESET_ALL
        #arr[self.y+h][self.x + w] = Style.RESET_ALL + arr[y][self.x + w]
        self.village.layout = arr
        #print(self.village.layout)
    
    def destroyed(self):
        if self.health <= 0:
            self.char = "_"
            return True
        return False

    def hit(self, damage):
        if self.health:
            self.health -=damage

        if self.health >= 0:
            self._color = healthCOLOR_town[self.health%len(healthCOLOR_town)]
             
    
    


class Hut(Buildings):
    def __init__(self, village, x, y, health = 4, character = 'h' , width = 2, height = 2):
        super().__init__(village, x, y, health, character, width, height)
        #self._color = healthCOLOR_hut[health]
     

class TownHall(Buildings):
    def __init__(self, village, x, y, health = 4, character = 'h' , width = 2, height = 2):
        super().__init__(village, x, y, health, character, width, height)
        #self._color = healthCOLOR_town[health]
     
class Wall(Buildings):
    def __init__(self, village, x, y, health = 4, character = 'h' , width = 2, height = 2):
        super().__init__(village, x, y, health, character, width, height)
        #self._color = healthCOLOR_wall[health]
     


class Canon(Buildings):
    def __init__(self, village, x, y, health = 4, character = 'h' , width = 2, height = 2):
        super().__init__(village, x, y, health, character, width, height)
        self.cooldown =0
    
    def canonfire(self):
        min =1000
        target = self.village.canonTargetsarr[0]
        for i in self.village.canonTargetsarr:
            dist = math.sqrt((self.x - i.x)**2 + (self.y - i.y)**2)
            if min > dist:
                min = dist
                target = i
            
        self.cooldown+=1
        self._color = healthCOLOR_town[self.health]
        if self.cooldown >= 5:
            if min <= 10:

                target.hit()
                self.cooldown =0
                self._color = Style.RESET_ALL



            
        
        
 