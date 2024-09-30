from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestResponseCase(TestCase):
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

    def get_id(self, username):
        user = get_user_model().objects.all().get(username=username)
        return user.id

    def test_users_show_view(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_users_create_view(self):
        response = self.client.get('/users/create/')
        self.assertEqual(response.status_code, 200)

    def test_users_update_view(self):
        id = self.get_id(username='kaito')
        response = self.client.get(f'/users/{id}/update/')
        self.assertEqual(response.status_code, 302)

    def test_users_delete_view(self):
        id = self.get_id(username='kaito')
        response = self.client.get(f'/users/{id}/delete/')
        self.assertEqual(response.status_code, 302)

    def test_users_login_view(self):
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

    def test_users_logout_view(self):
        self.client.post(
            reverse('login'), {'username': 'kaito', 'password': '6754556876a'}
        )
        response = self.client.post(
            reverse('logout')
        )
        self.assertEqual(response.status_code, 302)
