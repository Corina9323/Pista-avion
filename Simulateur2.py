import sys
from random import randint
from Plan import Plan
import time
from math import trunc
from ModelImpl import *
import re
import operator
import os
import sys 
from PyQt4 import QtCore
from PyQt4.QtCore import QObject, pyqtSignal
from radar import Ui_RadarWidget
list_of_names = ['Lufthansa', 'AirFrance', 'Wizz Air', 'Blue Air']

class Simulation2(QObject, Ui_RadarWidget):

	header = ['Nom', 'Priorite', 'Temp Estimee']
	def __init__(self, maxNombre, tempTick, numPiste):
		super(Simulation2, self).__init__()
		self.running = 0
		self.currentNombre = 0
		self.maxNombre = maxNombre
		self.tempTick = tempTick
		self.listOfAirplans = numPiste * [None]
		self.numPiste = numPiste
		self.arriverIn = []
		self.departIn = []
		self.departModel = None
		self.arriverModel = None
		self.__generateInitialData(self.maxNombre)
		self.temp = QTemp()
	def __setTempTick(self, temp):
		self.tempTick = (int)((100 - temp) / 50 * 1000)
		self.temp.setInterval(self.tempTick)
		self.setRunning()
	def __generateInitialData(self, nr):
		toGenerate = randint(0, nr)
		self.currentNombre += toGenerate
		print('Generating ' + str(toGenerate))
		if self.departModel is not None:
			self.departModel.triggerDataChanging()
			self.arriverModel.triggerDataChanging()
			

		for i in range(0, toGenerate):
			plan = Plan.generateRandomPlan()
			if plan.status == 0:
				self.departIn.append(plane)
			else:
				self.arriverIn.append(plane)
		self.departIn.sort()
		self.arriverIn.sort()
		if self.departModel is not None:
			self.departModel.triggerDataChanged()
			self.arriverModel.triggerDataChanged()
		
		
	def __bindUiToModel(self):
		if self is not None:
			for i in range(self.numPiste):
				airplane = self.listOfAirplanes[i]
				if airplane is not None:
					getattr(self, 'runway' + str(i)).setValue(int(airplane.getPercentage() * 100))
					getattr(self, 'runwayplane' + str(i)).setText(airplane.name + ' - ' + airplane.getReadableStatus())
				else:
					getattr(self, 'runway' + str(i)).setValue(0)
					getattr(self, 'runwayplane' + str(i)).setText('Pista Libera')
			self.labelSosiri.setText('Departs ' + str(len(self.arriverIn)))
			self.labelPlecari.setText('Arrivers ' + str(len(self.departIn)))

	def setGraphicalModel(self):
		#self.ui = ui
		self.departModel = MyTableModel(self.plecariIn, Simulation2.header,['nom', 'priorite', 'takeOffTime'],  self.tableDepart) 
		self.arriverModel = MyTableModel(self.sosiriIn,  Simulation2.header,['name', 'priority', 'landingTime'], self.tableArriver) 
		self.tableDepart.setModel(self.DepartModel)
		self.tableArriver.setModel(self.ArriverModel)
		self.__bindUiToModel()
		self.buttonStart.clicked.connect(self.setRunning)
		self.buttonStop.clicked.connect(self.setStopped)
		self.horizontalSlider.valueChanged[int].connect(self.__setTimerTick)
	def setStopped(self):
		self.running = 0
	def setRunning(self):
		self.running = 1
		# Connect it to c
		if not self.timer.isActive():
			self.timer.timeout.connect(self.__runSimulation)
		# Call c() every 1 second
			self.timer.start(self.timerTick)

	def __consumePlane(self):
		freeSpots = [x for x in self.listOfAirplanes if x is None]
		numPlanes = len(freeSpots)
		for x in range(numPlanes):
			if len(freeSpots) > 0:
				index = self.listOfAirplanes.index(None)
			else:
				return
			if len(self.departIn) > 0:
				departPlane = self.depIn[0]
			else:
				departPlane = None
			if len(self.arrIn) > 0:
				arriverPlane = self.depIn[0]
			else:
				arriverPlane = None
			if (arrPlane is None and depPlane is None):
				return
			if arrPlane is None or (depPlane is not None and depPlane.priority < arrPlane.priority):
				self.listOfAirplanes[index] = depPlane
				self.plecariIn.pop(0)
			elif depPlane is None or (arrPlane is not None and depPlane.priority > arrPlane.priority):
				self.listOfAirplanes[index] = arrPlane
				self.sosiriIn.pop(0)
			else:
				if len(self.sosiriIn) > len(self.plecariIn):
					self.listOfAirplanes[index] = arrPlane
					self.sosiriIn.pop(0)
				else:
					self.listOfAirplanes[index] = arrPlane
					self.plecariIn.pop(0)
	def __checkForCompletion(self):
		for i in range(0, len(self.listOfAirplanes)):
			if self.listOfAirplanes[i] is not None:
				if self.listOfAirplanes[i].status == 0:
					self.listOfAirplanes[i].landingTime-=1
				else:
					self.listOfAirplanes[i].takeOffTime-=1
				if self.listOfAirplanes[i].takeOffTime <= 0 or self.listOfAirplanes[i].landingTime<=0:
					self.listOfAirplanes[i] = None
					
	def __runSimulation(self):
		print('Sim time is ' + str(self.timerTick))
		if self.running != 0:
			self.currentNumber = len(self.sosiriIn) + len(self.plecariIn)
			if self.running == 2:
				return
			self.__generateInitialData(self.maxNumber - self.currentNumber)
			self.__checkForCompletion()
			self.__consumePlane()
			self.__printModel()
			self.__bindUiToModel()
		else:
			timer.stop()
	def stopInit(self):
		self.running = 0
	def __printModel(self):
		for i in range(0, len(self.listOfAirplanes)):
			if self.listOfAirplanes[i] is not None:
				print ('RW:' + str(i) + ' --- ' + self.listOfAirplanes[i].name + ' --- ' + str(int(self.listOfAirplanes[i].getPercentage() * 100)) + '%')
			else:
				print ('RW:' + str(i) + ' --- is free')
