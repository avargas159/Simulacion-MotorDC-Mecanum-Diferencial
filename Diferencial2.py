#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math as m;

class Diferencial2:
	
	def __init__(self,l,r):
		#l es la distancia entre las llantas, r es el radio de las llantas
		self._l = l;
		self._r = r;
		self._vd = 0.0;
		self._vi = 0.0;
		self._wd = 0.0;
		self._wi = 0.0;
		self._w = 0.0;
		self._t = 0.0;
		self._bigr = 0.0
		
	#Vector con entradas	
	def set_bottle(self,wd,wi,t):
		self._wd = wd
		self._wi = wi
		self._t = t
	
	#Velocidad tangencial en la rueda izquierda	
	def calculate_vd(self):
		self._vd = (self._wd * self._r )
		return self._vd
	
	#Velocidad tangencial en la rueda izquierda	
	def calculate_vi(self):
		self._vi = (self._wi * self._r )
		return self._vi
	
	#Velociad angular  del vehiculo	
	def calculate_w(self, l):
		self._w = (self._vd - self._vi) / l
		return self._w 	
	
	#Angulo para las dos ruedas	
	def calculate_angle(self):
		ang = (self._w * self._t) * (180 / m.pi)
		if ang < 0:
			return ang + 360
		return ang
		
	#R Grande	
	def calculate_bigr(self,l):
		self._bigr = (l / 2) * ((self._vi + self._vd) / (self._vd - self._vi))
		return self._bigr
	
	#Movimiento en X	
	def calculate_xprima(self):
		self._x = (self._bigr * m.sin(self._w * self._t) )
		return self._x
		
	#Movimiento en Y
	def calculate_yprima(self):
		self._y = (self._bigr - (self._bigr * m.cos(self._w * self._t) ) )
		return self._y
	
	#Velocidad total del vehiculo en la direccion que se mueva
	def calculate_vtotal(self):
		self._vt= (self._vd + self._vi) / 2
		return self._vt

	def __str__(self):
		string = "[ Carro diferencial ] \n"
		string += "distancia entre las ruedas: " + str(self._l) + "\n"
		string += "radio de las ruedas: " + str(self._r) + "\n"
		string += "velocidad angular del vehículo: " + str(self._w) + "\n"
		string += "velocidad tangencial de la rueda derecha: " + str(self._vd) + "\n"
		string += "velocidad tangencial de la rueda izquierda: " + str(self._vi) + "\n"
		string += "velocidad angular de la rueda derecha: " + str(self._wd) + "\n"
		string += "velocidad angular de la rueda derecha: " + str(self._wi) + "\n"
		string += "tiempo del recorrido: " + str(self._t) + "\n" 
		return string	
