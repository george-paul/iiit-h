from .king import King
from .tile import Tile


class Village:
	def __init__(self):
		self.rows = 18
		self.cols = 50
		self.gameOn = True							# whether the game is running
		self.king = King(self.rows//2,self.cols//2)					# king object
		self.field = []
		for i in range(self.rows):
			self.field.append([])
			for j in range(self.cols):
				self.field[i].append(Tile(i,j))
		self.field[self.rows//2][self.cols//2] = self.king


	def moveKing(self, ir , ic):
		r = self.king.r + ir
		c = self.king.c + ic
	
		if(r>=self.rows):
			r = self.rows-1
		if(c>=self.cols):
			c = self.cols-1
		if(r<0):
			r = 0
		if(c<0):
			c = 0
		self.field[self.king.r][self.king.c] = Tile(self.king.r, self.king.c)
		self.field[r][c] = self.king
		self.king.r = r
		self.king.c = c