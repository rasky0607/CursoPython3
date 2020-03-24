#Aqui podemos ver ejemplo de estructuras de repeticion o bucles de python:
#while :
#	pass <-Esta instruccion pass no hace absolutamente nada, no da erro de sintaxys pero tampoco hace nada

anio=2001
print("## Bucle While sin clausula final else")
while anio<=2017:
	print(anio)
	anio+=1

#IMPORTANTE: Particularidad de python en los bucle while:
	#Puede añadirse una clausula else al final de un bucle while, la cual se ejecutara justo antes de salir del bucle.
print("## Bucle While  PARTICULAR DE PYTHON con clausula final else")
anio=2001
while anio<=2017:
	print(anio)
	anio+=1
else:
	print("TERMINE!")

#Bucle FOR IMPORTANTE es muy particular tanto en comportamiento como estructura en python:
print("## Bucle FOR [MUY PARTICULAR] EN PYTHON")
#range(10) nos devuelve una secuencia o lista de numeros del 0 al 9, i va cogiendo los valores de este range
print("	-- Bucle FOR [Con numeros]")
for i in range(10):
	print("Valor de (i) dentro del For "+str(i))

print("	-- Bucle FOR [Con cadenas]")
for i in "hola":
	print("Valor de (i) dentro del For "+str(i))

print("	-- Bucle FOR [Con una lista]")
for i in [1,2,3]:
	print("Valor de (i) dentro del For "+str(i))

#IMPORTANTE destacar que al igual que el bucle while, puede tener una instruccion else que se ejecuta la final del bucle

print("	-- Bucle FOR [Con cadenas] y clausula final else")
for i in "hola":
	print("Valor de (i) dentro del For "+str(i))
else:
	print("TERMINE")

#Instrucciones de rotura o manipulacion de el curso natural del bucle 'break','continue'
#Break (Rompe el bucle, saliendo de el este por donde este)
for i in "hola":
	if(i=='o'):
		print("Valor de (i) dentro del For "+str(i)+" Ups un Break, SALGO del BUCLE")
		break
else:
	print("TERMINE")
#Continue (Lo que realiza esta instruccion es volver a realizar otra interacion del bucle o por asi decirlo incrementar su contador sin continuar con el resto de instruciones que esten por debajo de ella)
for i in "hola":
	if(i=='o'):
		print(" ¡¡Ups!! un continue, Ignoro la siguiente instrucion y doy otra vuelta al BUCLE")
		continue
	print("Valor de (i) dentro del For "+str(i))
else:
	print("TERMINE")

#Instruccion Zip() que nos posibilita con el bucle FOR recorrer dos o mas secuencias o coclecciones
	#IMPORTANTE , si una de las secuencias o colecciones tiene menos elementos, el bucle termianra cuando la colecion con menos elementos termine
print(" --Instruccion zip() que nos posibilita con el bucle FOR recorrer dos o mas secuencias o coclecciones")
for i,j in zip(range(2,5),["ana","juan","pepe"]):
	print("Valor de (i) dentro del For "+str(i)+" <-> Valor de (j) dentro del For "+str(j))
else:
	print("TERMINE")



