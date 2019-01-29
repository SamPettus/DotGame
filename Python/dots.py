from brain import Brain
import math
import pygame
def distance(posX, posY, goalX, goalY):
	return math.sqrt((posX - goalX)**2 + (posY - goalY)**2)
class Dot:
	def __init__(self):
		self.pos = [400,750]
		self.vel = [0,0]
		self.acc = [0,0]
		self.dead = False
		self.reachedGoal = False
		self.head = Brain(600)
		self.goalX = 400
		self.goalY = 40
		self.fitness = 0
		self.isBest = False
	def getPos(self):
		return self.pos

	def move(self): #Updates acc, vel, and pos based off of the brain vectors
		x = self.head.getdirSize()
		if(x>self.head.step + 1):
			self.acc = self.head.getDirection()[self.head.getStep() + 1]
			self.head.step = self.head.step + 1
		else:
			self.dead = True
		accx = self.acc[0]
		accy = self.acc[1]
		self.vel[0] = self.vel[0] + accx
		self.vel[1] = self.vel[1] + accy
		if(self.vel[0]>1):
			self.vel[0] = 1
		if(self.vel[0]<-1):
			self.vel[0] = -1
		if(self.vel[1]>1):
			self.vel[1] = 1
		if(self.vel[1]<-1):
			self.vel[1] = -1
		self.vel[0] = self.vel[0] * 8
		self.vel[1] = self.vel[1] * 8
		self.pos[0] = self.pos[0] + self.vel[0]
		self.pos[1] = self.pos[1] + self.vel[1]
		if self.pos[0] < 6 or self.pos[1]<6 or self.pos[0]>800-4 or self.pos[1]>800-4:
			self.dead = True
		if distance(self.pos[0],self.pos[1], self.goalX, self.goalY)<10:
			self.reachedGoal = True
	def calcFitness(self):
		if self.reachedGoal:
			self.fitness = 1.0/16.0 + 10000.0/float(self.head.step * self.head.step)
		else:
			distancetoGoal = distance(self.pos[0],self.pos[1], self.goalX, self.goalY)
			self.fitness = 1.0/(distancetoGoal * distancetoGoal)

	def createBaby(self):
		baby = Dot()
		baby.head = self.head.clone()
		baby.dead = False
		return baby