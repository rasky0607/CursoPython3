#Recogemos dos numeros por teclado e indicamos si la suma de estos dos da como resultado un valor negativo, positivo o 0
num1=float(input("Indicame el primer numero. "))
num2=float(input("INdicame el segundo numero."))
result= None
result=num1+num2;

if(result>0):
	print(str(num1)+"+"+str(num2)+"->El resultado es ##positivo##.")
elif(result<0):
	print(str(num1)+"+"+str(num2)+"->El resultado es ##negativo##.")
else:
	print(str(num1)+"+"+str(num2)+"->El resultado es ##0##.")
