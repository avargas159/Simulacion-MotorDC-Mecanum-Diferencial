#!/usr/bin/env python
from __future__ import division
import math
import time

class Motor:

	def __init__(self,radio, longitud, campo,constante_motor):
		#print ("Bienvenido a MotorSIM!")
		#print ("A continuacion se le solicitaran algunos datos acerca de su motor.")
		self._radio=radio
		self._longitud=longitud
		self._campo=campo
		self._constante_motor=constante_motor
	
	def flujoMagnetico(self):
		flujo = 2 * math.pi * self._radio * self._longitud * self._campo
		return flujo

	def velocidadAngular(self,voltaje):
		velocidad = (voltaje) / (self._constante_motor*self.flujoMagnetico())
		return velocidad
	
	def __str__(self):
		string = "Motor DC \n" 
		string += "R: "+str(self._radio)+"\n"
		string += "L: "+str(self._longitud)+"\n"
		string += "C: "+str(self._campo)+"\n"
		string += "CM: "+str(self._constante_motor)+"\n"
		return string

