from .tile import Tile

class King(Tile):
	def __init__(self, r, c, disp):
		super().__init__(r, c, disp)
		self.hp = 100
		self.damage = 20
		self.moveSpeed = 1
		
	# returns the corners of the box in which to attack
	# ie (u , l , b , r )

	def attackRange(self):
		u = self.r-1
		l = self.c-1
		b = self.r+1
		r = self.c+1
		return (u,l,b,r)

class ArcherQueen(Tile):
	def __init__(self, r, c, disp):
		super().__init__(r, c, disp)
		self.hp = 80
		self.damage = 10
		self.moveSpeed = 1
		self.range = 8
	def attackRange(self):
		u = self.r-2
		l = self.c-2
		b = self.r+2
		r = self.c+2
		return (u,l,b,r)