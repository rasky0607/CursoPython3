#Funciones Recursivas, Lambdas,Decoradores,Generadores en pyhton
#Funciones recursivas:
#Una función recursiva es aquella que al ejecutarse hace llamadas a ella misma.
#Por lo tento tenemos que tener “un caso base” que hace terminar el bucle de llamadas. 
#Ej:
	# def factorial(numero):
	#     if(numero == 0 or numero == 1):
	#         return 1
	#     else:
	#         return numero * factorial(numero-1)

#Funciones Lambda:
	#Las funciones lambda nos sirven para crear pequeñas funciones anónimas, de una sola línea sobre la marcha.
	
	#Ej:Imaginemos tener una varaible cuadrado definida anteriormente a la que queremos asignarle el resultado de
	#el cuadrado de un numero indicado con una funcion Lambda.
	#Lo hariamos de el siguiente modo:
		#1º Igualamos la variable a la palabra lambda.
		#2º Indicamos el "parametro REAL" [Es decir el nombre del parametro no el valor]
		#3º Indicamos dos puntos ":" y la operacion que se realizara con este parametro
			#En este caso el cuadrado del parametro de entrada asi que la variable x**2
		
		#cuadrado=lambda x:x**2
		#Nota1[IMPORTANTE]:[Realmente lo que estamos realizando es referenciar una "Funcion anonima" a una variable],
			#de forma que podremos realizar esto: cuadrado(5)
			#y tambien podriamos realizar usando las llaves {lambda x:x**2}(5)
				#Ya que es la variable cuadrado apunta la misma referencia o posicion de memoria,
				#que la "funcion anonima"o lambda que hemos creado.

#Funciones Decoradores:
	#Los decoradores son funciones que reciben como parámetros otras funciones y
	#retornan como resultado otras funciones con el objetivo de alterar el funcionamiento original
	#de la función que se pasa como parámetro. Hay funciones que tienen en común muchas funcionalidades,
	#por ejemplo las de manejo de errores de conexión de recursos I/O 
	#(que se deben programar siempre que usemos estos recursos) o las de validación de permisos
	#en las respuestas de peticiones de servidores, en vez de repetir el código de rutinas podemos abstraer,
	#bien sea el manejo de error o la respuesta de peticiones, en una función decorador.

	#Ej:
		# def tablas(funcion):
		#     def envoltura(tabla=1):
		#         print('Tabla del %i:' %tabla)
		#         print('-' * 15)
		#         for numero in range(0, 11):            
		#             funcion(numero, tabla)
		#         print('-' * 15)
		#     return envoltura
		# 
		# @tablas
		# def suma(numero, tabla=1):
		#     print('%2i + %2i = %3i' %(tabla, numero, tabla+numero))
		# 
		# @tablas
		# def multiplicar(numero, tabla=1):
		#     print('%2i X %2i = %3i' %(tabla, numero, tabla*numero))

		# Muestra la tabla de sumar del 1
		#suma()    
		# Muestra la tabla de sumar del 4 
		#suma(4)    
		# Muestra la tabla de multiplicar del 1
		#multiplicar()    
		# Muestra la tabla de multiplicar del 10
		#multiplicar(10) 

#Funcion Generadora:
	#Un generador es un tipo concreto de iterador. Es una función que permite obtener sus resultados paso a paso.
	#Ej:
		# def par(inicio,fin):
		#   for i in range(inicio,fin):
		#     if i % 2==0:
		#       yield i

		# datos = par(1,5)
		# next(datos)
		#2
		# next(datos)
		#4

		# for i in par(20,30):
		#   print(i,end=" ")
		#20 22 24 26 28

		# lista_pares = list(par(1,10))
		# lista_pares
		#[2, 4, 6, 8]
