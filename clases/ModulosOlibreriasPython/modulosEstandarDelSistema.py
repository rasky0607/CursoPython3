#Modulos estandar del sistema en python
#import nombreModulo

#Nombre de Modulos:
	# os -> nos da funcionalidad del sistema operativo.
		#Como por ejemplo funciones para optener directorio donde estamos trabajando.
		# o por ejemplo la funcionos.system("ls") -> 
			#nos permite ejecutar instrucciones directamente en el sistema operativo (como comandos de consola)
		#Enlace de mas info sobre este modulo:
		#https://docs.python.org/3.4/library/os.html#module-os
	
	#os.path-> Este submodulo nos ofrece funcionalidad sobre la ruta de directorios o sistema de archivos de nuestro Sistema
	
	#subprocess->Nos permite guardar la salida de comandos ejecutados en el sistema
		#Ej: salida = subprocess.check_output("ls") el cual devuelve un tipo byte que tendremos que convertir

	#shutil -> Nos permite realizar operaciones con ficheros como copiar, acceder a propiedades, etc
	#sys-> nos permite trabajar y perdir informacio del interprete de python3.
		#Ej1:Como indicar parametros a un script de python cuando este es llamado a su ejecucion usando  la propiedad 
		#sys.argv , el cual es recoge una "Lista " de los parametro indicados.
		#Imaginemos tene un script llamdado sumar.py

		#!/usr/bin/env python    
		#import sys
		#print("Has instroducido",len(sys.argv),"argumento")
		#suma=0
		#for i in range(1,len(sys.argv)):
		#    suma=suma+int(sys.argv[i])
		#print("La suma es ",suma)

		#Llamad del script y resulado de salida en la consola:
		#$  python3 sumar.py 3 4 5
		#Has introducido 4 argumento
		#La suma es  12
		#NOTA IMPORTANTE: la propiedad sys.argv, recoge como argumento tambien el nombre del script por lo que
		#a la hora de recorrer los argumentos abra que omitir el primer argumento que es el nombre del script

		#Ej2: la funcion exit() sys.exit(), terminaria la ejecucion de un programa