#Colecciones, listas, tuplas, coleccion de datos
#Definicion de una lista,tupla y dicccionario:
	#lista=[9,2,"pepe",10,'k'] --> MUITABLES
	#mitupla=(1,2,3,4)		--> INMUTABLES
	#miDiccionario={'one':1,'two':2,'three':3} --> MUTABLES

#Nota 0: MUTABLE ->(Se pueden modificar/borrar los elementos de la secuencia)
#			Ej:lista[2]=99
#			Ej:Tambien podemos modificar un subconjunto de la lista-->lista[2:4]=[10,5]
			#IMPORTANTE: En este ultimo ejemplo lista[2:4] el primer parametro indica donde empieza 
			#y el ultimo donde acaba menos 1 es decir desde el 2 al 3
#		 INMUTABLE->(No se pueden modificar elementos de la lista)

#Nota 1: En todas las Secuencias/colecciones se puede usar un operador de pertenecia.
	#Ej: 3 in lista // 3 not in lista <-- es decir el 3 se encuentra en esta secuencia?, devuelve true o false

#Nota 2: se puede usar el operador + para concatenar datos secuencia

#Nota 3: indexar a un elemento determinado, es decir acceder a una posicion determinada de la coleccion lista[0]

#Nota 4: Podemos optener un subconjunto de datos secuencia/coleccion es decir "slite" o "rebanada"
	#Ej:lista[2:4] <-- obtiene el subconjunto de una lista del la posicion 2 a la 3
	#(corresponderia a la posicion 3, por que el utimo parametro "el maximo" no es includo, si no que es uno menos)
	#Ej:Tambien podemos obtener un subcojunto desde una posicion indicada hasta el final
		#lista[2:] ,o al contrario lista[:4]
	#Ej:Tambien podemos indicar un principio un final y un intervalo como por ejemplo de 2 en 2
		#lista[2:5:2]

#Nota 5: Funcion len(), nos permite saber el numero de elementos que componen la lista como length().
#Nota 6: Funcion max() y min() nos permite encontrar el maximo elemento o minimo de una secuencia--> max(lista)
	#[IMPORTANTE todos los datos tienen que ser del mismo tipo para usar min() y max(),
	# si no, no se puede comprar o de tipo comparable al menos]
	#Funcion sum() nos  devuelve la suma de los elementos de la lista, si los elementos se pueden sumar.
	#Funcion sorted() para lista desordenadas, nos devuelve una lista ordenada.
		#Tambien se le puede indicar el parametro "reverse=true" para que la lista la ordena ala inversa
			#Ej sorted(lista,reverse=True) 
#Nota 7: funcion del() elimina subconjuntos de una secuencia/coleccion (Solo con secuencias MUTABLES)
	#Ej del lista[2:4] 

#Nota 8:podemos repetir una secunencia/coleccion, tambien llamdo actualizar(Solo con secuencias MUTABLES)
		#Ej lista*=2 tendriamos como resultado el mismo conjunto de datos en la misma lista, dos veces.	
#Nota 9:[ COPIAR LISTAS ] Obtiene toda la lista al completo lista[:]

#Nota 10: devolver la lista invertida lista[::-1]
		#Tambien si podemos indicar una posicion negativa y nos devolvera es posicion empezando
		#por el final --Ej: lista[-1] "Nos devolera e ultimo elemento de la lista"

#Nota 11:Funcion enumerate(),que nos permite enumerar las posiciones de una lista,
		#esta nos devuelve una lista de tuplas donde cada tupla tine dos elementos la enumeracion y el elemento
		#Tambien puede recibir el parametro "start=numeroPorElQueEmpiezaANumerar" enumerate(lista,start=2)

#Nota 12:Tablas o listas bidimensionales
		#Ej: tabla=[[1,4,2].["pepe",4,9],[0,7,1]] ,realmente e suna lista con 3 listas
		#para acceder a alguno de sus elementos por ejemplo, tabla[1][2] --> estariamos selecionado el '9'

#Podemos encontrar:
#-------------------------#

#Listas(con datos de distinto tipo) y son MUTABLES,tambien son objetos que se pueden comparar lista1==lista2 y se comparan elemento a elemento
#METODOS de la CLASE list() para manejarlas milista=[1,2,3]:
	#milista.append()-> añade elementos a el fila de la lista
	#milista.insert(pos,elemento)-> inserta un elemento en una posicion determinada,desplazando el resto de elementos, NO SUSTITUYE
	#milista.clear()-> vacia la lista
	#milista.extend()-> concatena unas listas con otra
	#milista.count()-> devuelve el numero de apariciones de un elmento en la lista
	#milista.pop() -> nos devuelve el ultimo elemento y lo quita de la lista
	#milista.pop(posicion)->"SOBRECARGA" por lo que podemos eliminar un elemento de una posicion concreta
	#milista.remove(elemento)-> igual que el anterior solo que indicamos el elemento NO la posicion
								# y NO nos devuelve el elemento al elimianrlo de la lista.
								#En caso de encontrar dos datos iguales, borra el primero que se encuentra.
	#milista.reverse()-> da la vuelta a la lista.
	#milista.sort() -> Ordena la lista, tambien encontramos sobre carga con milista.sort(reverse=true)
						#Tambien ordena cadena de caracteres,es decir string milista=["hola","ana"]->["ana","hola"]
						#En el caso de ordenacion de cadenas tiene otra sobre carga milista.sort(key=str.lower)
						#Esta convertira todas las cadenas a minuscula antes de ordenarlas
	#milista.copy()--> copia una lista lista3=milista.copy()
	#milista.index(elemento)-> devuelve el indice donde se encuentra el primer elemento que coincide con el indicado 
							#Tiene SOBRECARGA, pudiendo indicarle que busque un elemento a partir de una posicion
							#milista.index(elemento,posicion) -> milista.index(3,5)

#Ejemeplo:
print("#Ejemplos de lista:")
#Ej lista vacia lista=[] o usando el constructor lista= list()
lista=[9,2,"pepe",10,'k']
for i in lista:
	print(i)

#Ejemplo operador de pertenecia:
if 9 in lista:
	print("Si")
else:
	print("No")
#Concatenacion de tipos secuencia/coleciones con el operador +
print("#Ejemplos concatenacion de tipos secuencia:")
lista2=lista +[55,33,11]
for i in lista2:
	print(i)
print("Subconjunto-> "+str(lista2[2:4]))


#Ejemplo de uso de funcion enumerate() "Nota 11" para enumerar elmentos de una lista y como recorrerla
print("#Funcion enumerate() para enumerar elementos d euna lista")
for i,j in enumerate(lista2,start=3):
	print(i,j)

#Ejemplo tablas o listas bidimensionales
print("#Ejemplo tablas o lista bidimensionales")
tabla=[[1,4,2],["pepe",4,9],[0,7,1]]
for fila in tabla:
	for colum in fila:
		print("Fila -> "+str(fila)+" Columna-> "+str(colum))
	print()	
#-------------------------#

#Tuplas igual que las listas pero son INMUTABLES
#Ejemeplo:

#-------------------------#

#Rangos que posibilita una lista de datos numericos es un tipo INMUTABLE
#Ejemeplo:

#-------------------------#

#Cadena de caracteres,es decir un string que realmente es una secuencia de caracteres es un tipo INMUTABLE
#Ejemeplo:

#-------------------------#

#Los byte que son para guardar datos binarios y son INMUTABLES
#Ejemeplo:

#Los bytearray son iguales que los anteriores pero son MUTABLES
#Ejemeplo:

#-------------------------#

#Cojunto set, permite guardar un cojunto de datos,"SIN REPETICION" y es MUTABLE
#Ejemeplo:

#Conjunto frozenset, igual que el anterior pero en este caso es INMUTABLE
#Ejemeplo:

#-------------------------#


