### Hexlet tests and linter status:
[![Actions Status](https://github.com/ddertaliss/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ddertaliss/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/c9037aafe807e2de9f87/maintainability)](https://codeclimate.com/github/ddertaliss/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c9037aafe807e2de9f87/test_coverage)](https://codeclimate.com/github/ddertaliss/python-project-52/test_coverage)

[![built with](https://skillicons.dev/icons?i=py,django)](https://skillicons.dev)

<h1>Task Manager</h1>
<p>Task Manager is a task management system similar to http://www.redmine.org/. It allows users to create tasks, assign them to team members, and update their statuses. Registration and authentication are required to use the system.</p>
 
  <ul>
    <li>Create tasks</li>
    <li>Add statuses</li>
    <li>Add labels</li>
    <li>Create your account</li>
    <li>Set task performers</li>
  </ul>

<h1>Built with</h1>
  
  <ul>
    <li>Poetry</li>
    <li>Django</li>
    <li>Bootstrap 5</li>
    <li>Django-crispy-forms</li>
    <li>Django-filters</li>
    <li>Rollbar</li>
    <li>Flake8</li>
    <li>Django authentication</li>
  </ul>

<h1>Installation</h1>

```bash
git clone https://github.com/ddertaliss/python-project-52 && cd python-project-52
poetry install
make start
```

<h1>Tests</h1>

```bash
make test-all
```

```bash
make test-users
make test-labels
make test-statuses
make test-tasks
```

<h1>All Makefile commands</h1>
<ul>
  <li>make start</li>
  <li>make migrate</li>
  <li>make sh</li>
</ul>
