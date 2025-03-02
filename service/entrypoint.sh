#!/bin/sh
until pg_isready -h database -U "${DB_USER}"; do
  echo "Waiting for database..."
  sleep 2
done
echo "Applying migrations..."
python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear
exec "$@"