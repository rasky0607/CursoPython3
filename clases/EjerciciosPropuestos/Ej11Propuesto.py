#En este ejercicio se plantea recoger un numero por teclado
#y realizar la tabla de multiplicar de este del 1 al 10
#se plantear utilizar dos soluciones una con for  y otra con bucle while
numero=None
numero=int(input("Tabla de multiplicar del numero : "))
result=None
print("\nTabla de multiplicar con bucle while: ")
contador=1
while contador<=10:
	result=numero*contador
	print(str(numero)+"X"+str(contador)+" = "+str(result))
	contador+=1
	pass
print("\nTabla de multiplicar con bucle for: ")
for i in range(1,11):
	result=numero*i
	print(str(numero)+"X"+str(i)+" = "+str(result))
