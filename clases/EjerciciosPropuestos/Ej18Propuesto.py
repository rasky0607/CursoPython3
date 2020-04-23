#En este ejercicio indicaremos si una lista de enteros esta o no esta ordenada
lista=[1,2,5,7,0,3,9]
compara=None
print("#Inicio")
for item in lista:
	if(lista.index(item)==0):#Si la posicion del item que miramos es la primera de la lista
		compara=item
	else:
		if(compara>item):
			print("La lista NO esta ordenada")
			break
		else:
			compara=item
else:
	print("La lista SI esta ordenada")

lista.sort()
print("#Segundo intento")
for item in lista:
	if(lista.index(item)==0):#Si la posicion del item que miramos es la primera de la lista
		compara=item
	else:
		if(compara>item):
			print("La lista NO esta ordenada")
			break
		else:
			compara=item
else:
	print("La lista SI esta ordenada")

#Otra forma de realizar este ejercicio
print("#Otra forma de realizar el ejercicio")
lista1=[2,3,4,1]
lista2=lista[:]#Copiamos la lista en otra nueva
lista2.sort()#Ordenamos a lista nueva
if lista1==lista2:#Comparamos la lista ordenada "lista2" con la lista que puede estar desordenada "lista1"
    print("Lista ordenada")
else:
    print("Lista no ordenada")
