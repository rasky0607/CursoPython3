#obtenemos si el numero pasado por teclado es par o impar

num=float(input("Indicame un numero. "))

if(num%2==0):
	print("Este numero es ##par##.")
else:
	print("Este  numero es ##impar##.")

print("El resto de la operacion:"+str(num)+"/2= "+ str(num%2))
