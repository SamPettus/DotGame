from dots import Dot
class Population:
	def __init__(self, size):
		self.size = size
		self.population = []
		for i in range(0, size):
			self.population.append(Dot())
	def getDot(self, index):
		return self.population[index]
	def getSize(self):
		return self.size
	def movePopulation(self): #Moves every dot in the population
		for i in range(0,self.size):
			if not self.population[i].dead:
				self.population[i].move()
	def allDotsDead(self): #Checks to see if all the dots in the population are dead
		for i in range(0,self.size):
			if  not self.population[i].dead:
				return False
		return True