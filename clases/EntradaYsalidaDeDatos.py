#Entrada y salida de datos (recoger datos e imprimirlos)

#Funcion input():
	#Esta funcion se usa para recoger un valor por teclado.
	#devuelve siempre un tipo de cadena, es decir tenemos que reconvertir el resultado si lo necesitamos
	#Esta funcion tiene un parametro que pasada una cadena,la mostrará por consola antes de recibir el dato de entrada
		#Es decir n=input("Dame el primer dato")
			#Mostrara lo siguiente : ' Dame el primer dato _  ' y se quedara esperando el dato de entrada.
			#Pero IMPROTANTE el dato que recogera siempre será de tipo cadena, por lo tanto 'n' sera un string,
			# el cual deberá ser reconvertido a otro tipo si lo necesitamos como por ejemplo usnado la funcion ' int(n) '

#Funcion print():
	#Esta funcion es utilizada para imprimir valores de muchos tipos
	#Esta funcion por defecto nos colocara un espacio si imprimimos vario valores de golpe
		#Ejemplo: print(a+4,6,'p') imprimiera elValorDeAMas4 6 p
	#Esta funcion siempre terminara con u retorno de carro o \n.
	#Esta funcion puede recibirun parametro indicandole el separador que va usar en lugar del espacio que tiene por defecto
		#Ejemplo: print(2,4,'h',sep='-') imprimira 2-4-h
	#Esta funcion tambien puede recibir un parametro que indique el caracter de el final de la linea que por defecto es un salto de lina o \n.
		#Ejemplo: print(2,4,'h',sep='-',end='#') imprimira 2-4-h#
	#Esta funcion tambien puede usar el operador de concatenacion '+' o el multiplicador de cadenas.
		#IMPORTANTE a la hora de concatenar en la funcion print, todo debe ser string, deberemos convertir lo que no lo sea.
		#en estos casos no se le añade el separador espacio por defecto
		#Ejemplo1: print('hola'+str(5)+'adios') imprimira hola5adios
		#Ejemplo2: print('hola'*3) imprimira holaholahola

	#Formateo de salida estandar:
		#Podemos encontrar dos estilos, uno llamado 'Antiguo' y otro llamado 'Nuevo'

			#Estilo antiguo o usando comodines:
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

			#Estilo nuevo o usando la funcion 'format' de la clase String:
				#Ejemplo: 
					# print('El valor redondeado a 2 decimales de 2.4567 es '+ format(2.4567,'.2f') +' EL valor en octal de 12 es '+format(12,'o')+' el valor en binario de 17 es '+format(17,'b'))
				#Imprimira:
					# El valor redondeado a 2 decimales de 2.4567 es 2.46 EL valor en octal de 12 es 14 el valor en binario de 17 es 10001
