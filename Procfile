release: python manage.py migrate
release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json'
release: sh -c 'python manage.py migrate && python manage.py loaddata pandorabox.json'
web: gunicorn project_django.wsgi --log-file -