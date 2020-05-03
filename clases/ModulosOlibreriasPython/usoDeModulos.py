#Uso de moduos o librerias de pyhton3

#Modulo:
#Cada fichero con la extension ".py"  es para nosotros un modulo 
#y todos los elemntos dentro de este lo podemos importar en otro como ocurre en php.
	#Modulo predefinidas en python del SISTEMA llamado "sys"
	#import sys
	#Para acceder a los distintos submodulos de este:
	#sys.builtin_module_names
	#Nombre de algunos de los paquetes que podemos encontrar en "sys":
	#('_ast', '_bisect', '_codecs', '_collections', '_datetime', '_elementtree',
	# '_functools', '_heapq', '_imp', '_io', '_locale', '_md5',
	# '_operator', '_pickle', '_posixsubprocess', '_random', '_sha1',
	# '_sha256', '_sha512', '_socket', '_sre', '_stat', '_string', '_struct',
	# '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'array',
	# 'atexit', 'binascii', 'builtins', 'errno', 'faulthandler', 'fcntl', 'gc', 'grp',
	# 'itertools', 'marshal', 'math', 'posix', 'pwd', 'pyexpat', 'select', 'signal', 'spwd',
	# 'sys', 'syslog', 'time', 'unicodedata', 'xxsubtype', 'zipimport', 'zlib')

	#Modulo para funciones matematicas predefinidas "math"
	#import math


#Paquetes:
#Los modulos los cuales los guardamos en directorios, son denominados paquetes

#Nota 1:en nuestros script de python o modulos, podemos tener puntos de entrada de nuestro programas,
	#es decir nuestros "Main" por los cuales se ejecutara el script, pero si este fichero o script es importado
	#como modulo a otro, el punto de entrada o "Main"  de ese fichero NO se tendra en cuenta.

	#Ej: Imaginemos que este es un script o fichero python que tenemos.
		#La  instruccion main, solo se llamara cuadno ejecutemos directamente este script,
		#pero si este es usado como modulo en otro que si se ejecuta como scrit,
		#el apartado MAIN de este se ignorara.
		#Solo se tendra en cuanta cuando ejetacos ese modulo/fichero, como un script
	#!/usr/bin/env python    

	#def cuadrado(n):
	#   return(n**2)
	#def cubo(n):
	#    return(n**3)
	#if __name__ == "__main__":
	#    print(cuadrado(3))
	#    print(cubo(3))

#Forma de importar otros modulos/librerias en otros scripts de python3

	#Importacion de modulos completos:
		#Opcion 1-> import nombreFicheroSinExtension
			#Ej: import useDeModulos

			#Para acceder a los campos y funciones de esta, deberemos usar el nombre cualificativo, es decir,
			#Ej:  useDeModulos.funcion1()

		#Opciones 2-> podemos realizar la importacion del mismo modo, pero indicando un alias, para no escribir tanto
			#Ej: import useDeModulos as m
			#	m.funcion1()

		#Opcion 3 -> En un mismo import podemos importar varios modulos.
			# import useDeModulos, moduoinventado
			#en este caso estamos importando dos modulos con un solo import

	#Importacion parcial de un modulo(es decir funciones concretas de este):
		#Ej: from useDeModulos import funcion1, en este caso para llamarla no necesitamos el nombre cualificativo
		#	solo el nombre de la funcion es decir , funcion1()
		
		#Ej2:Tambien podemos improtar varias funciones.
			#from useDeModulos import funcion1,funcion2,funcion3

		#Ej3:Tambien importar todas las funciones con el comodin *
		#	from useDeModulos import *

		#Ej4 Con estas importaciones parciales tambien podemos asignar alias.
		#Esto es util cuando tenemos dos modulos importados diferentes que tienen funciones con el mismo nombre.
		#	from useDeModulos import funcion1 as mf
		# 	from moduloInventado import funcion1 as mi
		#En este caso para llamar a esta funcion usariamos solo el alias , no el nombre cualificativo.
		# Es decir -->  mf()	y mi() son los alias de funciones con mismo nombre pero de modulos diferentes

	#Importar modulos que estan dentro de un paquete:
		#import nombrePaqueteOCarpeta.NombreDelModuloOFichero
		#Ej: import operaciones.potencias
		#para acceder a sus funciones pues usaremos el nombre cualificativo.
		#operaciones.potencia.cuadrado()

		#Ej2: Tambien podemos importar funciones dentro de estos paquetes
		#	  from operaciones.potencia import cuadrado
		#Llamariamos a esta simplemente cuadrado() sin usar nombre cualificativo

	#Funcion dir(nombreModuloIMportado), que nos indica los elementos que podemos utilizar de ese modulo