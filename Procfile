
release: python manage.py migrate --no-input

web: bin/start-pgbouncer-stunnel gunicorn timelord.wsgi --log-file -