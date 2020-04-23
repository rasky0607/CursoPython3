#1. Dada dos cadenas desvolver true o false si la segunda cadena es una subcadena de la primera
	#Por ejemplo, cadena es una subcadena de subcadena.
#2. Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe cod y adove debe devolver adove.

cadena1=input("Escribe la primera cadena: ")
cadena2=input("Escribe la segunda cadena: ")
#PUNTO 1
if(cadena1.find(cadena2)!=-1):
	print(cadena2+" SI es una subcadena de la primera -> "+cadena1)
else:
	print(cadena2+" NO es una subcadena de la primera -> "+cadena1)

 
#PUNTO 2
#flag=False
#for i in cadena1:
#	for j in cadena2:
#		if(i==j):
#			continue
#		elif(i<j):#Comparacion caracter a caracter de ambas cadenas
#			flag=True
#			print(cadena1)
#			break;
#		else:
#			flag=True
#			print(cadena2)
#			break;#Salimos del bucle interno
#	if(flag):#Si es verdad se sale tambien del bucle mas externo
#		break

#Resumen de PUNTO 2
if(cadena1<cadena2):
	print(cadena1)
else:
	print(cadena2)