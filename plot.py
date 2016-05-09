#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
# -*- coding: utf-8 -*-
class Plot:
	
	def __init__(self):
		self._ax = plt.axes()
		plt.ylim(-1,10)
		plt.xlim(-1,10)
		plt.title("Movimiento del carro")
		plt.xlabel("x")
		plt.ylabel("y")
		plt.grid(True)

	def addArrow(self,x1,y1,x2,y2):
	#	colorVal = scalarMap.to_rgba(1)
		self._ax.arrow(x1, y1, x2, y2, head_width=0.05, head_length=.1, fc='k', ec='k')

	def show(self):
		plt.show()

