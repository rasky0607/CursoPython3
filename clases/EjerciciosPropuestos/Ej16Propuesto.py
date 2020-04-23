#Inicializar una lista desde codigo y copiar esta en una nueva, pero invertida
lista=["Juan","pepe","Ramon","Invierno"]
lista2=list.copy(lista)
list.reverse(lista2)
#Otra forma de devolver la lista invertida sera print(lista2[::-1])
print("\nLista original: ")
for item in lista:
	print(item,end=" ")

print("\n")	

print("Lista copiada e invertida: ")
for item in lista2:
	print(item,end=" ")

print("\n")	