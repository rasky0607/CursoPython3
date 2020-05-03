#Instalacion de modulos/librerias externo/as escritos por terceros a nuestro interprete de python3

#Para esto se  utiliza un gestor de paquetes llamado PyPI:
	#El Python Package Index o PyPI, es el repositorio de paquetes de software oficial para aplicaciones de terceros
	# en el lenguaje de programación Python.
	#pip: Sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos
	# en Python que se encuentran alojados en el repositorio PyPI. 


#Repositorio de paquetes o modulos pip: [RECOMENDACION USAR OPCION 3º]
	#Esta es el repositorio para instalar paquetes o modulos en nuestro sistema.
	#Instalacion de dicho repositorios de paquetes o modulos.
	#Encontramos 3 formas alternativas de instalarlo:
		#1º Utilizar los modulos de los paquetes de python que estan ya en nuestra distribucion de Linux.
			#Buscamos el paquete concreto en nuestro sistema Linux con el comando 
			#apt-cache show python3-requests ,en este caso buscamos el paquete requests
			#y si es el que necesitamos, entonces ejecutamos el apt install pyhton3-requests

			#Contras de esta alternativa, la version del modulo que instalamos puede ser muy antigua,
			#ya que dependera del momento que se estabilizao nuestra version del sistema.

		#2º instalamos el sistema de paquetes python3-pip
			#Tras tener pip, usamos este par ainstalar los paquetes externos.
			#pip install requests
			#Este instalara la ultia version de este modulo

			#Contras de esta alternativa: Los paquetes externos instalados si coinciden con los que estan en el sistema operativo
			#pero con versiones más recientes, pueden entrar en conflicto con los modulos más antiguo y/o
			#tener problemas de dependencias incumplidas de paquetes.
			#Esta opcion debe ser usada cuando tengamos un control sobre los paquetes y la version que tenemos y la que instalamos
			#para evitar estos errores y comprobar que funcionan posteriormente correctamente.

		#3º Utilizar un entorno virtual pyhton:
			#Es decir crearemos un directorio aislado donde instalaremos los modulos necesarios para que nuestra aplicacion funcione.

			#Tenemos dos opciones para instalar un entorno virtual:
				#1º instalando virtualenv:[LA MAS RECOMENDADA]
					#sudo apt install python-virtualenv
					
					#Creamos un directorio donde crearemos los entornos virtuales. mkdir misEntornosVirtuales
					#Dentro de este directorio ejecutamos virtualenv indicando
					#la version que queremos utilizar y dandole un nombre
					#La opción -p nos permite indicar el interprete que se va a utilizar en el entorno:
						#virtualenv -p /usr/bin/python3 Mientorno
					#Esto creara el directorio virtual e instalara distintas utilidares entre ellas el instalador pip.

					#Para activar nuestro entorno virtual, al activarlo cambiara el promp del sistema:
					#source Mientorno/bin/activate
					#(Mientorno)$ 
					#Para desactivarlo:
					#(Mientorno)$ deactivate

					#Si necesitamos distribuir o informar de los modulos que estamos utilizando, como cuando trabajamos en equipo.
					#Podemos utilizar el siguiente comando para que todos los miembros del equipo de trabajo conozcan los modulos a usar.
						#Y si queremos guardar esta información en un fichero que podamos distribuir:
							#(Mientorno)$ pip freeze > requirements.txt
						#Esto realizara el volcado dela lista de modulos que estan en el directorio virtual.
						#De tal manera que otro desarrolador, en otro entorno,
						#teniendo este fichero pude reproducirlo e instalar los mismos paquetes de la siguiente manera:
							#(Mientorno)$ pip install -r requirements.txt

				#2º instalando el asistente venv en lugar de virtualenv(Funciona casi totalmente igual).
					#apt-get install python3-venv

					#Creacion del entorno virtual con este asistente:
						#python3 -m venv entorno3
					#La opción -m del interprete nos permite ejecutar un módulo como si fuera un programa.
					
					#Para activar el entono virtual:
						#$ source entorno3/bin/activate
					#Para desactivar el entorno virtual:
						#(entorno3)$ deactivate

			#Pros: Esta es la opcion mas recomendada, ya que es la mas limpia y segura para el correcto funcionamiento de la aplicacion
