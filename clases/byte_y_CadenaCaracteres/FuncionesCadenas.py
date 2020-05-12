#Funciones de cadenas o String, recordar que las cadenas son INMUTABLES
	#Es decir las cadenas no cambian, es decir si usamos un meoto para convertir
	#una cadena a minuscula, lo que hara es crear un NUEVO objeto con la cadena en minuscula

#Funciones:
#Resumen de todos ellos:
#cadena.capitalize    cadena.isalnum       cadena.join          cadena.rsplit
#cadena.casefold      cadena.isalpha       cadena.ljust         cadena.rstrip
#cadena.center        cadena.isdecimal     cadena.lower         cadena.split
#cadena.count         cadena.isdigit       cadena.lstrip        cadena.splitlines
#cadena.encode        cadena.isidentifier  cadena.maketrans     cadena.startswith
#cadena.endswith      cadena.islower       cadena.partition     cadena.strip
#cadena.expandtabs    cadena.isnumeric     cadena.replace       cadena.swapcase
#cadena.find          cadena.isprintable   cadena.rfind         cadena.title
#cadena.format        cadena.isspace       cadena.rindex        cadena.translate
#cadena.format_map    cadena.istitle       cadena.rjust         cadena.upper
#cadena.index         cadena.isupper       cadena.rpartition    cadena.zfill

#Funcion capitalize() --> Nos pone el primer caracter de la cadena en Mayuscula micadena.capitalize()
#Funcion lower()--> Convierte la cadena a minuscula
#Funcion upper()--> Convierte la cadena en mayusculas
#Funcion swapcase()-->Cambia las mayusculas por minusculas y las minusculas por mayusculas
#Funcion title() -->Coloca la primera letra de cada palabra en mayuscula es decir "hola mundo" en "Hola Mundo"
#Funcion center()--> sirve para centrar una cadena, indicando el numero de espacios introducidos antes de esta.
	#Ej:micadena.center(50) Introducimos 50 espacios antes de escribir la cadena
	#Ej2:SOBRECARGA micadena.center(50,"="),en este caso rellenara en lugar de con espacios, con el caracter indicado antes y despues de la cadena.
#Funcion ljust()--> Igual que el anterior pero alinea a la izquiera	
		#Ej:micadena.ljust(50,"=")
#Funcion rjust()--> Igual que el anterior pero alinea a la derecha
#Funcion zfill()--> Dada una numero en su parametro rellena la cadena por la izquierda con la cantidad de 0 hasta llegar a este numero.
		#Ej: micadena="123" micadena.zfill(12) Resultado-> 000000000123,es decir la cadena siempre sera de 12 caracteres.

#Metodos de busqueda:

#Funcion count()-->Cuentala cantidad de apariciones de un caracter en una cadena
				#Ej:micadena.count("a")
				#Ej2:SOBRECARGA micadena.count("a",4) --> empieza a contar a partir de la 4 posicion
				#Ej3SOBRECARGA micadena.count("a"4,7)--> empieza a contar a partir de la 4 posicion hasta la 7
#Funcion find()-->Devuelve el indice de una subcadena, si o existe, devuelve -1
				#Ej:micadena.find("mun") busca la subcadana mun , por ejemplo "Hola mundo"  
#Funcion rfind()--> busca empezando por el final(desde la derecha) 
#Funcion index()--> busca una subcadena y devuelde la posicion como la funcion anterior,
					# pero si NO existe devuelve una excepcion micadena.index("a")

#Metodos de validacion:

#Funcion startswith()--> pregunta si una cadena empieza poruna subcadena y de vuelve true o false
					#Ej: micadena.startswith("mun")
					#Ej2:SOBRECARGA, podemos preguntar empezando por una posicion concreta micadena.startswith("mun",5)
#Funcion  endswith()--> Igual que la anterior pero en este caso ve si la cadena termina por una subcadena dada.
						#Tiene la misma sobrecarga que startswith()
#Funcion isalnum() --> Nos indica si la cadena es una cadena alfanumerica.
#Funcion isalpha()-->  Nos indica si la cadena esta formada por caracteres del alfabero(Letras)
#Funcion isdecimal()--> Nos indica si la cadena es un decimal
#Funcion isdigit()-->Nos indica si la cadena es un numero
#Funcion islower()--> Devuelve true si la cadena esta minuscula
#Funcion isupper()-->Devuelve true si la cadena esta en mayuscula
#Funcion isspace()--> Devuelve true si hay algun espacio en la cadena
#Funcion replace()--> Sustitulle un caracter o cadena por otra devolviendo una nueva cadena con el cambio
					#Ej:micadena="Hola" micadena.replace("o","e"), sustituira todas la "Ho" por "el"
#Funcion  strip()--> Elimina los espacios de una cadena, por delante y detras.
#Funcion lstrip()--> Elimina los espacios por la izquierda
#Funcion rstrip()--> Elimina los espacios por la derecha
				#Ej:SOBRECARGA si indicamos un caracter, eliminara ese caracter, si no indicamos nada, seran espacios
					#micadena.strip("a")
#Funcion join()-->Une o anexa una cadena al final de CADA ELMENTO de otra,CadenaQueQuieroUnir.join(cadenaAlaQueSeUnira)
				#Esta funcion ya itera por si sola, por lo que NO PUEDE estar dentro de un bucle for
				#Ej:micadena="Hola "  "que tal".join(micadena) Resultado-> "Hque tal o que tal que talaque tal"
				#Ej2:micadena"Hola" ".".join(micadena) Resultado->"H.o.l.a."
#Funcion partition()--> Indicandole un caracter separador, podemos divir una cadena en base a el,
						#devolviendonos una tupla de cadenas IMPORTANTE, solo separa  partir de la primera aparicion del caracter
						#Ej:micadena="12:45:30" micadena.partition(":") nos devolvera una TUPLA con 3 cadenas ("12",":","45:30")
#Funcion rpartition()-> Lo mismo pero por la derecha
#Funcion lpartition()--> Lo mismo pero por la izquierda
#Funcion split()--> Divide una cadena en base a un caracter separador que le indicaremos,
					#devolviendo una LISTA con todas las subcadenas resultantes de esta division
					#Ej:micadena="hola:pepe:4" micadena.split(":") resultado->["hola","pepe","4"]
#Funcion rsplit()-->Lo mismo pero por la derecha
#Funcion lsplit()-->Lo mismo pero por la izquierda
#Funcion splitlines()--> Devuelve una LISTA con cada una de las lineas que forma la cadena
						#Es decir si esta tiene saltos de linea como:
						#Ej:cadena="linea 1\nlinea 2\nlinea 3"
						#cadena.splitlines() Resultado->["linea 1","linea 2","linea 3"]

#Formateo de salida estandar de cadenas:
	#Podemos encontrar dos estilos, uno llamado 'Antiguo' y otro llamado 'Nuevo'

		#Estilo ANTIGUO o usando comodines:
			# %d formatea o imprime el valor en entero
			# %f formatea o imprime el valor como un float o flotante
			# Tambien podemos usar %2f el valor sera imprimido como un flotante redondeado a dos decimales.
			# %s formatea o imprime el valor como una cadena
			# %o formatea o imprime el valor en octal
			# %b formatea o imprime el valor en binario
			# %x formatea o imprime el valor en Hexadecimal

			#IMPORTANTE  para separar la cadena con el comodin del dato o variable a formatear usamos '%'
			#IMPORTANTE tambien es necesario que el resultado a mostrar este entre parentesis () o si no dara error
			#IMPORTANTE siempre que no usemos un formateo como estos explicados es necesario convertir el valor a mostrar en cadena con la funcion str()
				#Ejemplo print('El valor entero de 2.4 es %d' % (2.4)) imprimira El valor entero de 2.4 es 2

	#Estilo NUEVO o usando la funcion 'Format' de la clase String:
		#Ejemplo: 
		# print('El valor redondeado a 2 decimales de 2.4567 es '+ format(2.4567,'.2f') +' EL valor en octal de 12 es '+format(12,'o')+' el valor en binario de 17 es '+format(17,'b'))
		
		#Imprimira:
		# El valor redondeado a 2 decimales de 2.4567 es 2.46 EL valor en octal de 12 es 14 el valor en binario de 17 es 10001

		#De la siguiente forma indicamos una cadena con tantas llaves como elementos vayamos acolocar,y en el metodo format
		#las cadenas que se sustituiran en cada llava, como por ejemplo:

		#Usamos->'{} {}'.format("a", "b")
		#Resultado->'a b'

		#Igual que el ejemplo anterior pero indicando inices, similar a .NET
		#Usamos->'{1} {0}'.format("a", "b")
		#Resultado->'b a'

		#En este caso utilizamos claves creadas por nosotros como "latitude" y "longitude" y las igualamos.
		#Usamos->'Coordenadas: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
		#Resultado->'Coordenadas: 37.24N, -115.81W'

		#Usamos los comodines del estilo de formato Antiguo conla funcion formar, para dar distintos formatos numericos
		#Usamos->'{0:b} {1:x} {2:.2f}'.format(123, 223,12.2345)
		#Resultado->'1111011 df 12.23'

		#En este usamos las llaves para centrar el tecto en 10 caracteres por la derecha e izquierda
		#Usamos->'{:^10}'.format('test')
		#Resultado->'   test   '