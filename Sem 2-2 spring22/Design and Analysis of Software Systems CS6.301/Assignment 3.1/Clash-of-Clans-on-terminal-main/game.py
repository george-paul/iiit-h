from array import *
from ast import For
from turtle import width
import colorama
import sys
import os
import math
import time
import copy
import time
from colorama import Fore, Back, Style
from buildings import Hut, TownHall, Wall, Canon
from extra import COLS, ROWS, Xd0, Yd0
from king import King, Barbarian

WIDTH =COLS
HEIGHT = ROWS

class Village():
    def __init__(self):
        self.layout = [[Fore.GREEN+"_" +Style.RESET_ALL]* HEIGHT for _ in range(WIDTH)]
        self.size = (WIDTH, HEIGHT)
        self.townHall =  TownHall(self, int(WIDTH//2 ), int(HEIGHT//2), 8, 'T', 4,3)
        self.hut1 = Hut(self, int(WIDTH//2 - 7), int(HEIGHT//2), 6, 'h', 1,1)
        self.hut2 = Hut(self, (WIDTH//2 + 4), (HEIGHT//2), 6,'h', 1,1)
        self.hut3 = Hut(self, (WIDTH//2+2 ), (HEIGHT//2+7), 6, 'h',1,1)
        self.hut4 = Hut(self, WIDTH//2 - 9, HEIGHT//2+5, 6, 'h',1,1)
        self.hut5 = Hut(self,WIDTH//2 , HEIGHT//2-5, 6, 'h',1,1)
        #self.wall = Wall(self,(WIDTH//2)-11 , (HEIGHT//2)-7, 4, 'W',1,1)
        self.wallarr =[]
        for i in range(WIDTH//2-11 , WIDTH//2+7)  :
            self.wallarr.append(Wall(self,i , HEIGHT//2-7, 6, 'W',1,1))
            self.wallarr.append(Wall(self,i , HEIGHT//2+9, 6, 'W',1,1))
        for i in range(HEIGHT//2-7, HEIGHT//2+9)  :
            self.wallarr.append(Wall(self,WIDTH//2-11 , i, 4, 'W',1,1))
            self.wallarr.append(Wall(self,WIDTH//2+7 , i, 4, 'W',1,1))

        self.hutArr = [self.hut1, self.hut2, self.hut3, self.hut4, self.hut5]
        self.canonArr =[ Canon(self, WIDTH//2-8, HEIGHT//2+6,   10, 'C' , width = 1, height = 1), Canon(self, WIDTH//2+5, HEIGHT//2+6,   2, 'C' , width = 1, height = 1), Canon(self, WIDTH//2-2, HEIGHT//2+6,   10, 'C' , width = 1, height = 1)]
        
        self.barbarianTroops = []
        #self.barbarianTroops = [Barbarian(self,2,1,Xd0,Yd0)]
        self.totalBuildingsarr = self.hutArr + self.canonArr  
        self.totalBuildingsarr.append(self.townHall)
        self.raid = True
        self.King= King(self, 20, 1)
        self.canonTargetsarr = [self.King] + self.barbarianTroops

    def barbarianSpawner(self,x,y):

        self.barbarianTroops.append(Barbarian(self,2,1,x,y))
        self.canonTargetsarr = [self.King] + self.barbarianTroops

    def healthUp(self):

        self.King.health = int(self.King.health*1.5)

        for i in self.barbarianTroops:
            i.health =int(i.health * 1.5)

    def speedUp(self):

        self.King.turns +=1
        self.King.atk += 1

        for i in self.barbarianTroops:
            i.turns +=1
            i.atk +=1


    

