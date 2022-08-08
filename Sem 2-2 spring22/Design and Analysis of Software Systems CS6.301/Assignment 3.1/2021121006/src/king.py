from .tile import Tile

class King(Tile):
	def __init__(self):
		self.hp = 100
		self.damage = 20
		self.moveSpeed = 1
	def __init__(self, r, c):
		super().__init__(r,c)
		self.hp = 100
		self.damage = 20
		self.moveSpeed = 1