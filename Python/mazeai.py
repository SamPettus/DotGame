import pygame
import math
import sys
import os
from dots import Dot
pygame.init()
white = [255,255,255]
red = [255,0,0]
blue = [0,255,0]
Population = []
screen = pygame.display.set_mode((800,800))
def main():
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	screen.fill(white)
	pygame.display.update()
	generatePopulation(3)
	run = True
	while run:
		screen.fill(white)
		pygame.draw.circle(screen, red, (400,40), 10,0)
		for i in range(0,3):
			drawDot(Population[i])
		for i in range(0,3):
			Population[i].move()
		pygame.display.update()
		pygame.time.delay(180)
		#Lets you quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		keys = pygame.key.get_pressed();
		if keys[pygame.K_ESCAPE]:
			run = False;

	pygame.quit()
	return
def generatePopulation(x):
	for i in range(0, x):
		Population.append(Dot())

def drawDot(w):
	z = w.getPos()
	pygame.draw.circle(screen, blue , (int(z[0]),int(z[1])), 3, 0)
main()
