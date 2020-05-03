#Modulo utilizado para el manejo de fechas y horas.

#Modulo time:
	import time
	#time-> nos permite el manejo de fechas desde el 1 de enero de 1970 hasta el 2038 debido a un tipo de valor double que usa de C.
	#Este problema se ha solucionado ya con otras librerias alternativas
	#podemos usar el valor devuelto por la funcion  Time.time() para convertir esa cantidad de segundos transcurridos desde 1970 hasta ahora
	#en algo mas legible usando:
	#Time.localTime(Time.time)
	#Y recibimos una estructura donde encontraremos el año, el mes, el dia ,la hora, minuto , segundo , etc...
	print(time.localtime(time.time()))
	#Tambien podemos representarlo en un formato cadena con:
	#time.asctime()
	print(time.asctime())

	#Con el uso de comodines tambien podemos indicar un formato determinado
	#fecha1.strftime("%d/%m/%Y")
	#'04/03/2017'
	#hora1.strftime("%H:%M:%S")
	#'10:05:00'

	#Comparacion de fechas:
	#from datetime import datetime, date, time, timedelta
	# hora1 = time(10,5,0)
	# hora2 = time(23,15,0)
	# hora1>hora2
	#False

	# fecha1=date.today()
	# fecha2=fecha1+timedelta(days=2)
	# fecha1
	#datetime.date(2017, 3, 4)
	# fecha2
	#datetime.date(2017, 3, 6)
	# fecha1<fecha2
	#True

#Modulo datetime
#Este es una mejora del modulo anterior
	#En el podemos encontrar funciones como datetime.now() que nos devuelve un objeto datetime con la fecha y hora actual
	#Por ejemplo para obtener el mes el dia y el año
	#datetime.now().day, datetime.now().month, datetime.now().year
	#(Resultado -> (4, 3, 2017)

	#Comparacion de fechas con este modulo:
		#hoy = date.today()
		#ayer = hoy - timedelta(days=1)
		#diferencia=hoy -ayer
		#diferencia
		#datetime.timedelta(1)

		#fecha1=datetime.now()
		#fecha2=datetime(1995,10,12,12,23,33)
		#diferencia=fecha1-fecha2
		#diferencia
		#datetime.timedelta(7813, 81981, 33319

#Modulo candelar que nos permite trabajar con calendarios, como el calendario del mes actual.

	#import calendar
	#Mostrar el calendario del mes actual:

	#año = date.today().year 
	#mes = date.today().month
	#calendario_mes = calendar.month(año, mes)
	#print(calendario_mes)
	#Resultado:
	#     March 2017
	#Mo Tu We Th Fr Sa Su
	#       1  2  3  4  5
	# 6  7  8  9 10 11 12
	#13 14 15 16 17 18 19
	#20 21 22 23 24 25 26
	#27 28 29 30 31

	#Y para mostrar todos los meses del año:
		#print(calendar.TextCalendar(calendar.MONDAY).formatyear(2017,2, 1, 1, 2))

