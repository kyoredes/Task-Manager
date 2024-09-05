from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user


class TestUsersCase(TestCase):
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
    
    def test_user_registration(self):
        model = get_user_model()
        user_exists = model.objects.filter(username='kaito').exists()
        self.assertTrue(user_exists)
    
    def test_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'kaito',
            'password': '6754556876a',
        })
        self.assertTrue(response.wsgi_request.user.is_authenticated)
    
    # def test_user_update(self):
    #     user_model = get_user_model()
        