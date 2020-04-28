#Ester ejercicio convertira uan cadena escrita en codigo morse y viceversa segun las claves de un diccionario:

#Diccionario de codigo morse
dicmorse = {
    'A': '.-',     'B': '-...',    'C': '-.-.',
    'D': '-..',    'E': '.',       'F': '..-.',
    'G': '--.',    'H': '....',    'I': '..',
    'J': '.---',   'K': '-.-',     'L': '.-..',
    'M': '--',     'N': '-.',      'O': '---',
    'P': '.--.',   'Q': '--.-',    'R': '.-.',
    'S': '...',    'T': '-',       'U': '..-',
    'V': '...-',   'W': '.--',     'X': '-..-',
    'Y': '-.--',   'Z': '--..',    '1': '.----',
    '2': '..---',  '3': '...--',   '4': '....-',
    '5': '.....',  '6': '-....',   '7': '--...',
    '8': '---..',  '9': '----.',   '0': '-----',
    '.': '.-.-.-', ',': '--..--',  ':': '---...',
    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
    '-': '-....-', '/': '-..-.',   '=': '-...-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
    '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
}

cadena=input("Transformare la cadena introducida a morse: ")
resultMorse=[]#Para luego recovertir el resultado morse en letras de nuevo
print("Resultado: ")
for letra in cadena:
	resultMorse.append(dicmorse.get(letra.upper()))
	print(dicmorse.get(letra.upper())+" ",end=" ")

print()

print("Resultado morse -> "+str(resultMorse))

#Ahora la inversa buscamos la clave segun el valor que tenemos
for j in resultMorse:
	for k in dicmorse:
		valor=dicmorse.get(k)
		#print("valor "+k+" -> ["+valor+"] j-> ["+j+"]")
		if(valor==j):#Si el valor de el indice que estamos recorriendo coincide con el valor de la lista del resultado morse, es la clave que estamos buscando en el diccionario
			#print("SIIII")
			print(k,end="")

else:
	print()
