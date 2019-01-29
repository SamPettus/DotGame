from brain import Brain
import pygame

class Dot:
	goalX = 400
	goalY = 40
	def __init__(self):
		self.pos = [400,750]
		self.vel = [0,0]
		self.acc = [0,0]
		self.dead = False
		self.reachedGoal = False
		self.head = Brain(5000)

	def getPos(self):
		return self.pos

	def move(self): #Updates acc, vel, and pos based off of the brain vectors
		x = self.head.getdirSize()
		if(x>self.head.step):
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
		self.vel[0] = self.vel[0] * 6
		self.vel[1] = self.vel[1] * 6
		self.pos[0] = self.pos[0] + self.vel[0]
		self.pos[1] = self.pos[1] + self.vel[1]
		if self.pos[0] < 3 or self.pos[1]<3 or self.pos[0]>800-3 or self.pos[1]>800-3:
			self.dead = True