#Nota1:Todo lo que declaramos en python es un objeto d euna determinada clase,
	#de ese modo una funcion es un objeto de la clase (Function)

#Nota2:Siempre en python el pase de parametros es por referencia.

#Funciones en python3
	#Ambito de las variables:
		#Tanto los parametro como las variables que creamos dentro dela funcion,
		#tiene ambito local,(Solo existen dentro de la funcion),
		# solo si la definimos con la palbra reservada global, tendra un ambito global y no local
	
	#Para definir la funcion:
		#utilizamos la palabra reservada "def" para definir una funcion,
		#un nombre y un conjunto de parametros y los :
		#Es opcional despues de la definicion del metodo utilizar triple comillas dobles para documentar la funcion,
		#de este modo podremos utilizar la funcion help(), la cual nos devolvera esta documentacion de las funciones	
		
		#Ej: def mifuncion1(p1,p2,p3):
		#		"""Calcula el factorial de un número"""		<--COmentario que devolvera la funcion help(mifuncion1)  

		#Ej2:[Funcion al completo].
#	 def factorial(n):
#   	"""Calcula el factorial de un número"""
#   	resultado = 1
#   	for i in range(1,n+1):
#     		resultado*=i
#   	return resultado


	#Tipos de parametros:
		#Parametro formal:Parametros que recibe una funcion,es decir su definicion f1(p1,p2), en ese caso serai p1 y p2
			#En estos se pueden indicar valores por defecto
				#f1(a,b,c='miValorPorDefecto',d="valorPordefecto2")
				#[Estos parametro c y d no se modificaran si no se les indica en la llamada ala funcion otro valor]
				#Ej:
					# def operar(n1,n2,operador='+',respuesta='El resultado es '):
					#   if operador=="+":
					#     return respuesta+str(n1+n2)
					#   elif operador=="-":
					#     return respuesta+str(n1-n2)
					#   else:
					#     return "Error"


		#Parametro real:Parametros que realmente se pasan a la funcion al usarla f1(5,10) es decir 5 y 10
			#Podemos clasificar los parametro Reales, segun la forma de mandarlos:
				#Posicionalmente: Es decir sin indicar el nombre del parametro,si no que se asigna segun el orde de su declaracion
					#Ej1 f(a,b), f(1,8), a=1 y b=8
				#Con clave o Keyword: es decir indicando el nombre del parametro.
					# f1(a,b), f1(a=2,b=8)

					#Nota3:Si en la definicion de parametros encontramos un asterisco'*', los parametro que esten definidos
						#despues de este, hay que pasarles el valor como clave o Keyword, es decir
						#indicandoe l nombre del parametro = y el valor de este.
						#Ej:
						# def operar(n1,n2,*,operador='+',respuesta='El resultado es '):
						#   if operador=="+":
						#     return respuesta+str(n1+n2)
						#   elif operador=="-":
						#     return respuesta+str(n1-n2)
						#   else:
						#     return "Error"

			#Parametros Arbitrarios: Esto son representados, por un asterisco '*' seguido de un nombre.
				#Esto indica que puede  o no recibir una lista indefinida de parametros,y no se puede usar el metodo keyword para indicarlos,
				#e internamente en la funcion seran recorridos como una lista.
				#Ej:
				# def sumar(n,*args):
				#   resultado=n
				#   for i in args:
				#     resultado+=i
				#   return resultado
				#
				#Una funcion de este tipo puede recibir una lista como argumentos posicionales en *args del siguiente modo:
				# sumar(n=1,*milista)  [IMPORTANTE colocar el * antes de la coleccion que le pasamos]

			#Este caso es igual que anterior [Parametros Arbitrarios], con la salvedad de
			#que en este caso se indica con doble asterisco'**' y los parametros DEBEN indicarse como keyword.
			#Ej:
			#[Los parametros indicados en el kwargs son realmente un diccionario que posteriormente recorreremos]
			# def saludar(nombre="pepe",**kwargs):
			#   cadena=nombre
			#   for valor in kwargs.values():
			#    cadena=cadena+" "+valor
			#   return "Hola "+cadena
 


