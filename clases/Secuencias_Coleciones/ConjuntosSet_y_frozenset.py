#Los conjuntos de Set y Frozenset son lista de datos no repetidos.
#El tipo de dato Set -> Es MUTABLE
#El tipo de dato Frozenset -> Es INMUTABLE

#Crear un conjunto Set:
	#Ej:miset=set() usando el constrcutor
	#Ej2:miset=set{1,2,3} Sin usar el constructor, is no usando las llaves
	#Ej3:Podemos crear un conjunto Set a partir de una lista(Aun que puede ser cualquier tipo de secuencia) con repeticiones
		#miset=set([1,3,4,5,1,3,8,9])


#Metodos de conjuntos Set:
	#set1.add                          set1.issubset
	#set1.clear                        set1.issuperset
	#set1.copy                         set1.pop
	#set1.difference                   set1.remove
	#set1.difference_update            set1.symmetric_difference
	#set1.discard                      set1.symmetric_difference_update
	#set1.intersection                 set1.union
	#set1.intersection_update          set1.update
	#set1.isdisjoint     

#Ej: set1.symmetric_difference_update(set2) -> recoge la diferencia entre ambos conjuntos y modifica y añade esta el conjunto set1
#Ejset1.remove(2) elimina el elemento del conjunto [Si no lo encuentra lanza excepcion]
#Ejset1.discard(2) elimina el elemento del conjunto [Si no lo encuentra NO lanza excepcion]

#Crear un conjunto Frozenset:
	#Es igual que el Set solo que usando su constructor frozenset()
		#Ej:mifrozenset=frozenset([1,3,4,5,1,3,8,9])

#Metodos de conjunto Frozenset:
	#fset1.copy                  fset1.isdisjoint            fset1.symmetric_difference
	#fset1.difference            fset1.issubset              fset1.union
	#fset1.intersection          fset1.issuperset		

#A los conjuntos Set podremos añadir elementos con add()por ser MUTABLES,
#mientras que a Frozenset no por ser INMUTABES:
#Ej:miset1.add(4)

#En estos tipos de colecciones solo podemos hacer
#Recorrerlas con un bucle, operadores de pertenecia 'in' y 'in not' y algunas funciones predefinidas como:
#lend(),max(),min(),short() etc ..