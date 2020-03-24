#Ejercicio 6 propuesto pretende dada una cantidad de minutos a cuantas horas y minutos corresponde
minutos=0
tm=0#Total minutos
th=0#Total horas
minutos=int(input("Indicame una cantidad entera de minutos a convertir."))
minutos2=minutos #EJEMEPLO 2
if minutos<60:
	tm=minutos
	print("La catidad es ... \n  0 Horas \n "+ str(tm)+" Minutos")
else:
	while minutos>=60:
		minutos = minutos-60
		th +=1
		tm=minutos

print("CALCULO CON BUCLE WHILE: La catidad es ... \n "+str(th)+" Horas."+" \n "+ str(tm)+" Minutos.")

#EJEMEPLO 2
th=minutos2//60 #Calculamos el numero de horas y cogemos solo la parte entera
tm=minutos2%60 #Calculamos el resto dela division, que seran el numero de minutos restantes
print("CALCULO SIN BUCLE WHILE: La catidad es ... \n "+str(th)+" Horas."+" \n "+ str(tm)+" Minutos.")