#En este documento trataremos todas las peculiaridades de los caracteres y cadenas de caracteres,asi como bytes
#Funciones que  pasados bytes podemos obtener carateres de la tabla asccii
#Ej: chr(1004) resultado-->'6'
#	chr(97) resultado --> 'a'
#Funcion inversa a chr() es ord():
#Ej: ord("a") resultado--> 97

#De este modo podemos guardar una cadena con salto de linea, usando las comillas simple pero 3 veces
#En este caso se guarda incluo la tabulacion dada en la asignacion de la variable
cadena='''paco
	que
		tal '''	
#Otro modo de guardar cadenas con salto de lineas
cadena2="paco\nque\ntal"		
print(cadena)
print()
print(cadena2)

#Las cadenas, estas siguen siendo una secuencia o coleccion y son INMUTABES
#Por lo que se le pueden aplicar todas las funciones de las secuencias/coleciones de las secuencias INMUTABLES
#Es decir, no se pueden m odificar posiciones o eliminar posiciones concreta de la secuencia
#Constructor de String/cadenas str(),convierte el parametro en cadena
micadena=str(1992)
print(micadena)
#Funciones predefinidas de cadenas 
#Funcion repr() -> nos devueve la definicion de un tipo de un objeto pasado
#		Ej: repr(range(1,10)) resultado--> 'range(1,10)'
#Funcion eval()->Evalua la represnacion de un objeto, es decir si le pasamos una represancacion a eva()
#		Esta la ejecuta como si la inicializaramos en el codigo independientemente
#		Ej: eva(repr(range(1,10))) resultado-> creara un  objeto de tipo rango con valores del 1 al 9
#Funcion ascii()-> dado un caracter nos devuelve su presentacion, normalmente en la codificacion de latin1(codificacion de occidente)
#Funcion bin()-> dado un numero devuelve la represacion binaria de este