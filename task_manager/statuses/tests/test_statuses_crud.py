from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status


class TestStatusesCase(TestCase):
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
            reverse('login'), {
                'username': 'kaito',
                'password': '6754556876a',
            }
        )

    def get_id(self, title):
        user = Status.objects.all().get(name==title)
        return user.id

    def test_create_status(self):
        self.client.post(
            reverse('create_status'), {'name': 'name'}
        )
        status_exists = Status.objects.filter(name='name').exists()
        self.assertTrue(status_exists)

    def test_update_status(self):
        self.client.post(
            reverse('create_status'), {'name': 'name'}
        )
        id = self.get_id('name')
        self.client.post(
            reverse('update_status', kwargs={'pk': id}), {'name': 'new_name'}
        )
        status_exists = Status.objects.all().filter(name='new_name').exists()
        self.assertTrue(status_exists)

    def test_delete_status(self):
        self.client.post(
            reverse('create_status'), {'name': 'name'}
        )
        id = self.get_id('name')
        self.client.post(
            reverse('delete_status', kwargs={'pk': id})
        )
        status_exists = Status.objects.all().filter(name='name').exists()
        self.assertFalse(status_exists)
