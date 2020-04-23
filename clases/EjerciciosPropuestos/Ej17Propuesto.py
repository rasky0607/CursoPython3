#1º En este ejercicio se propone introducir una cadena por teclado e identificar si esta se encuentra en la lista
#2ºImprimir cuantas veces aparece dicha cadena en la lista
#3º Si la cadena introducida, se encuentra en la lista, la sustituiremos tantas veces como aparezca, por una nueva
#4º Eliminar el reemplazo que hicimos de la lista
lista=["carlos","tail","playa","noise","tail","Ester"]
remplazo=None#Se usa si se encuentra la cadena en la lista, si no, no
apariciones=None#Igual que remplazo
pos=None#igual que remplazo
print("Lista -> "+str(lista))
cadena = input("#Introduce una palabra: ")
try:#Control de exceciones
	if(lista.index(cadena)):#Comprobamos si la cadena esta en la lista
	#Otra forma de comprobar si la cadena esta en la lista es con el operador de pertenencia'in' [if cadena in lista:]
		print("'"+cadena+"' si se encuentra en la lista")
		apariciones=lista.count(cadena)
		print("Numero de veces que aparece la cadena: "+str(lista.count(cadena)))
		remplazo=input("Remplazar por: ")
		
except:#Tratamiento de exceciones
	print("No se encuentra en la lista")
if remplazo!=None:
	print("Insercion de la cadena introducida '"+cadena+"' en la posicion 1'empezando desde la 0'")
	for i in range(0,apariciones):
		pos=lista.index(cadena)
		lista[pos]=remplazo
	print("Lista -> "+str(lista))

	print("Eliminamos el elemento de la 2º posicion de la lista")
	for i in range(0,apariciones):
		pos=lista.index(remplazo)
		lista.pop(pos)
	print("Lista --> "+str(lista))
