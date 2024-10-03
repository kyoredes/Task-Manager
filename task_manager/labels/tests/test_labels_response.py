from django.test import TestCase
from django.urls import reverse
from task_manager.labels.models import Label


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
        self.client.post(
            reverse('create_label'), name='title'
        )

    def test_labels_show_view(self):
        response = self.client.get('/labels/')
        self.assertEqual(response.status_code, 200)

    def test_labels_create_view(self):
        response = self.client.get('/labels/create/')
        self.assertEqual(response.status_code, 200)

    def test_labels_update_view(self):
        Label.objects.create(name='title')
        id = Label.objects.all().get(name='title').id
        response = self.client.get(f'/labels/{id}/update/')
        self.assertEqual(response.status_code, 200)

    def test_labels_delete_view(self):
        Label.objects.create(name='title')
        id = Label.objects.all().get(name='title').id
        response = self.client.get(f'/labels/{id}/delete/')
        self.assertEquals(response.status_code, 200)
