start:
	poetry run python manage.py runserver
install:
	poetry install
migrate:
	poetry run python task_manager/manage.py makemigrations
	poetry run python task_manager/manage.py migrate
lint:
	poetry run flake8
check:
	poetry check
build:
	poetry build
test:
	cd task_manager/ && poetry run coverage run manage.py test
test-coverage:
	cd task_manager/ && poetry run coverage run manage.py test
	poetry run coverage report
shell:
	poetry run python task_manager/manage.py shell
test-users:
	poetry run python task_manager/manage.py test task_manager/users/tests
test-statuses:
	poetry run python task_manager/manage.py test task_manager/statuses/tests
test-tasks:
	poetry run python task_manager/manage.py test task_manager/tasks/tests
test-labels:
	poetry run python task_manager/manage.py test task_manager/labels/tests
