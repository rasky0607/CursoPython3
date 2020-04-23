#Ejercicio de lista, añade numeros a una lista hasta que se añada un numero negativo
#y muestra el numero maximo de esa lista y los numeros pares
numero=None
lista=[]
numero=int(input("Introduce un numero: "))
print("-------------------------")
while numero>=0:
	lista.append(numero)#añadimos numero a la lista
	print("#Numero añadido \n#Lista:")
	for item in lista:
		print(item)
	numero=int(input("Introduce un numero: "))
	print("-------------------------")
else:#Cuando se va salir del bucle
	print("#Se introducjo un numero negativo "+str(numero))

#Mostramos el mayor entero de la lista
print("#Numero maxmimo de la lista-> "+str(max(lista)))

#Motramos los numeros pares de la lista
print("#Numeros pares de la lista: ")
for item in lista:
		if(item%2==0):
			print(item)