import sqlite3, binascii, datetime
import pygame, sys, random, socket, _thread, time
from pygame.locals import *

# we will make game.
# agent can build, gather, train, and so on.
# It is kind of RPG.

# variable setting
units = []
buildings = []

# Pygame Setting
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200,800),0,32)
pygame.display.set_caption('Game')
fpsClock = pygame.time.Clock()
BASICFONTSIZE = 16
BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)


# Color Setting
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
SKYBLUE = (128, 128, 255)
DARKGRAY = (100, 100, 100)
GRAY = (140,140,140)
WHITEGRAY = (200,200,200)

class unit:
	name = ''
	# stat
	hp = (0,0)
	mp = (0,0)
	sp = (0,0)
	exp = (0,0)
	speed = 0

	# inventory
	inventory = []
	inventorylimit = (0,0) # weight, volume
	inventorylock = -1 # only me

	# state
	position = (0,0,0) # x,y,r. if r is 0, on collision
	direction = 0
	action = 0

	# passive skill
	def passiveskill():
		pass

	# active skill
	
	def generate():
		pass

	def load():
		pass

class building:
	name = ''
	# stat
	hp = (0,0)

	# inventory
	inventory = []
	inventorylimit = (0,0) # weight, volume
	inventorylock = -1 # only me

	# state
	position = (0,0,0,0) # x,y,width,height

	def generate():
		pass


def loaddata():
	f1 = open("./data/units.txt", "r")
	f2 = open("./data/buildings.txt", "r")

	# read units
	# data format = hp, mp, sp, exp, speed, inventory, inventorylimit, inventorylock, position, direction, action
	while True:
		line = f1.readline()
		if not line: break
		token = line.split(' ')
		name = token[0]
		hp = (int(token[1]), int(token[2]))
		mp = (int(token[3]), int(token[4]))
		sp = (int(token[5]), int(token[6]))
		exp = (int(token[7]), int(token[8]))
		speed = int(token[9])

		# parse inventory
		temp = token[10].split(',')
		inventory = []
		for i in temp:
			inventory.append(int(i))

		inventorylimit = list((int(token[11]), int(token[12])))
		inventorylock = int(token[13])

		position = list((int(token[14]), int(token[15]), int(token[16])))
		direction = int(token[17])
		action = int(token[18])

		units.append((hp, mp, sp, exp, speed, temp, inventory, inventorylimit, inventorylock, position, direction, action))


	# read buildings
	# data format = hp, inventory, inventorylimit, inventorylock, position
	while True:
		line = f2.readline()
		if not line: break
		token = line.split(' ')
		name = token[0]
		hp = (int(token[1]), int(token[2]))
		temp = token[3].split(',')
		inventory = []
		for i in temp:
			inventory.append(int(temp))

		inventorylimit = (int(token[4]), int(token[5]))
		inventorylock = int(token[6])
		position = (int(token[7]), int(token[8]), int(token[9]), int(token[10]))

		buildings.append((hp, inventory, inventorylimit, inventorylock, position))



def start():
	loaddata()

def drawmap():

	DISPLAYSURF.fill(BLACK)

	# display map

	# for testing
	textSurf = BASICFONT.render('Hello World!', True, WHITE)
	textRect = textSurf.get_rect()
	textRect.topleft = (40, 40)
	DISPLAYSURF.blit(textSurf,textRect)

	# testing end

	# draw building
	for i in buildings:
		pass
	# draw unit
	for i in units:
		 pygame.draw.circle(DISPLAYSURF, SKYBLUE, (i[9][0],i[9][1]), i[9][2])

	pygame.display.update()

def processinput():

	mousex = 0
	mousey = 0
	mouseClicked = False

	for event in pygame.event.get(): # event handling loop
		if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mousex = event.pos[0]
			mousey = event.pos[1]
			mouseClicked = True
		elif event.type == MOUSEBUTTONUP:
			mousex = event.pos[0]
			mousey = event.pos[1]
			mouseClicked = True
		# Process Keyboard Input

	if mouseClicked == True:
		# process event if mouse cursor in event range
		
		units[0][9][0] = mousex
		units[0][9][1] = mousey

def processaction():
	for i in units:
		pass
	for i in buildings:
		pass

def mainloop():
	while True:
		drawmap()
		processinput()
		processaction()

start()
mainloop()