#!/usr/bin/env bash
# exit on error
set -o errexit

apk add rust cargo
 

pip install -r requirements.txt
 
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@test.com --noinput

