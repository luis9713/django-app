ls -la Mostrar ficheros ocultos
pip listmuestra los paquetes.
pip freezeLista los paquetes que tine el entorno virtual.
Para colocar venv
py -m venv venv se coloca el modulo y el segundo venv es el nombre que se le quiere dar.

django-admin startproject app . instalar la carpeta en el mismo Sitio por el punto.

source venv/script/ activate Se usa el "Source" como comando principal depende de como estas en la terminal y activate .

pip install django instala "django".

rm -rf app/Para borrar elementos

pip freeze > requirements.txt para crear un txt en la carpeta a través de paquetes.

pip install -r requirements.txt actualizacion de los requirements.txt

Activar el DJANGO para entrar.
source venv/script/ activate
py manage.py runserver para correr Django en el puerto //8000.
python manage.py runserver para correr Django en el puerto //8000.
 crtl + c para apagar el Puerto
Staging
git status mira el estado actual
git add . agrega los comabios al estado actual
git commit -m "//comentario" colocar un comentario.
git push subir el add y el comentario.
Visualizar las migraciones
Despues de aplica la base de datos de models.py

$py manage.py migrate convierte una migración en tabla.

$py manage.py showmigrations  Visualizar migraciones.

$py manage.py makemigrations Crear migraciones o crear modelos.

Crear el super usuario con el siguiente comando:
py manage.py createsuperuser Crear el super usuario

pip install psycopg2 para instalar controlador de python.

Cuando se clona el repositorio con:
git pull

pip install -r requirements.txt Recuperar todos los paquetes que se descargaron en el repositorio

Base de Datos settings.py
'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'app',
        "USER": 'postgres',
        'PASSWORD': 'unicesmag',
        'PORT': '5432',
    }
py manage.py migrate para actualizar en postgres la data base
