#!/usr/bin/env python
import time
from motordc import *
from Mecanum import *
from plot import *

print("-----------------------------Bienvenido a Motor SIM (Mecanum)------------------\n")
r = float(input("Radio: "))
l = float(input("Longitud: "))
b = float(input("Campo Magnetico del estator: "))
k = float(input("Constante de motor: "))
primero = Motor(r,l,b,k)
segundo = Motor(r,l,b,k)
tercero = Motor(r,l,b,k)
cuarto  = Motor(r,l,b,k)
print(primero)
print("Flujo magnetico del motor: "+str(primero.flujoMagnetico()))
rm = float(input("Radio de las ruedas del mecanum: "))
lx = float(input("Ancho del carro mecanum: "))
ly = float(input("Largo del carro mecanum: "))
p=Plot()
x0=0
y0=0
m=Mecanum(lx,ly,rm)

#print "Flujo Magnetico = " + str(primero.flujoMagnetico())

exit = True
while exit:
	v = []
	v.append(input("Voltaje inducido(Fem) del rotor 1: "))
	v.append(input("Voltaje inducido(Fem) del rotor 2: "))
	v.append(input("Voltaje inducido(Fem) del rotor 3: "))
	v.append(input("Voltaje inducido(Fem) del rotor 4: "))
	ciclos = float(input("Definir los ciclos del motor: "))
	then = float(time.time())
	now = float(time.time())
	diff = float(now - then)
	while diff<ciclos:		
		diff = now - then
		seconds = float(diff)
		print ("Segundo = "  + str(seconds))
		now = float(time.time())
		w=[]
		w.append(primero.velocidadAngular(float(v[0])))
		w.append(segundo.velocidadAngular(float(v[1])))
		w.append(tercero.velocidadAngular(float(v[2])))
		w.append(cuarto.velocidadAngular(float(v[3])))
		w.append(float(seconds));
		for i in range(0, 4):
			print ("Velocidad Angular: " +str(i)+ " "+ str(w[i])) 
	m.set_wn(w);
	
	x1=m.calculate_vx()*w[4]+x0
	y1=m.calculate_vy()*w[4]+y0
	m.calculate_w();
	m.calculate_vr();
	print(m)
	print("Angulo="+ str(m.calculate_angle()))
	p.addArrow(x0,y0,x1-x0,y1-y0)
	print(x0,y0,x1,y1)
	x0=x1
	y0=y1
	cont = str(raw_input("Desea continuar [y/n]: "))
	if cont.upper() == "N":
		p.show()
		exit = False
		print("Bye!")


	#print(str(w[4]))
	#print seconds	 
	
#if __name__ == "__main__":
#	main()

