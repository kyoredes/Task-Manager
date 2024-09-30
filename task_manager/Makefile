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
	lsof -i :8000 -t | xargs -P 2 kill

test-users:
	poetry run python manage.py test users .
test-statuses:
	poetry run python manage.py test statuses/tests
test-tasks:
	poetry run python manage.py test tasks/tests
test-labels:
	poetry run python manage.py test labels/tests
test-all:
	poetry run python manage.py test tasks/tests
	poetry run python manage.py test statuses/tests
	poetry run python manage.py test users/tests
