#Introduciremos una cadena por teclado, y cambiaremos los digitos por un caracter tambien introducido por teclado

cadena=input("Introduce una cadena: ")
caracter=input("introduce un caracter: ")
result=""
for i in cadena:
	if(i.isdigit()):#Si esun digito el elemento de la cacena, guardamos el caracter, si no el elemento de la cadena
		result+=caracter
	else:
		result+=i
else:
	print("Resultado-> "+ result)