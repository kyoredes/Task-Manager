from django.test import TestCase
from django.urls import reverse
from tasks.models import Task
from statuses.models import Status
from django.contrib.auth import get_user_model


class TestTaskCase(TestCase):
    def setUp(self):
        users_data = {
            'username': 'kaito',
            'first_name': 'kaito',
            'last_name': 'kaito',
            'password1': '6754556876a',
            'password2': '6754556876a',
        }
        response =  self.client.post(
            reverse('create_user'), users_data
        )
        self.client.post(
            reverse('login'), {'username': 'kaito', 'password': '6754556876a'}
        )
    
    def test_task_create(self):
        status = Status.objects.create(title='title')
        user = get_user_model().objects.all().get(username='kaito')
        response = self.client.post(reverse('create_task'), {'title': 'title', 'description': 'sjhfkshk', 'status': status.id, 'executor': user.id})
        task = Task.objects.all().filter(title='title').exists()        
        self.assertTrue(task)
    
    def test_task_update(self):
        status = Status.objects.create(title='title')
        user = get_user_model().objects.all().get(username='kaito')
        res = self.client.post('/tasks/create/', {'title': 'title', 'description': 'sjhfkshk', 'status': status.id, 'executor': user.id})
        id = Task.objects.all().get(title='title').id
        self.client.post(f'/tasks/{id}/update/', {'title': 'new_title', 'description': 'dsfsdf', 'status': status.id, 'executor': user.id})
        task = Task.objects.all().filter(title='new_title').exists()
        self.assertTrue(task)

    def test_task_delete(self):
        status = Status.objects.create(title='title')
        user = get_user_model().objects.all().get(username='kaito')
        res = self.client.post('/tasks/create/', {'title': 'title', 'description': 'sjhfkshk', 'status': status.id, 'executor': user.id})
        id = Task.objects.all().get(title='title').id
        self.client.post(f'/tasks/{id}/delete/')
        task = Task.objects.all().filter(title='title').exists()
        self.assertFalse(task)
        