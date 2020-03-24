#Obtener ayuda usando la funcion help() en la consola de python
# o para optener ayuda concreta help(print) o la funcion de la cual deseamos info.

#Funciones predefinidas de Python3:
#abs()           dict()         help()          min()        setattr()
#all()           dir()          hex()           next()       slice()
#any()           divmod()       id()            object()     sorted()
#ascii()         enumerate()    input()         oct()        staticmethod()
#bin()           eval()         int()           open()       str()
#bool()          exec()         isinstance()    ord()        sum()
#bytearray()     filter()       issubclass()    pow()        super()
#bytes()         float()        iter()          print()      tuple()
#callable()      format()       len()           property()   type()
#chr()           frozenset()    list()          range()      vars()
#classmethod()   getattr()      locals()        repr()       zip()
#compile()       globals()      map()           reversed()   __import__()
#complex()       hasattr()      max()           round()      
#delattr()       hash()         memoryview()    set()   
#Ejemplo de funciones:
# eval() --> evalua cadena de caracteres como : 
#x=1
#eva("x+1")

#Algunos ejemplos :
#La entrada y salida de información se hacen con la función print y la función input:
#Tenemos algunas funciones matemáticas como: abs, divmod, hex, max, min,…
#Hay funciones que trabajan con caracteres y cadenas: ascii, chr, format, repr,…
#Además tenemos funciones que crean o convierten a determinados tipos de datos: int, float, str, bool, range, dict, list, …

#CONSTANTES predefinidas:
#True y False: Valores booleans
#None especifica que alguna variables u objeto no tiene asignado ningún tipo.

#OPERADORES 
# la potencia se usa **
# Operadores unarios virdulilla + -
# multiplicar,dividir,modulo, division entera *  /  %  // (La division entera o //  lo que hace es devolver solo el resultado entero)
#desplazamiento de bit >> <<
#operador binario and &
#operador binario OR y XOR | ^
#operadores de comparacion <= <  >  >=
#operadores de igualdad <> == !=
#operadores de asignacion = %=  -=  += //= *= **=
#operadores de pertenencia in is not
#operadores logicos not or and
#operador de identidad is  o   is not nos idica si una varaible esta referenciando al mismo valor que otra
	#Ya que a diferencia de otros lenguajes en Python guardar en la variable 'a=5' lo que hacemos en realidad es:
	#referenciar la varaible a la posicion de meoria de 5, es decir es como si 5 fuera otra variable y se coloca un puntero hacia este
	#por lo que por Ejemplo: si preguntamos ' if a is 5: '  esto devolvera true , pero si  luego hacemos 'a=7' ya devolvera false
	#de el mismo modo podemos hacer la pregunta de forma negativa usando is not