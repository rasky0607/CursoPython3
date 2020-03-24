#Ejercicio 2º propuesto Calcula el area de un triangulo dada su base y su altura

b=None
a=None
print("Calcularemos el area de un triangulo, dada una base y una altura.")
#IMPORTANTE: recordar que la funcion input() devuelve una cadena, de modo que tenemos que convertirlos o casting
b=float(input("Base: "))
a=float(input("Altura: "))

#Disitntas formas de mostrar el resultado de salida
print("El area del triangulo es: "+ str(a*b))
print("El area del triangulo es: ", str(a*b))
print("El area del triangulo es: %.2f " % (a*b))