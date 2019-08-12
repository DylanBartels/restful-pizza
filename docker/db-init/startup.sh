#!/bin/bash

python manage.py makemigrations pizza_ordering_service --no-input
python3 manage.py migrate --no-input
