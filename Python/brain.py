import random
class Brain:

	def __init__(self, dirSize):
		self.dirSize = dirSize
		self.step = 0
		self.direction = [[]]
		self.randomize()


	def randomize(self): #Creates an array of vectors from [-1 to 1, -1 to 1]
		random.seed()
		for i in range(0,self.dirSize):
			randX = random.random()
			if(randX>.5):
				x = random.random() * 10
			else:
				x =-1.0 * random.random() * 10
			randY = random.random()
			if(randY>.5):
				y= random.random() * 10
			else:
				y = -1.0 * random.random() * 10
			self.direction.append([x,y])
	def getDirection(self):
		return self.direction
	def getStep(self):
		return self.step 
	def getdirSize(self):
		return self.dirSize
	def clone(self):
		x = Brain(self.dirSize)
		for i in range(0,self.dirSize):
			x.direction[i] = self.direction[i]
		return x
	def mutate(self):
		random.seed()
		mutationRate = .025
		for i in range(0,self.dirSize):
			rand = random.random()
			if rand<mutationRate:
				randX = random.random()
				if(randX>.5):
					x = random.random() * 7
				else:
					x =-1.0 * random.random() * 7
				randY = random.random()
				if(randY>.5):
					y= random.random() * 7
				else:
					y = -1.0 * random.random() * 7
				self.direction[i] = [x,y]

