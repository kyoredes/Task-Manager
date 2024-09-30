start:
	poetry run python manage.py runserver
install:
	poetry install
migrate:
	poetry run python task_manager/manage.py makemigrations
	poetry run python task_manager/manage.py migrate
lint:
	poetry run flake8
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
test-all:
	poetry run python task_manager/manage.py test task_manager/tasks/tests
	poetry run python task_manager/manage.py test task_manager/statuses/tests
	poetry run python task_manager/manage.py test task_manager/users/tests
	poetry run python task_manager/manage.py test task_manager/labels/tests
