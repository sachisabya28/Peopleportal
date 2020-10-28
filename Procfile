web: gunicorn run:app
release: python manage.py db migrate
release: python manage.py db upgrade
release: python release_script.py
