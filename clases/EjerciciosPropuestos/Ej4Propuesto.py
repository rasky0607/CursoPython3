#Ejercicio 2º propuesto Calcula la suma resta multiplicacion y division entre dos numeros dados.

n1=None
n2=None
print("Calcularemos la suma,resta,multiplicacion y division entre dos numeros dados.")
#IMPORTANTE: recordar que la funcion input() devuelve una cadena, de modo que tenemos que convertirlos o casting
n1=float(input("1º Numero: "))
n2=float(input("2º Numero: "))

#Disitntas formas de mostrar el resultado de salida
print("La suma de "+str(n1)+" y "+str(n2)+" es-> "+ str(n1+n2)+" sin formateo a 2 decimales")
print("La resta de "+str(n1)+" y "+str(n2)+" es-> ", str(n1-n2)+" sin formateo a 2 decimales")
print("La multiplicacion de "+str(n1)+" y "+str(n2)+" es-> %.2f" % (n1*n2)+" con formateo a 2 decimales")
print("La division de "+str(n1)+" y "+str(n2)+" es-> %.2f" % (n1/n2)+" con formateo a 2 decimales")