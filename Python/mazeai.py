import pygame
import math
import sys
import os
from Population import Population
from dots import Dot
pygame.init()
white = [255,255,255] #Creating Const Color Values for ease of use
red = [255,0,0]
blue = [0,255,0]
test = Population(30) # Creates a population of 30
screen = pygame.display.set_mode((800,800))
def main():
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	screen.fill(white)
	pygame.display.update()
	run = True
	while run:
		screen.fill(white)
		pygame.draw.circle(screen, red, (400,40), 10,0)#Draws the goal
		drawPopulation(test)#Draws all the dots in the population
		test.movePopulation()#updates all the dots position vector
		pygame.display.update()
		pygame.time.delay(140)
		#Lets you quit
		if test.allDotsDead():#if all the dots in the population are dead the game will exit
			run = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		keys = pygame.key.get_pressed();
		if keys[pygame.K_ESCAPE]:
			run = False

	pygame.quit()
	return

def drawDot(w): #Draws the Dot
	z = w.getPos()
	pygame.draw.circle(screen, blue , (int(z[0]),int(z[1])), 3, 0)
def drawPopulation(x): #Draws each dot in the population using the above function
	for i in range (0,x.getSize()):
		drawDot(x.getDot(i))
main()
