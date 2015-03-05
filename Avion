import sys
from random import randint

list_of_nom = ['Lufthansa', 'AirFrance', 'Wizz Air', 'Blue Air']

class avion:
	def __str__(self):
		return self.nom + '\n' + str(self.landingTemps) + '\n' + str(self.takeOffTemps) + '\n' + ('Decolage' if self.status == 0 else 'Aterissage') + '\nPriorite:' + str(self.priorite)
	def __init__(self, nom, landingTemps, takeOffTemps):
		self.nom = nom
		self.landingTemps = landingTemps
		self.__maxLandingTemps = landingTemps
		self.takeOffTemps = takeOffTemps
	def getPercentage(self):
		if self.status == 0:
			return (self.__maxLandingTemps - self.landingTemps) /float( self.__maxLandingTemps);
		return (self.__maxLandingTemps - self.takeOffTemps) / float(self.__maxLandingTemps);
	def __lt__(self, other):
		return (self.priorite < other.priorite)
	def setPriorite(self, priorite):
		self.priorite = priorite
	def setNom(self, nom):
		self.nom = nom
	def getNom(self):
		return self.nom
	def setStatus(self, status):
		self.status = status
	def getStatus(self, status):
		return self.status
	def getReadableStatus(self):
		return 'coller' if self.status == 0 else 'decoller'
	def generateRandomavion():
		index = randint(0, len(list_of_nom) - 1)
		id = randint(0, 2500)
		landingTemps = randint(1, 5)
		avion = avion(list_of_nom[index] + str(id), landingTemps, landingTemps)
		avion.setStatus(id % 2)
		avion.setPriorite(int(randint(0, 60) / 12))
		return avion
	generateRandomavion = staticmethod(generateRandomavion)
