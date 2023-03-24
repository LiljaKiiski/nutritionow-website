#!/bin/sh
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py migrate
chmod 755 staticfiles/models/dalai/alpaca/main
python3 manage.py runserver