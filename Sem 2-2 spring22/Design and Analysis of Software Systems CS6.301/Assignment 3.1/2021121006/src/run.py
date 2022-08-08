from pynput.keyboard import Key, Listener
from . import village
from os import system

vilg = village.Village()

def render():
	system('cls')
	for i in range(vilg.rows):
		for j in range(vilg.cols):
			# if i == vilg.king.x and j == vilg.king.y:
			if vilg.field[i][j] is vilg.king:
				print("K", end='')
			else: 
				print("_", end='')
		print("")

def runGame():
	render()
	while(vilg.gameOn):
		pass

def on_press(key):
	try:
		if key.char and key.char == 'w':
			vilg.moveKing(-1, 0)
		if key.char and key.char == 's':
			vilg.moveKing(1, 0)
		if key.char and key.char == 'a':
			vilg.moveKing(0, -1)
		if key.char and key.char == 'd':
			vilg.moveKing(0, 1)
	except AttributeError:
		pass
	

	# test
	# system('cls')
	# print(f"{key} was pressed")

	# End Game
	if key == Key.esc:
		vilg.gameOn = False
		quit()
	render()

def on_release(key):
	pass

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()