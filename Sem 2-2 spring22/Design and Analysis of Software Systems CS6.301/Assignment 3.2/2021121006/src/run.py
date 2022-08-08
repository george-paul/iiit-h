from .inpt import input_to
from .village import Village

vilg = Village()

def runGame():
	vilg.characterChoice = input("Which character? (A for Archer Queen, else King): ").upper()
	vilg.initialise()

	while(vilg.gameOn):
		vilg.rend()
		key = input_to()

		# move king
		if key == 'w':
			vilg.moveMC(-1, 0)
		elif key == 's':
			vilg.moveMC(1, 0)
		elif key == 'a':
			vilg.moveMC(0, -1)
		elif key == 'd':
			vilg.moveMC(0, 1)
		
		# attack
		elif key == " ":
			box = vilg.mc.attackRange()
			# (u,l,b,r)
			for i in range(box[0], box[2]+1):
				for j in range(box[1], box[3]+1):
					vilg.attack(i, j, vilg.mc.damage)

		# exit game
		elif key == '`':
			vilg.gameOn = False
		else:
			pass