#Lectura de ficheros de texto

#FUNCIONES BASICAS de apertura y cierre de fichero:
#Funcion open("rutaAlFichero",ModoEnQueAbrimosElFichero) para abrir el fichero
#Si no se indica el modo, se abrira en modo lectura.
	#Ej:mifi = open("miEjemplo.txt","w")

#Funcion close() para cerrar el fichero IMPORTANTE!
	#mifi.close() 	

	#	Modos de acceso

	#Los modos que podemos indicar son los siguientes:
	#Los que terminan en 'b'es para ficheros binarios.
	
	#Modo 	Comportamiento 															Puntero
	#r		Solo lectura													Al inicio del archivo
	#rb		Solo lectura en modo binario 	
	#r+		Lectura y escritura 											Al inicio del archivo
	#rb+	Lectura y escritura binario										Al inicio del archivo
	#w		Solo escritura. Sobreescribe si existe. 						Al inicio del archivo
			#Crea el archivo si no existe.	
	
	#wb		Solo escritura en modo binario.									Al inicio del archivo
	#		Sobreescribe si existe. Crea el archivo si no existe.

	#w+		Escritura y lectura. 											Al inicio del archivo
	#		Sobreescribe si existe. Crea el archivo si no existe.	
	
	#wb+	Escritura y lectura binaria. Sobreescribe si existe.			Al inicio del archivo
	# 		Crea el archivo si no existe.
	
	#a		Añadido (agregar contenido). Crea el archivo si no existe.		Si el archivo existe, al final de éste. 
	#																		Si el archivo no existe, al comienzo.

	#ab		Añadido (agregar contenido).									Si el archivo existe, al final de éste. 
	#																		Si el archivo no existe, al comienzo.

	#a+		Añadido y lectura. Crea el archivo si no existe.				Si el archivo existe, al final de éste.
	#																		Si el archivo no existe, al comienzo.

	#ab+	Añadido y lectura en binario. Crea el archivo si no existe		Si el archivo existe, al final de éste.
	#																		Si el archivo no existe, al comienzo.

	#Podemos trabajar con ficheros binarios y con ficheros de textos.

#Abrir el fichero, leerlo y cerrarlo en una sola linea
#En este caso NO necesitaremos close()
	# with open("ruta","r") as nombreInventado: 
	#Ej:with open("ejemplo.txt","r") as miArchivo:
	#		micontenido=miArchivo.read()
	#En "micontenido" tendremos todo el contenido del fichero 

#Propiedades:
# .closed -> nos devuelve true o false segun si el fichero esta cerrado o no.
# .mode-> para saber en el modo en el que esta abierto el fichero.
# .name-> nos indica el nombre del fichero	

#Funciones ficheros:

	#LECTURA#
#read() --> lee  y devuelve una cadena con el contenido total del fichero
	#Ej:f.read()
	#SOBRECARGA read(4) podemos leer un numero determinado de caracteres indicandoselo como parametro
	#este leeara el numero de caracteres indicado a partir de la posicion actual
		#Ejf.read(4)

#tell()-> indice o posicion actual en la que esta el puntero
	#Ej:f.tell()

#seek()-> Nos permite colocar el puntero en una posicin determinada
	#Ej:f.seek(5)	

#readline()->Nos devuelve una cadena de una linea del fichero
	#Ej:f.readline()

#readlines()-> Nos devuelve una LISTA con todas las lineas del fichero
	##Ej:f.readlines()

	#ESCRITURA#
#write("cadena")->Escribe una cadena en el fichero y nos devuelve la posicion de donde se quedo el puntero
	#Ejf.write("hola pepe")

#writelines("ListaDeCadenas")-> indicandole una lista de cadenas,escribira cad auna linea linea
	#Ej:f.writelines(["linea1","linea2","linea3"])

#Tambien podemos recorrerlo linea a linea de la siguiente manera:
	#with open("./FicherosDePrueba/ejemplo1.txt","r+") as archivo:
		#for linea in archivo:
			#print(linea)

#Ejemeplo de pruebas de apertura de fichero,sin necesidad de usar close y teniendo que usar close
with open("./FicherosDePrueba/ejemplo1.txt","r+") as archivo:
	contenido=archivo.read()
print(contenido)

f=open("./FicherosDePrueba/ejemplo1.txt","r+")
c=f.read()
print(c)
f.close()
print(f.closed)
	