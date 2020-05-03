#Modulo de lectura de python para ficheros CSV
#Importamos el modulo de csv
import csv

#Nota1: podemos usar el meotod seek() de los ficheros para mover el puntero a una posicion concreta
#En primer lugar abrimos el fichero de "prueba.csv"como un fichero normal de texto en modo lectura
f=open("./FicherosDePrueba/prueba.csv","r")
#Usamos el metodo reader() de la clase csv importada por la libreria csv y leemos el fichero
#Este metodo, nos devolvera un tipo _csv.reader
#SOBRECARGA csv.reader(fichero,quotechar='"') ,quotechar indica el separador que ahi en el csv, ya sean una coma  una almohadilla etc..
contenido=csv.reader(f)

#Convertirmos el contenido en una lista
#Esta sera una lista que a su vez contine una lista del contenido de cada fila:
#Vista de la lista con listas que hemos creado:
#print(list(contenido))
#[
	#['4/5/2015 13:34', 'Apples', '73'],
 	#['4/5/2015 3:41', 'Cherries', '85'],
  	#['4/6/2015 12:46', 'Pears', '14'],
    # ['4/8/2015 8:59', 'Oranges', '52'],
    #['4/10/2015 2:07', 'Apples', '152'],
	#['4/10/2015 18:10', 'Bananas', '23'],
	#['4/10/2015 2:40', 'Strawberries', '98']
#]

datos=list(contenido)
#Obtener de la primera fila(o primera lista  de la lista padre) el primer elemento
print(len(datos[0]))
print(datos[0][0])
#Obtenemos el segundo elemento de la primera fila o lista....
print(datos[0][1])
#Obtenemos el primer elemento de la segunda fila o lista
print(datos[1][0])
contador=0
for i in datos:
	print("Datos de fila ["+str(contador)+"]")
	for j in i:
		print(j)

	contador+=1
else:
	print("FIN DEL LISTADO")

#Cerramos el fichero
f.close()


#Ejemplo de escritura en fichero CSV
#La funcion writerow(), nos permite escribir una fila
#La funcion writerows(), nos permite intriducir una lista con varias listas que represetarian las distintas filas
#import csv
#fichero = open("ejemplo3.csv","w")
#contenido = csv.writer(fichero)
#contenido.writerow(['4/5/2015 13:34', 'Apples', '73']) 
#contenido.writerows(['4/5/2015 3:41', 'Cherries', '85'],['4/6/2015 12:46', 'Pears', '14'])
#fichero.close()