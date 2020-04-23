#Escribir una cadena por teclado y que diga si estas es o no un palindromo
cadena=input("escribe una cadena: ")
if(cadena.lower() == cadena[::-1].lower()):# es la lista de carcteres de la cadena en orden inverso
	print("La cadena es un palindromo!")
else:
	print("La cadena NO es un palindromo!")