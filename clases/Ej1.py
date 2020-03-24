#Este primer ejemplo NO COMPILARA ya que es##
##solo meramente orientativo para ver estructuras de control##

#IMPORTANTE en Python es muy importante controlas las tabulaciones correctamente 
#Ya que de esto depende en gran medida la correcta compilacion del programa
if num>=0:
	while  num<10:
		print(num)
		num = num + 1

#Para ejecutar un programa de python en el interprete o la consola:
#Para ejecutarlo en nuestra consola el propio interprete como cuando ejecutaos mysql,
#primero debemos tenerlo includo en la variable Path en caso de  estar usando Windows,
#A diferencia de Linux y IOS, tras esto solo debemos ejecutar en la consola en la ruta donde este
#nuestro programa o fichero .py "python3 nombrefichero.py"

numero=5
#Al terminar interrogantes como los if /else o estructuras de control se utilizan
#los : para finalizar
if numero==5:
	print("correcto!")

if numero==3:
	print("medio correcto!")
else:
	print("nada correcto")
#podemos realizar varias intrucciones en una misma linea separadas por ;
#pero (No es muy recomendable)
edad = 15; print(edad)

#Podemos escribir dos intrucciones en una linea siempre y cuando sea un interrogante,
#como el mostrado a continuacion y la siguiente instruccion sea una(Aun que noe  smuy recomendable)
if condicion1: print("es verdad")

#La \ nos permite continuar escribiendo una misma instruccion
# en la siguiente linea como por ejemplo un if demasiado largo
if condicion1 and condicion2 and condicion3 and \
	condicion4 and condicion5:

#Las expresiones entre parentesis, llaves o corchetes
#pueden ocupar varias lineas
#Ejemplo de declaracion de listas
	dias=['lunes','martes','miercoles','jueves','viernes',
	'viernes','sabado','domingo']