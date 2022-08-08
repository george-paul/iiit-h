from .tile import Tile

class Building(Tile):
	def __init__(self, r, c, disp, hp, w, h):
		super().__init__(r,c,disp)
		self.hp = hp
		self.disp = disp
		self.w = w
		self.h = h
	

class Wall(Building):
	def __init__(self, r, c):
		super().__init__(r, c, "W", 30, 1, 1)