from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status


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
        self.client.post(reverse('login'), {
            'username': 'kaito',
            'password': '6754556876a',
        })
        statuses_data = {
            'title': 'complete'
        }
        self.client.post(
            reverse('create_status'), statuses_data
        )

    def get_id(self, title):
        user = Status.objects.all().get(title=title)
        return user.id

    def test_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'kaito',
            'password': '6754556876a',
        })
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        if response.wsgi_request.user.is_authenticated:
            print('user is logged in')

    def test_statuses_show_view(self):
        response = self.client.get('/statuses/')
        self.assertEqual(response.status_code, 200)

    def test_statuses_create_view(self):
        response = self.client.get('/statuses/create/')
        self.assertEqual(response.status_code, 200)

    def test_statuses_update_view(self):
        id = self.get_id(title='complete')
        response = self.client.get(f'/statuses/{id}/update/')
        self.assertEqual(response.status_code, 200)

    def test_statuses_delete_view(self):
        id = self.get_id(title='complete')
        response = self.client.post(f'/statuses/{id}/delete/')
        self.assertEqual(response.status_code, 302)
