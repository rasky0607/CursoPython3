#En este ejercicio se pretende  realizar un juego de adivinar un numero
#El programa preguntara continuamente hasta que el numero sea adivinado

#Extra añadido 
import os

numero=None
numero=int(input("Dime el numero secreto: "))
contador=0
#Extra añadido (este metodo procede de la libreria del sistema importa 'os'
#que nos permite ejecutar metodos dle sistema, es decir comandos del bash)
os.system("clear") 
#------------
respuesta=int(input("Adivina el numero: "))
while respuesta!=numero:
	print("No has acertado =( ...")
	if(respuesta>numero):
		print("El numero que me indicaste es mayor que el numero secreto ...")
	if(respuesta<numero):
		print("El numero que me indicaste es menor que el numero secreto ...")

	respuesta=int(input("Vuelve a intentarlo. Adivina el numero: "))
	contador+=1

if(respuesta==numero):
	print("Has acertado al "+str(contador)+"º intento =) !!!, el numero secreto era el "+str(numero))
		