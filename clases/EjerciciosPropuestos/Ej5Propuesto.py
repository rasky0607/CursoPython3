#Ejercicio 5 propuesto, pedira una palabra al usuario para luego imprimirla 1000 veces con espacios incluidos
p=input("Palabra que desea imprimir ")
repeticion=1000
print((p+" ")*1000,end='***')#El parametro end='***' indica que el final de print o finar de linea se pintara con el caracter indicado  en este caso '***'

#Otra forma  mas complicada de hacerlo >< aun que en este se mete salto de linea
#veces=1
#while veces<=1000:
#	print("["+str(veces)+"] "+p)
#	veces=veces+1
