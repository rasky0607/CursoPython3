#realizar el factorial d eun numero introducido por teclado es decir multiplicar desde ese numero hasta la unidad
#o desde la unidad a hasta ese numero !5 = 5x4x3x2x1 (Aun que oviamosel 1 en los bucles)
numero=None
numero=int(input("Realizar factorial de el numero: !"))
result=1
contador=numero
print("Con bucle While:")
while contador>=2:
	if(contador!=1):	
		print(str(result)+" X "+str(contador))
	result*=contador
	contador-=1
else:	
	print("Resultado -> "+str(result))
	pass
#Reiniciamos  variables
print("\nCon bucle For:")
contador=numero	
i=0
result=1
for i in range(2,numero+1):
	if(i!=1):	
		print(str(result)+" X "+str(i))
	result*=i
else:
	print("Resultado -> "+str(result))