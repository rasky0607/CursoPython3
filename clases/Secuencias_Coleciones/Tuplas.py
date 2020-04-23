#Ejemplo de como crear y manejar Tuplas, las cuales a diferencia de las listas son INMUTABLES
#Estas a dfierencia de la slitas tambien, se crean con ()  NO con []
#Ej: mitupla=(1,2,3,4)
#Ej2:mitupla=tuple([1,2,3]) Usando el contructor y pasandole una coleccion/secuencia
#Podemos crear un tubla sin los parentesis ya que el contructor de este realmente es la coma no el parentesis
	#Ej3:mitupla=1,2,3

#Concepto de empaquetado y desempaquetado de tuplas:
	#Desempaquetado --> guardar cada uno de los elementos d euna tupla en variables idependientes.
		#Ej:mitupla=1,2,3
		#	a,b,c=mitupla --> el resultado será a=1,b=2,c=3
		#(El empaquetado sera al contrario creo...)

#Las tuplas pueden usar el operador de pertenencia "IN", concatenarse como las listas etc..
#Son iguales en todo.. exceto que son INMUTABLES, es decir solo almacena valores no modificables:
	#Es decir,NO SE PUEDE MODIFICAR un elemento como:
	#Ej:mitupla=1,2,3
	#mitupla[1]=10
	#Tampoco se puede utilizar la funcion DEL() para eliminar ciertos elementos de la tupla

	#La clase Tupla SOLO PERMITE utilizar dos metodos de las secuencias/coleciones
	#tupla.count y tupla.index, es decir recoger el indice o posicion delelemento o contar repeticiones de uno de estos
