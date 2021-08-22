#!/bin/sh

python /code/aukse/manage.py makemigrations
python /code/aukse/manage.py migrate
python /code/aukse/manage.py runserver 0.0.0.0:8000
