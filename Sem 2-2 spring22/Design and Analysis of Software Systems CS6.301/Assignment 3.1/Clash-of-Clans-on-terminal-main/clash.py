from array import *
from pickle import FALSE
from tkinter.tix import ROW
from turtle import st
from click import style
import colorama
import sys
import os
import math
import time
import copy
import time
from colorama import Fore, Back, Style
from buildings import TownHall
from extra import ROWS, COLS, X0, Y0, Xd0, Xl0, Xr0, Yd0, Yl0, Yr0
# custom modules
from game import HEIGHT, Village
from input import get_input
from extra import ROWS, COLS, T
import json
# initialize the layout
inlist =[]
 
        
WIDTH = COLS
HEIGHT = ROWS
layout = [[Fore.GREEN+"_"] * HEIGHT for _ in range(WIDTH)]
townHallDeathCheck =0
frame =0
Dict = {}   #empty dictionary
f = open('replay.json', 'r+')
blank_board = []
for i in range(ROWS):
    row = ['_']*COLS
    row.append('\n')
    blank_board.append(row)
# for r in  layout:
#    for c in r:
#       print(Fore.GREEN +c,end = " " + Style.RESET_ALL)
#    print()

village = Village()
while village.raid:
    key = get_input()
    print("\033[H\033[J", end="")
    # village.layout = copy.deepcopy(blank_board)
    village.King.display()
    # village.hut1.display()
    for h in village.hutArr:
        h.display()

    for w in village.wallarr:
        w.display()

    for w in village.canonArr:
        w.display()
    # village.wall.display()
    village.townHall.display()
    for i in village.barbarianTroops:
        i.display()
    # print(board)
    for row in village.layout:
        for c in row:
            print(c, end='')
        print()

    for i in village.canonArr:
        i.canonfire()
             
    for br in village.totalBuildingsarr:
        if br.destroyed():
            village.layout[br.y][br.x] = Fore.GREEN+"_" + Style.RESET_ALL
            village.totalBuildingsarr.remove(br)

    for br in village.canonArr:
        if br.destroyed():
            village.layout[br.y][br.x] = Fore.GREEN+"_" + Style.RESET_ALL 
            village.canonArr.remove(br)

    if village.King.destroyed():
        village.layout[village.King.y][village.King.x] = Fore.GREEN+"_" + Style.RESET_ALL

     
    for br in village.barbarianTroops:
        if br.destroyed():
            village.layout[br.y][br.x] = Fore.GREEN+"_" + Style.RESET_ALL
            village.barbarianTroops.remove(br)
            village.canonTargetsarr.remove(br)

#    village.King.moveY()
#    village.King.attacking()
    for br in village.wallarr:
        if br.destroyed():
            village.layout[br.y][br.x] = Fore.GREEN+"_" + Style.RESET_ALL
            village.wallarr.remove(br)
             
    for br in village.hutArr:
        if br.destroyed():
            village.layout[br.y][br.x] = Fore.GREEN+"_" + Style.RESET_ALL
            village.hutArr.remove(br)
            #village.totalBuildingsarr.remove(br)

     

    # village.King.moveY()
    
    if(not village.King.destroyed()):
        if (key == "d"):
            village.King.moveX()
            Dict[frame] = key
        elif (key == "a"):
            village.King.moveX(-1)
            Dict[frame] = key
        elif (key == "w"):
            village.King.moveY(-1)
            Dict[frame] = key
        elif (key == "s"):
            village.King.moveY()
            Dict[frame] = key
        elif (key == " "):
            village.King.attacking()
            Dict[frame] = key
        elif (key == "l"):
            village.King.leviathan()
            Dict[frame] = key
        elif (key == "2"):
            village.barbarianSpawner(Xd0,Yd0)
            Dict[frame] = key
        elif (key == "3"):
            village.barbarianSpawner(Xr0, Yr0)
            Dict[frame] = key
        elif (key == "4"):
            village.barbarianSpawner(Xl0,Yl0)
            Dict[frame] = key
        elif (key == "."):
            village.healthUp()
            Dict[frame] = key
        elif (key == ","):
            village.speedUp()
            Dict[frame] = key

    inlist.append(key)
    for i in village.barbarianTroops:
        i.pathFinder()
        i.attacking()
    print(village.King.x)
    print(village.King.y)
    print("health:" + str(village.King.health))
    for i in range(village.King.health):
        print(Back.GREEN+"|"+ Style.RESET_ALL, end = " ")
    print()
    print("speed:" + str(village.King.turns))
    print("attack:" + str(village.King.atk))
    print(len(village.barbarianTroops))

    time.sleep(T)
    frame+=1
    if not village.totalBuildingsarr:
        print("VICTORY")
        village.raid = False 
        data = json.load(f)
        data.append(inlist)
        f.seek(0)
        json.dump(data, f)
         
    elif  (not village.barbarianTroops) & village.King.destroyed():
        print("LOSS")
        village.raid = False
        data = json.load(f)
        data.append(inlist)
        f.seek(0)
        json.dump(data, f)

    # os.system('cls' if os.name == 'nt' else 'clear')
