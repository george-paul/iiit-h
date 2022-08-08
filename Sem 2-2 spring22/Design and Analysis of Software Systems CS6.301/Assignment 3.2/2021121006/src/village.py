from .mainCharacters import ArcherQueen, King
from .tile import Tile
from . import building 
from os import system

class Village:
	def __init__(self):
		self.characterChoice = "K"
		self.rows = 21
		self.cols = 41
		self.gameOn = True							# whether the game is running

	def initialise(self):
		# initialise field
		self.field = []
		for i in range(self.rows):
			self.field.append([])
			for j in range(self.cols):
				self.field[i].append(Tile(i,j, "_"))
		if self.characterChoice == "A":
			# initialise Archer Queen
			self.mc = ArcherQueen(1,1, "A")
			self.field[1][1] = self.mc
		else:
			# initialise Archer Queen
			self.mc = King(1,1, "K")
			self.field[1][1] = self.mc
		#						 up left, bottom right
		# spawn walls (6,11),(15,30)
		for i in range(6,16):
			for j in range(11, 31):
				if i == 6 or i == 15 or j == 11 or j == 30:
					self.field[i][j] = building.Wall(i,j)



	def rend(self):
		system('clear')
		for i in range(self.rows):
			print(str(i) + "\t", end='')				# coordinates
			for j in range(self.cols):
					print(self.field[i][j].disp, end='')
			print("")
		print("\n\t" + "0123456789" * 6)			# coordinates



	def moveMC(self, ir , ic):
		r = self.mc.r + ir
		c = self.mc.c + ic
	
		if isinstance(self.field[r][c], building.Building):
			return

		if(r>=self.rows):
			r = self.rows-1
		if(c>=self.cols):
			c = self.cols-1
		if(r<0):
			r = 0
		if(c<0):
			c = 0
		self.field[self.mc.r][self.mc.c] = Tile(self.mc.r, self.mc.c, "_")
		self.field[r][c] = self.mc
		self.mc.r = r
		self.mc.c = c

	

	def attack(self, r, c, dmg):
		if isinstance(self.field[r][c], building.Building):
			self.field[r][c]
			self.field[r][c].hp -= dmg
			if self.field[r][c].hp <= 0:
				self.field[r][c] = Tile(r,c,"_")