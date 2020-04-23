#Programa que lee por  teclado una cadena y un caracter, e inserte el caracter entre cada letra de la cadena
cadena=input("introduce una cadena: ")
caracter=input("Introduce un caracter")

cadena=cadena.strip()#Eliminamos posibles espacios de la cadena
print(caracter.join(cadena))#Introducimos el caracter depues de cada uno de los elementos de la cadena
