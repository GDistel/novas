#!/bin/sh
if [ "$DATABASE" = "postgres" ]
then
    echo "PostgreSQL started"
    python manage.py flush --no-input
fi

python manage.py migrate
python manage.py collectstatic --no-input --clear

exec "$@"