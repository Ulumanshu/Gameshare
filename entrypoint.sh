#!/bin/sh

python /code/gameshare/manage.py makemigrations
python /code/gameshare/manage.py makemigrations games

python /code/gameshare/manage.py migrate
python /code/gameshare/manage.py runserver 0.0.0.0:8000
