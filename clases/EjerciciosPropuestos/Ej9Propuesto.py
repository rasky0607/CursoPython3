#Ejercicios 9 propuesto Logeo d eun usuario, se pide usuario y contraseña, si es correcta se indica que entro en el sistema, si no un error
usuario='pablo'
passwrod='1234'
user=input("Intruce el usuario: \n")
passw=input("Intruce la contraseña: \n")

if(usuario == user and passwrod == passw):
	print("Login correcto.\n ## ENTRO EN EL SISTEMA ##")
else:
	print("ERROR: el usuario o contraseña son incorrectos ...")