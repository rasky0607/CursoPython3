#Estructuras De Control
#IMPORTANTE en python no existe swich()
	#Estructura de control alternativa Los if y  los else siempre tienen la expresion a evaluar y despues terminan en :
		#Ejemplo alternativa simple: 
				#if minutos<60:				
				#	print("bla bla bla ...")
				#else:
				#	print("bla bla bla ...")
		#Ejemplo alternativa multiple en lugar de usar 'elseif' como normalmente se hace , se usa 'elif'
				#if minutos<60:				
				#	print("bla bla bla ...")
				#elif:
				#	print("bla bla bla ...")
				#else:
				#	print("bla bla bla ...")
		#Forma reducida de usar el if con el siguiente orden:
			#(el resultado si la expresion es verdad | if[EXPRESION] | el resultado si la expresion es falsa) 
				#Ejemplo:
				#lang="es"
				# saludo="hola" if lang="es" else "hi"
				#Al pintar la variable saludo con un print, veremos que esta habra guardado la cadena "hola", ya que devolvio verdad.
				#En caso contrario habria guardado "hi".

