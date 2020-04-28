#Iteradores y generadores:
#Iterador:Nos permite recorrer elementos de una secuencia/coleccion
#todas las secuencias cuando se recorrern devuelven un objeto iterador para poder iterarlo
#Ej:miterador=iter([1,2,3]) este seria un list_iterator
#Metodos de los Iteradores:
#next() -> nos devuelve el siguente elemento a iterar
	#miterador=iter([1,2,3]) miterador.next(), nos devolvera 1, en la suigente ejecucion 2 etc...
	#Si llamamos de nuevo a next() tras realizarla ultima iteracion, devolvera una excepcion

#reversed()--> Nos permite crear un iterador con el orden inverso, es decir :
	#Ej: miterador2 = reversed([1,2,3])
		#Ahora al ejecutar el metodo next() sobre este iterador,
		#nos devolvera miterador2.next() resultado--> 3, siguiente--> 2 etc...

#El módulo/libreria itertools contiene distintas funciones que nos devuelven iteradores.
	#En esta libreria podemos encontrar varios metodos como:
	#count(), el cual devuelv eun iterador infinito Ej: miterador=count(start=10)
		#Cada vez que ejecutemos next, nos devolvera la siguiente iteracion y nunca llegara al final
	#cycle(), El cual nos devuelve tambien un iterador infinito pero ciclico, es decir cuando llega al final
			#este comienza de nuevo por el principio
			#Ej:from itertools import cycle
				#colors = cycle(['red', 'white', 'blue'])
				#colors.next()->nos dara red, luego while luego blue.. y luego de nuevo red etc..

#Un Generador es una funcion, que nos permite obtener los resutltados de la funcion paso a paso.
	#En este caso normalmente se usaria en otros lenguajes "Returm" pero aqui 
	#la palabra reservada yield. Se explicara con profundidad en el tema de las funciones.
#Tambien podemos usar un Generador con listas comprimidas
	#Ej:Utilizando la sintaxis de las “list comprehension”
		#iter1 = (x for x in range(10) if x % 2==0)
		 #next(iter1)
		 #0
		 #next(iter1)
		 #2
		 #next(iter1)
		 #4
