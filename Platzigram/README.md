##Proyecto Platzigram

clon basico de instagram utilizando python con el framework Django

Algunos conceptos:

	-Request: Un request es un requerimiento, peticion o solicitud que le
		  hace un cliente a un servidor.
		  
	-CGI Script: Tambien llamado Interfaz de entrada comun, es una
	     	     tecnologia que permite solicitardatos a traves de un
		     request a un programa que se esta ejecuntado en un
		     servidor web.
		     
	-Framework: Un Framework (Marco de trabajo) es el esquema o estructura
		    que se establece y qque se aprovecha para desarrollar y
		    organizar un sofware determidado. Es decir es una
		    herramienta que al iniciar un proyecto ya tiene todo lo
		    basico listo para ser aplicado.
		    
	-ORM: Es un modelo deprogramacion que consiste en la trasnformacion
	      de las tablas en una base de datos, en una serie de entidades que
	      simplifiquen el acceso a los datos.
	      
	-Entorno Virtual: es una funcion que permite crear entornos de
		 	  desarrollo con la capacidad de instalar frameworks
			  sin alterar el area de trabajo general.

	-Templates: Archivos HTML que permiten la inclusion y ejecucuion de
		    logica especial para la presentacion de datos.
		    
	-Modelo: Parte de un proyecto de Django que se encarga de estructurar
		 las tablas y propiedades de la base de datos a traves de
		 clases de Python.
		 
	-Vista: Parte de un proyecto de Django que se encarga de la logica
		de negocio y es la conexion entre el ttemplate y el modelo.
		
	-App: Conjunto de codigo que se encarga de resolver una parte muy
	      especifica del proyecto, contiene sus modelos, vistas, urls, etc.
	      
	-Patron de diseño: Solucion comun a un problema particular.


Instalacion de python y un entorno virtual en linux:
## Correr:

	    add-apt-repository -y ppa:jonathonf/python-3.6
	    apt-get update -y	       
	    apt-get install -y python3.6
	    apt-get install -y python3.6-dev
	    apt-get install -y python3.6-distutils
	    ln -s /usr/bin/python3.6 /usr/local/bin/python3
	    wget https://bootstrap.pypa.io/get-pip.py -O /home/ubuntu/get-pip.py
	    python3.6 /home/ubuntu/get-pip.py
	    rm /home/ubuntu/get-pip.py
	    ln -s /usr/local/bin/pip /usr/local/bin/pip3
	    

## Verificación de la descarga

   	1. Correr `python3 --version`
   	2. Correr `pip3 --version`

## Entorno virtual

   	1. Correr `python3 -m venv ENTORNO` donde `ENTORNO` sea el nombre deseado
	2. Correr `source ENTORNO/bin/activate` para activar el entorno
	3. Correr `deactivate` para desactivar el entorno

## Instalación de django

   	1. Activar entorno virtual
	2. Correr `pip install django -U`

----------------------------------------------------------------------
## Documentacion

HttpRequest:

	https://docs.djangoproject.com/en/2.2/topics/http/urls/

-------------------------------------
## Comandos a usar

python3 manage.py runserver

-------------------------------------