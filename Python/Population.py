from dots import Dot
import random
class Population:
	def __init__(self, size):
		self.size = size
		self.population = []
		self.fitnessSum = 0
		self.bestDot = 0
		self.minSteps = 500000000
		self.GOAL = False
		self.gen = 0
		for i in range(0, size):
			self.population.append(Dot())
	def getDot(self, index):
		return self.population[index]
	def getSize(self):
		return self.size
	def movePopulation(self): #Moves every dot in the population
		for i in range(0,self.size):
			if self.population[i].dead or self.population[i].reachedGoal:
				if self.population[i].reachedGoal:
					self.GOAL = True
				continue
			else:
				self.population[i].move()
	def allDotsDead(self): #Checks to see if all the dots in the population are dead
		x = 0
		for i in range(0,self.size):
			if self.population[i].dead:
				x = x + 1
			elif self.population[i].reachedGoal:
				x = x + 1
			else:
				break
		if x==self.size:
			return True
		else:
			return False
	def calcFitness(self):
		for i in range(0,self.size):
			self.population[i].calcFitness()
	def calcFitnessSum(self):
		self.fitnessSum = 0
		for i in range(0,self.size):
			self.fitnessSum = self.fitnessSum + self.population[i].fitness
	def setBestDot(self):
		Max = 0
		maxIndex = 0
		for i in range(0,self.size):
			if(self.population[i].fitness>Max):
				Max = self.population[i].fitness
				maxIndex = i
		self.bestDot = maxIndex
		if self.population[self.bestDot].reachedGoal:
			self.minSteps = self.population[self.bestDot].head.step
	def selectParent(self):
		random.seed()
		w = random.uniform(0, self.fitnessSum)
		runningSum = 0
		for i in range(0,self.size):
			runningSum = runningSum + self.population[i].fitness
			if(runningSum>w):
				return self.population[i]
	def naturalSelection(self):
		evolved = []
		self.setBestDot()
		self.calcFitnessSum()
		evolved.append(self.population[self.bestDot].createBaby())
		evolved[0].isBest = True
		for i in range(1,self.size):
			parent = self.selectParent()
			evolved.append(parent.createBaby())
		self.population = evolved
		self.gen = self.gen + 1
	def mutate(self):
		for i in range(0,self.size):
			self.population[i].head.mutate()