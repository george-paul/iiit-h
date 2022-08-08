 
import colorama
from colorama import Back

# time
FPS = 100
T = 1/FPS

# screen size
ROWS = 30
COLS = 30

# starting coordinates for king
#X0 = int(COLS//2)
X0 = 5
Y0 = 0

# starting coordinates for king
#X0 = int(COLS//2)
Xr0 = COLS-2
Yr0 = ROWS//2

# starting coordinates for king
#X0 = int(COLS//2)
Xl0 = 5
Yl0 = 0+2

# starting coordinates for king
#X0 = int(COLS//2)
Xd0 = 2
Yd0 = ROWS//2


# colorconstants
healthCOLOR_town = [Back.GREEN,  Back.RED,Back.RED,
               '\033[40m','\033[41m'
        ,'\033[42m'
        ,'\033[43m'
       ,'\033[44m'
        ,'\033[45m'
        ,'\033[46m'
        ,'\033[47m']

healthCOLOR_hut = [Back.RESET, Back.RED,
              Back.GREEN, Back.YELLOW, Back.BLUE]

healthCOLOR_king = [
               '\033[40m',Back.GREEN, Back.YELLOW
        ,'\033[43m'
       ,'\033[44m'
        ,'\033[45m'
        ,'\033[46m'
        ,'\033[47m']

healthCOLOR_wall = [Back.RESET, Back.RED,
              Back.GREEN, Back.YELLOW, Back.MAGENTA]


