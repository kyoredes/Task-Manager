from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
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
        self.client.post(
            reverse('create_user'), users_data
        )
        self.client.post(
            reverse('login'), {'username': 'kaito', 'password': '6754556876a'}
        )

    def test_filter(self):
        status = Status.objects.create(name='title')
        label = Label.objects.create(name='name')
        user = get_user_model().objects.all().get(username='kaito')
        self.client.post(
            reverse('create_task'),
            {
                'name': 'title',
                'description': 'sjhfkshk',
                'status': status.id,
                'executor': user.id
            }
        )
        # status filter
        response = self.client.get(
            f'/tasks/?status={status.id}&executor=&label='
        )
        self.assertEqual(response.status_code, 200)
        # executor filter
        response = self.client.get(
            f'/tasks/?status=&executor={user.id}&label='
        )
        self.assertEqual(response.status_code, 200)
        # label filter
        response = self.client.get(
            f'/tasks/?status=&executor=&label={label.id}'
        )
        self.assertEqual(response.status_code, 200)
