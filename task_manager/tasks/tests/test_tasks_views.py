from django.test import TestCase
from django.urls import reverse
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model


class TestTaskResponseCase(TestCase):
    def setUp(self):
        users_data = {
            'username': 'kaito',
            'first_name': 'kaito',
            'last_name': 'kaito',
            'password1': '6754556876a',
            'password2': '6754556876a',
        }
        self.client.post(
            reverse('create_user'), users_data
        )
        self.client.post(
            reverse('login'), {'username': 'kaito', 'password': '6754556876a'}
        )

    def test_tasks_show_view(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)

    def test_tasks_create_view(self):
        response = self.client.get('/tasks/create/')
        self.assertEqual(response.status_code, 200)

    def test_tasks_update_view(self):
        status = Status.objects.create(title='title')
        user = get_user_model().objects.all().get(username='kaito')
        label = Label.objects.create(name='name')
        response = self.client.post(reverse('create_task'), {
            'title': 'title',
            'description': 'sjhfkshk',
            'status': status.id,
            'executor': user.id,
            'label': label.id,
            })
        id = Task.objects.all().get(title='title').id
        response = self.client.get(f'/tasks/{id}/update/')
        self.assertEqual(response.status_code, 200)

    def test_tasks_delete_view(self):
        status = Status.objects.create(title='title')
        user = get_user_model().objects.all().get(username='kaito')
        label = Label.objects.create(name='name')
        response = self.client.post(reverse('create_task'), {
            'title': 'title',
            'description': 'sjhfkshk',
            'status': status.id,
            'executor': user.id,
            'label': label.id
            })
        id = Task.objects.all().get(title='title').id
        response = self.client.post(f'/tasks/{id}/delete/')
        self.assertEqual(response.status_code, 302)
