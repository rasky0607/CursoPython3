#Tipo de datos Map o diccionarios con clave valor,(en php por ejemplo son los arrays asociativos) 
#Son MUTABLES
#Dentro de los diccionarios, no existe el orden
#Formas de crear un diccionario:
	#Crear un diccionario vacio:
		#Ej: miDict={} y rellenando las claves 1 a 1--> miDict["one"]=1
	#Usando el costructor
		#Ej: a=dict(one=1,two=2,three=3)
		#a["one"] Acceso a los datos (si intentamos acceder a una clave que no existe en el diccionario, dara una excepcion)
	#Otra forma de crear el diccionario es utilizando la llave:
		#Ej: a={'one':1,'two':2,'three':3}
	#Usando el metodo de compresion zip para crear el diccionario con listas:
		#Ej:c = dict(zip(['one', 'two', 'three'], [1, 2, 3])) Donde lo primero son las claves y lo segundo una lista con los valores
	#Usando tuplas y clave valor
		#Ej: d = dict([('two', 2), ('one', 1), ('three', 3)])
	#Usando el constructor y las llaves a la vez para crear el diccionaro:
		#Ej:e = dict({'three': 3, 'one': 1, 'two': 2})


#Los diccionarios pueden ser comparados entre sí:
	#Ej:a==b==c

#Operador de pertenencia 'IN', para comprobar si una clave esta en el diccionario:
	#Ej:"two" in a

#Funciones o metodos de los diccionarios:
#	dict1.clear       dict1.get         dict1.pop         dict1.update      
#	dict1.copy        dict1.items       dict1.popitem     dict1.values      
#	dict1.fromkeys    dict1.keys        dict1.setdefault  

	#Funcion del() para eliminar un elemento del diccionario:
		#Ej: del(a["one"]) de este modo estamos elimiando el dato del diccionario que tiene como clave "one"

	#Funcion iter() me devuelve un interador con las claves del diccionario
	#de este moddo podemos podemos usar la funcion next() repetidamente para recorrerlo
		#Ej:miIter=iter(miDict) next(miIter)
		#Ej2: next(iter(miDict))

	#Funcion copy() para copiar como las listas un diccionario a otro diferente, es decir que no apunte a la misma posicion de memoria
	#o dicho de otro modo con distinta referencia:
		#b=miDict.copy()

	#Funcion fromkeys() nos permite inicializar un diccionario con unas claves indicadas pero con valores vacios
	#o incluso iniciar todas estas claves a un mismo valor unico
		#Ej1:dict.fromkeys(["one","two","three"]) Inicializamos las claves con valores vacios
		#Ej2:dict.fromkeys(["one","two","three"],100) Inicializamos todas las claves con un valor unic, el "100"

	#Funcion dict.update() nos permite añadir elementos a un diccionario
	#incluso añadir elemento de un diccionario a otro.

		#Ej:Añadimos a un diccionario los elementos de otro diccionario:
		#dict1 = dict(one=1, two=2, three=3)
		#dict2 = {'four':4,'five':5}
		#dict1.update(dict2)
		#Resultado -> dict1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

	#Funcion dict1.setdefault() tiene dos comportamientos:
		#Si le indicamos una clave que ya existe y un valor que puede ser el suyo o no,
		#nos deolvera el valor de esa clave en el diccionario(independientemente del valor que le indicaramos).
			#Ej1:(Indicando un valor que ya existe en el diccionario)
			#dict1={'one': 1, 'two': 2, 'three': 3, 'four': 4}
			#dict1.setdefault("one",40)
			#Nos devuelve -> 1

		#Si le indicamos una clave que no existe,creara en el diccionario un nuevo elemento con esa clave y ese valor indicados.
			#Ej2:(Indicando un valor que NO existe en el diccionario)
			#dict1={'one': 1, 'two': 2, 'three': 3, 'four': 4}
			#dict1.setdefault("five",5)
			#Nos devuelve -> 5
			#Y el diccionario ahora tendra un nuevo elemento -> {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five':5}
	
	#Funcion Get() el cual indicando una clave, nos devuelve el valor de esta:
		#Ej:dict1.get("five")

	#Funcion Pop() [eliminar] como en la listas, devuelve el valor de dicha clave Y lo elimina del diccionario:
		#Ej:dict1.pop("one")

	#Funcion keys() nos devuelve una tupla con las claves del diccionario:
		#Ej:dict1.keys

	#Funcion Values() nos devuelve una tupla con los valores de cada clave de el diccionario:
		#Ej:dict1.values

	#Funcion items() nos devuelve por tuplas las claves y valores del diccionario:
		#Ej:1dict1.items()
		#Nos devuelve -> dict_items([('one', 1), ('two', 2), ('three', 3)])


#Estos metodos keys(),values() y items() son DINAMICOS:
#Es decir por ejemplo, si guardamos las claves de un diccionario en una variable:
	#Ej:dict1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5} (Creamos el diccionario)
		#misClaves=dict1.keys (Guardamos las claves en una variable)
		#Si luego añadimos una clave nueva al diccionario:
		#dict1["seven"]=7
		#automaticamente la variable "misClaves" se actualizara y contendra tambien la clave "seven" sin tene que ejecutar de nuevo el metodo keys().
		#Es decir misClaves -->({'one', 'two', 'three', 'four', 'five','seven')}
	
