#Solicitar una cadena de texto por teclado y  crear un diccionario
#con cada una de las palabras como key y el numero de veces que aparece dicha palabra en la cadena
	#que bien que estoy resutado->{'que':2,'bien':1,'estoy':1}
diccionario={}
cadena=input("Dime una cadena. ")
listCadena=cadena.split(" ")#La separamos para poder preguntar por cada palabra

print(listCadena)

for i in listCadena:
	print("La cadena "+str(i)+"-> "+str(cadena.count(i)))
	diccionario.setdefault(i,cadena.count(i))#Creamos la clave si no esta y le añadimos el valor de el numero de veces que se repite en la cadena

print("El diccionario "+str(diccionario))