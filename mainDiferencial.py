#!/usr/bin/env python
import time
from Diferencial2 import *
from motordc import *
from plot import *

print ("----------Bienvenido a Motor SIM (Diferencial)-----------\nInserte los datos que se le solicitan.")
r = float(input("Radio: "))
l = float(input("Longitud: "))
b = float(input("Campo Magnetico del estator: "))
k = float(input("Constante de motor: "))
primero = Motor(r,l,b,k)
segundo = Motor(r,l,b,k)
#tercero = Motor(r,l,b,k)
#cuarto  = Motor(r,l,b,k)
print(primero)
print ("Flujo Magnetico = " + str(primero.flujoMagnetico()))
ld = float(input("Separacion de las ruedas diferenciales: "))
rd = float(input("Radio de las ruedas: "))
p=Plot()
x0=0
y0=0
d=Diferencial2(ld,rd)
exit = True
while exit:
	v = []
	v.append(input("Voltaje inducido(Fem) del rotor 1: "))
	v.append(input("Voltaje inducido(Fem) del rotor 2: "))
	ciclos = float(input("Definir los ciclos del motor: "))
	#ciclos = float(ciclos)
	then = float(time.time())
	now = float(time.time())
	delta = float(now - then)
	while delta<ciclos:		
		delta = now - then
		seconds = float(delta)
		print ("Segundo = " + str(seconds) )
		now = float(time.time())
		w = []
		w.append(primero.velocidadAngular(float(v[0])))
		w.append(segundo.velocidadAngular(float(v[1])))
		w.append(float(seconds));
		for i in range(0, 2):
			print ("Velocidad Angular " +str(i)+ ": "  + str(w[i]))
	wd = w[0]
	wi = w[1]
	print (str(seconds))
	vector = d.set_bottle(wd,wi,seconds)
	x1 = (d.calculate_xprima() * seconds) + x0
	y1 = (d.calculate_yprima() * seconds) + y0
	print ("Vector de Velocidades angulares: (" + str(w[0]) + "," + str(w[1]) + ")")
	print ("Velocidad en la rueda derecha: " + str(d.calculate_vd()))
	print ("Velocidad en la rueda izquierda: " + str(d.calculate_vi()))
	print ("Velocidad angular del vehiculo: " + str(d.calculate_w(ld)))
	print ("Angulo: " + str(d.calculate_angle()))
	print ("R grande: "  + str(d.calculate_bigr(ld)))
	print ("X prima: " + str(d.calculate_xprima()))
	print ("Y prima: " + str(d.calculate_yprima()))
	print ("Velocidad total del vehiculo: " + str(d.calculate_vtotal()))
	p.addArrow(x0,y0,x1-x0,y1-y0)
	x0=x1
	y0=y1
	cont = str(raw_input("Desea continuar [y/n]: "))
	if cont.upper() == "N":
		exit = False
		p.show()
		print ("Bye!")


