#Tratamiento de excepciones o errores en ejecucion
#Bloque de tratamiento:
#try:
	#Operaciones
#except NombreDeExcepcion:
	#Operaciones cuando se produce la excepcion
#except: (Sin excepcion concreta)
	#Operaciones cuando se produce la excepcion
#finally: (Esta instruccion se EJECUTA SIEMPRE al terminar)

#Ejemplo 1 de manejo de excepciones:
try:
	print ("Otro ejemplo de excepciones [Ejempplo 1]")
	cad=int(input("Introduce un numero para divirlo por 10: "))
	print (10/int(cad))
except ValueError: #Excepciones concreta que puede lanzar la operacion
	print("No se puede converir a entero")
except ZeroDivisionError:#Excepciones concreta que puede lanzar la operacion
	print("No se puede divir por cero")
except:#El resto de excepciones posibles que puede lanzar la operacion
	print("Otro error")
finally:
	print("Se termina el programa")

#Ejemplo 2 de tratamiento de excepciones, bucle para pedir un dato correcto cuando falla el introducido:

#while True:
#   try:
#     x = int(input("Introduce un número:"))
#     break
#   except ValueError:
#     print ("Debes introducir un número")

#Ejemplo 3 Obtener informacion de una excepcion producida:
	#Ya que las excepcion es un objeto, podemos crear uno y obtenr la informacion de este.

#	cad = "a"
# try:
#   i = int(cad)
# except ValueError as error: #Damos un nombre (error) al objeto de la excepcion ValueError
#   print(type(error))
#   print(error.args) #Obtenemos la informacion del error producido
#   print(error)
 
 #Ejemplo 3 excepciones de tipo raise:
 	#(Excepciones propagadas por las funcioes)
 	#Si construimos una función donde se maneje una excepción podemos hacer que la excepción se envía a la función desde la que la hemos llamado. Para ello utilizamos la instrucción raise. Veamos algunos ejemplos:
print ("Otro ejemplo de excepciones [Ejempplo 3]")
def nivel(numero):
    if numero<0:
        raise ValueError("El número debe ser positivo:"+str(numero))#Personalizamos el mensaje que  queremos enviar al program principal al progarla excepcion
    else:
        return "EL numero es posivo -> "+str(numero)

#Con la palabra reservada "raise" también podemos propagar una excepción en concreto:

def dividir(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        raise #Propaga la excepcion al programa principal
#LLamada a funciones
print(nivel(-2))

try:
	print(dividir(2,0))
except:
	print("No se puede dividir.")

