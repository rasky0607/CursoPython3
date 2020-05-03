#Lectura de ficheros Json
#Importar libreria que maneja  ficheros json
import json
datos=""
with open("./FicherosDePrueba/prueba.json") as fichero:
	#Metodo Load() lee las cadenas de tipo Json o un fichero Json,este devuelve normalmente un tipo dicccionario
	datos=json.load(fichero)
print("Tipo")
print(type(datos))
print("Datos")
print(datos)

#Escribir en un fichero json
datos2 = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
fichero2 = open("./FicherosDePrueba/prueba2.json","w")
#Funcion Dump() para escribir en un fichero json
json.dump(datos2,fichero2)
fichero2.close()

