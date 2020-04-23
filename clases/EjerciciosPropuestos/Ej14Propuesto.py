#Optener si unn umero introducido por teclado es primo o no
numero=None
numero=int(input("Introduce un numero entero: "))

if(numero==1):
	print("El numero es primo")
if(numero==0):
	print("El numero no es primo")
contador=2
while numero%contador!=0:
	#Si ninguno de los numeros anteriores al indicado al dividirlo por el est enumero indicado da de resto 0.. es que el numero es primo
	if(contador==numero-1):
		print("El numero SI es primo")
		break
	contador+=1
else:
	print("El numero NO es primo")
	pass