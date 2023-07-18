#!/bin/sh
python manage.py migrate
python manage.py collectstatic --clear --noinput

gunicorn -b :8000 --access-logfile - --error-logfile - conf.wsgi #--workers=4