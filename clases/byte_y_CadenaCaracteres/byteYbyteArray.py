#Tipos de datos Byte y ByteArray
#El tipo Byte es INMUTABLE
#El tipo ByteArray es MUTABLE
#Estos pueden representar caracteres ASSCI o como numero del 0 al 255
#Forma de definir un Byte[INMUTABLE]:
	#Ej1: mibyte=b"hola"
	#Ej2:Usando el constructor mibyte = bytes(10) estamos creando un cadena de 10 caracteres de byte vacios
	#Ej3:Usando el constructor para crear cadena hexadecimal byte3=bytes.fromhex('2Ef0 F1f2')
	#IMPORTANTE: podemos indicar la codificacion en el constructor de byte para cuando manejamos
		#caracteres especiales como la 'ñ'
			#Ej4: byte1=bytes('piña',"latin1") o byte1=bytes('piña',"utf-8")
		#Tambien podemos convertir una cadena/string normal a byte usando :
			#Ej:cadena1="piña" byte1=cadena1.encode("utf-8")
		#Y realizzar el proceso inverso convertir de byte a cadena/String:
		#(Importante conocer la codificacion del byte para esto)
			#Ej: cadena2=byte1.decode("utf-8")

		#Cuando no conocemos la codificacion del Byte para poder realizar el decode():
		#Tenemos dos opciones entre otras... :
			#byte1=bytes('piña',"latin1")
			#Para que ignore los caracteres que no puede convertir a cadena de utf-8 por ejemplo
			#1-Usar: byte1.decode("utf-8","ignore") ->Resultado-> 'pia'
			#Para reemplazar los caracteres que no se pueden convirtir por un caracter comodin
			#2-Usar: byte1.decode("utf-8","replace")->Resultado-> 'pi�a'
			
#Forma de definir un ByteArray [MUTABLE]:
	#Ej1: ba4=bytearray(b"hola") crearemos una coleccion de byte que contienen la colecion de caracteres "hola"
	#Ej2:ba2=bytearray(10) habremos creado una coleccion de byte de 10 posciones vacio de caracteres
	#Ej3:ba5=bytearray.fromhex('2Ef0 F1f2')crearemos una colecion de bytearray con cadenas hexadecimales
	#A diferencia de los tipo Byte, lo ByteArray si son MUTABLES
		#Por lo que podemos modificarlo por posicion:
			#Ej: ba4=bytearray(b"hola") 
				#ba4[2]=90  resultado -> ba4="hoZa" Habremos cambiado la 'l' por el caracter ascci 90-> 'Z'mayuscula 

#Metodos de la clase Byte:
	#byte1.capitalize  byte1.index       byte1.join        byte1.rindex      byte1.strip
	#byte1.center      byte1.isalnum     byte1.ljust       byte1.rjust       byte1.swapcase
	#byte1.count       byte1.isalpha     byte1.lower       byte1.rpartition  byte1.title
	#byte1.decode      byte1.isdigit     byte1.lstrip      byte1.rsplit      byte1.translate
	#byte1.endswith    byte1.islower     byte1.maketrans   byte1.rstrip      byte1.upper
	#byte1.expandtabs  byte1.isspace     byte1.partition   byte1.split       byte1.zfill
	#byte1.find        byte1.istitle     byte1.replace     byte1.splitlines  
	#byte1.fromhex     byte1.isupper     byte1.rfind       byte1.startswith  

#Metodos de la clase ByteArray:
	#bytearray1.append      bytearray1.index       bytearray1.lstrip      bytearray1.rstrip
	#bytearray1.capitalize  bytearray1.insert      bytearray1.maketrans   bytearray1.split
	#bytearray1.center      bytearray1.isalnum     bytearray1.partition   bytearray1.splitlines
	#bytearray1.clear       bytearray1.isalpha     bytearray1.pop         bytearray1.startswith
	#bytearray1.copy        bytearray1.isdigit     bytearray1.remove      bytearray1.strip
	#bytearray1.count       bytearray1.islower     bytearray1.replace     bytearray1.swapcase
	#bytearray1.decode      bytearray1.isspace     bytearray1.reverse     bytearray1.title
	#bytearray1.endswith    bytearray1.istitle     bytearray1.rfind       bytearray1.translate
	#bytearray1.expandtabs  bytearray1.isupper     bytearray1.rindex      bytearray1.upper
	#bytearray1.extend      bytearray1.join        bytearray1.rjust       bytearray1.zfill
	#bytearray1.find        bytearray1.ljust       bytearray1.rpartition  
	#bytearray1.fromhex     bytearray1.lower       bytearray1.rsplit 