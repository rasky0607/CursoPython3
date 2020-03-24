#Identificar si la letra introducida es mayuscula o no es mayuscula
letra=input("Intruce una letra \n")

if(letra>='A' and letra<='Z'): #Esta comparacion es realizada gracias a la tabla ASCI ya que todas las mayusculas estan consecutivas
	print("Es una Mayuscula")
elif(letra>='a' and letra<='z'):
	print("Es una Minuscula")
else:
	print("Es un caracter especial")