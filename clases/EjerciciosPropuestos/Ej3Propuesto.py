#Ejercicio 3º propuesto Calcula el perimetro y area de un circulo dado su radio
import math #Importacion de clase matematica math par usar la constante pi

r=None

print("Calcularemos el area y perimetro de un circulo, dada su radio.")
#IMPORTANTE: recordar que la funcion input() devuelve una cadena, de modo que tenemos que convertirlos o casting
r=float(input("Radio: "))

#Disitntas formas de mostrar el resultado de salida
print("El area del circulo es: %.2f"% (math.pi*(r**2)))
print("El perimetro del circulo es: %.2f"% (2*math.pi*r))

#print("El area del circulo es: ", str(a*b))
#print("El area del circulo es: %.2f " % (a*b))