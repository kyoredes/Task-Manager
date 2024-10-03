from django.test import TestCase
from django.urls import reverse
from task_manager.labels.models import Label


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

    def test_create_label(self):
        self.client.post(
            reverse('create_label'), {'name': 'title'}
        )
        exists = Label.objects.all().filter(name='title').exists()
        self.assertTrue(exists)

    def test_update_status(self):
        self.client.post(
            reverse('create_label'), {'name': 'title'}
        )
        id = Label.objects.all().get(name='title').id
        self.client.post(
            reverse('update_label', kwargs={'pk': id}), {'name': 'titlee'}
        )
        exists = Label.objects.all().filter(name='titlee').exists()
        self.assertTrue(exists)

    def test_delete_status(self):
        self.client.post(
            reverse('create_label'), {'name': 'title'}
        )
        id = Label.objects.all().get(name='title').id
        self.client.post(
            reverse('delete_label', kwargs={'pk': id})
        )
        res = Label.objects.all().filter(id=id)
        self.assertEqual(len(res), 0)
