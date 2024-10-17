dev:
	poetry run python manage.py runserver
start:
	poetry run gunicorn --bind 0.0.0.0:8000 task_manager.wsgi
install:
	poetry install
migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
lint:
	poetry run flake8
check:
	poetry check
build:
	poetry build
test:
	poetry run coverage run manage.py test
test-coverage:
	poetry run coverage run --source='.' manage.py test && poetry run coverage xml
shell:
	poetry run python manage.py shell
test-users:
	poetry run python manage.py test task_manager/users/tests
test-statuses:
	poetry run python manage.py test task_manager/statuses/tests
test-tasks:
	poetry run python manage.py test task_manager/tasks/tests
test-labels:
	poetry run python manage.py test task_manager/labels/tests
locale:
	poetry run django-admin compilemessages