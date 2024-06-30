#!/bin/sh

set -e

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
echo "Waiting for Postegres Database Startup ($POSTGRES_NOT $POSTGRES_PORT)..."
sleep 2
done

echo "Postegres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"
echo "Current user: $(whoami)"
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py runserver 0.0.0.0:8000
