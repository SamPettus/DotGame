import random
class Brain:

	def __init__(self, dirSize):
		self.dirSize = dirSize
		self.step = 0
		self.direction = [[]]
		self.randomize()


	def randomize(self):
		random.seed()
		for i in range(0,self.dirSize):
			randX = random.random()
			if(randX>.5):
				x = random.random()
			else:
				x =-1.0 * random.random()
			randY = random.random()
			if(randY>.5):
				y= random.random()
			else:
				y = -1.0 * random.random()
			self.direction.append([x,y])
	def getDirection(self):
		return self.direction
	def getStep(self):
		return self.step 
	def getdirSize(self):
		return self.dirSize
	def printDirection(self):
		for i in range(0, self.dirSize):
			print(self.direction[i])