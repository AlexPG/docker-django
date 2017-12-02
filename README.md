# docker-django
An example of deploying a django app with docker compose.

# Requirements
Docker
Docker Compose

# Installation
Download or clone the repo in your target directory. 

Then move to the folder containing the docker-compose.yml file.

First we will run
```python
docker-compose build
```
to build our web service. This web service is built with a Dockerfile inside docker_django directory .

After that we will do
```python
docker-compose up -d
```
to start our services in detached mode.

Finally we have to do some Django management.
```python
docker-compose run web /usr/local/bin/python manage.py makemigrations
```
to check for new migrations.
```python
docker-compose run web /usr/local/bin/python manage.py migrate
```
for applying  migrations.
```python
docker-compose run web /usr/local/bin/python manage.py collectstatic
```
to collect the static files into STATIC_ROOT.
```python
docker-compose run web /usr/local/bin/python manage.py createsuperuser
```
This is only necesary if we want to use the django admin site.

# Usage
Now you can navigate to [localhost:8001](http://localhost:8001) or [127.0.0.1:8001](http://127.0.0.1:8001). 
We can also navigate to [localhost:8001/admin](http://localhost:8001/admin) or [127.0.0.1:8001/admin](http://127.0.0.1:8001/admin).