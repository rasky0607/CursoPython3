#Funciones matematicas y intriduccion a programacion funcional en python

#Funciones:

#map() -->Esta funcion DEVUELVE un objeto map y ejecuta una funcion indicada a un conjunto de datos
#		  que esta guardado en una sencuancia/coleccion.
#	 Esta funcion permite indica una funcion que se va ejecutar sobre cada uno de los elementos de la coleccion
#	 Ej 1: lista=["1","3","9","8"] (Queremos convertir cada una de esas cadenas a enteros)
#	 Para ello usamos la funcion map(funcionAEjecutar,ColeccionSobreLaqueSeEjecuta) map(int,lista)
#	 Esto quiere decir que sobre cada uno de los elementos de la lista se ejecutara funcion int() par convertir una cadena a entero

#funcion filter--> Es igual que map(), pero sirve para filtrar el conjunto de datos optenidos.
#					Es decir, por ejemplo creamos una funcion que identifique numeros pares,
#					y deseamos recoger los elementos pare de nuestra lista, para ellos usamos lo siguiente
#					Ej:list(filter(miFuncPar,lista)) , usamos el constructor list(), para convertir el resultado en lista

#Funcion reduce--> esta esta dentro de la libreria o modulo 'functools', es similar a las dos anteriores.
#					pero en lugar de obtener un conjunto de datos, optenemos uno solo.
#					Ej: imagina que queremos sumar todos los elementos de una lista.
#					Para ello nos creariamos una funcion Suma() y la usariamos de la siguiente forma:
#					reduce(Suma,lista) , en este caso no necesitamos castear nada como antes con el constructor list()

#Listas Comprimidas: realmente sun funcion es obtener una lista modificada a partir de otra, realizando operaciones
#					Matematicas.
#					Por ejemplo en este caso, queremos recoger los cubos de todos los elementos de una lista
#					Usariamos --> [x ** 3 for x in [1,2,3,4,5]]
#					Resultado --> [1, 8, 27, 64, 125]
#
#					En este otro ejmplo, nos quedamos con los pares de los 10 primeros numero de un bucle
#					Usaremos --> [x for x in range(10) if x % 2 == 0]
#					Resultado --> [0, 2, 4, 6, 8] 
#					
#					En este tercer ejemplo obtendremos una lista que es la suma de cada uno de los elementos
#					de dos listas difernetes
#					Usaremos --> [x + y for x in [1,2,3] for y in [4,5,6]]
#					Resultado --> [5, 6, 7, 6, 7, 8, 7, 8, 9]



#Ej1 funcion map():
lista=["1","3","9","8"]
print(lista)
print(list(map(int,lista)))
