#Boleanos
#Que se considera False:
	#Cualquier valor real que tenga su parte decinal terminada en 0
	#Valor entero que sea 0
	#El valor None(o ausencia de valor) se considera tambien False
	#Cualquier secuencia/Coleccion vacia o si alguna de estas tiene un valor 0, como diccionario,tuplas,listas {},(),[] etc.. se considera False
	#Ejemplo: Esto devolvera la cadena "Falso", ya que 0 es considerado 'False'
	# if 0:
	#	print("Ok")
	# else:
	#	print("Falso")

# siempre podemos usar para negar un resultado booleado la palabra reservada 'not' por ejemplo si a=true podemos realinar not a y este devovlera 'False'
 
 #Funciones:
 #all() recibe una coleccion o secuencia.
 	#all([1,true,2.45]) devuelve True por que ninguno de sus elementos es 0 o vacio
 	#all([1,true,""]) devolvera falso por que uno de sus elemntos es una cadena vacia
 	#all([1,true,0]) devuelve falso por que uno de sus elementos es 0
 #any() devuelve verdadero si alguno de sus elemento de la colecion o secuencia es verdadero o true, es decir..
 	#contine al menos un elemento en la coleccion que se considera verdadero.
	#Ejemplo any([1,"",0]) devolvera true por que uno de sus elemento es considerado true que seria el 1