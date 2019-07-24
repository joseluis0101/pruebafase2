# pruebafase2
Prueba fase 2 bosques y arboles
# Comandos para ejecutar el proyecto
para instalar las dependencias ejecutamos el siguiente comando dentro del proyecto
´´´
pip install -r requirements.txt
´´´
para sincronizar la base de datos ejecutamos los siguientes comandos
´´´
python manage.py makemigrations
python manage.py migrate
´´´
para iniciar el servidor ejecutamos el siguiente comando

´´´
python manage.py runserver 
´´´

El proyecto ya incluye un dockerfile y un docker-compose si lo que se desea es montarlo en docker
o se puede descargar la imagen de docker hub 


´´´
docker pull joseluis01011990/prueba2_web

´´´
si deseas probar el servicio desde postman sin montarlo puedes hacerlo desde esta url 
https://pruebafase2.herokuapp.com/api/bosques/

