#Crear una funcion que devuelva la cantidad de segundos en un tiempo dado en horas, minutos y segundos.

param=input("Indica un numero de horas minutos y/o segundos separados por ',' superior o igual a 0 [Ej:1,40,10]:\n ")
if(len(param)!=0):
	listparam= param.split(",")

def sumar(arguments):

	h=0
	m=0
	s=0
	h=int(arguments[0])
	m=int(arguments[1])
	s=int(arguments[2])
	print("Esto es los args-> h:"+str(h)+" m:"+str(m)+" s:"+str(s))

	while h>=1:
		h-=1#Restamos 1 h
		m+=60# sumamos un minuto
	else:
		m+=h#Sumamos los minutos restante que quedan de las horas


	while m>=1:
		m-=1
		s+=60
	
	print("Segundos totales -> "+str(s))

try:
	if(len(listparam)>=0 and len(listparam)<=3):
		sumar(listparam)
	else:
		print("Solo pueden ser indicado 3 parametros")
except:
	print("Los parametros indicados no son correctos")