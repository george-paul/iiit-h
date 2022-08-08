from headers import *
from board import getboard
from paddle import Paddle
from brick import Brick
from ball import *
from powerup import *
from ballcollision import *
from colors import *
os.system('clear')
PADDLE = Paddle(30,38,0,34,37)
PADDLE.createpaddle()
BALL = Ball(34,37,1,-1,5,0)
BALL.createball()
BRICK = Brick()
POWER1 = Power1()
POWER1.assign_color()
POWER2 = Power2()
POWER2.assign_color()
POWER3 = Power3()
POWER3.assign_color()
POWERINF = Powerinf()
POWERINF.assign_color()
EXPLOADBRICK = Exploadbrick()
EXPLOADBRICK.assign_color()
BALLCOLLISION = getballcollision
BOARD = getboard
BOARD.printboard()


start_time = time.time()
screen_time=time.time()
x=time.time()


while True:
   os.system("tput reset")
  

   #print board
   BOARD.printboard()
   newtime =(round(time.time()) - round(start_time))
   print(  Fore.GREEN+"time:"+Back.RESET , newtime,  Fore.CYAN+"   lives remaining :"+Back.RESET, BALLCOLLISION.lives,  Fore.RED+"   score :"+Back.RESET, BALLCOLLISION.score)
   #print (newtime) 
    #move paddle
   PADDLE.move_paddle()
   if PADDLE.flag == 1:
      BALLCOLLISION.moveball()