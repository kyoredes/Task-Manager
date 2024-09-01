start:
	poetry run python manage.py runserver
s:
	poetry run python manage.py runserver
migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
lint:
	poetry run flake8
m:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
sh:
	poetry run python manage.py shell
kill:
	lsof -i :8000 -t | parallel kill