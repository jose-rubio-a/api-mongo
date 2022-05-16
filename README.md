Pasos a seguir para desarrollar el proyecto final:
1.- Descargar virtualenv para crear un entorno virtual
2.- Instalar todas las librerías del archivo requirements.txt con el comando pip freeze
3.- Crear la base de datos en la nube con MongoDB Atlas
4.- Elaboración del dockerfile
5.- Con el docker file creado, correr el comando docker build -t <nombre_imagen> para crear la imagen
6.- Subir la imagen a nuestro docker hub
7.- Utilizar docker-compose para ligar los servicios de nuestro sistema

Ahora para utilizar Kubernetes:
1.- Convertir los archivos del programa a kubernetes
2.- Añadir pods con el siguiente código: kubectl apply -f <nombre_archivo>
3.- Comprobar en dashboard y realizar pruebas

Por último para utilizar OpenShift:
1.- Para esta herramienta se deben subir los archivos a un repositorio de Git Hub
2.- Entrar a la página principal desarrollador de OpenShift y seleccionar la opción "Add"
3.- Seleccionar la opción "Import from git"
4.- Indicar el repositorio donde se encuentran los archivos del programa y configurar
5.- Despliegue de la aplicación y pruebas
