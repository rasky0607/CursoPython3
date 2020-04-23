#Lee una cadena de caracteres y muestre la siguiente informacion:
#1. que muestre la primera letra de cada palabra
#2.Dicha cadena con la letra de cada palabra en mayuscula
#3.Las palabras que comienzan con la letra "a"
cadena=input("Introduce una frase: ")
#Este forma parte del apartado 3. para recoger las palabras que empiezan con A o a
palabrasA=[]#Lista vacia que contien palabras que empiezan por A

#Muestra la primera letra de cada palabra
print("#Primera letra de cada palabra:")
filtrado=cadena.split(" ")
contador=0

for i in filtrado:#Leemos todos los elementos de la lista
	for j in i:#Leemos la palabra caracter a caracter
		contador+=1
		if(contador==1):#Solo la primera letra de cada palabra
			print(j)		
	if(i.startswith("a") cor i.startswith("A")):#Este forma parte del apartado 3. para recoger las palabras que empiezan con A o a
		palabrasA.append(i)#Añadimos la palabra que empiza por A a la lista			
	contador=0
else:
	print("--------")

#Muestra la priemra letra de cada palabra en mayuscula ,es decir camelcase
print("#Primera letra de cada palabra en mayuscula: \n"+cadena.title())
print("--------")

#Palabras que empiezan con A o a
print("#Palabras que empiezan con A o a")
print(palabrasA)
print("---FIN---")
