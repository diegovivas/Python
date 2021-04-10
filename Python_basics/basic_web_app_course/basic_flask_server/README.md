-PyPi (python package index) es un repositorio de paquetesde terceros que se pueden utilizar en proyectos de python
-Para instalar un paquet, es necesario utilizar la herramienta pip.
- la forma de instalar un paquete es ejecutando el comando pip install paquete
-Tambien se puede agrupar la instalacion de varios paquetes a la vez con el archivo requirements.txt

Ambientes virtuales

* Es una buena practica crear un ambiente virtualpor cada proyecto de Python en el que trabje.
* Esto evita conflictos de paquetes enel interpete principal.
*pip install virtualenv
*virtualenv venv
*source venv/bin/activate
*desactivate

Instalar virtualenv

-Primero instalar pip
	 linux - sudo apt-get install python-pip "para python2.x"
-Luego; pip install virtualenv

Crear Virtualenv

-ejecutar el comando virtualenv <nombre del entorno>
-para entrar en el entorno virtual: <nombre del entorno>/bin/activate
-para ver los paquetes en el entorno: pip freeze "python2", pip3 freeze "python3"
-para salir del entorno virtual: deactivate