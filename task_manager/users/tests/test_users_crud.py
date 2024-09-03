from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user


class TestUsersCase(TestCase):
    def test_user_registration(self):
        model = get_user_model()
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
        user_exists = model.objects.filter(username='kaito').exists()
        self.assertTrue(user_exists)
    
    def test_login(self):
        self.assertFalse(get_user(self.client).is_authenticated)
        self.client.login(username='kaito', password='6754556876a')
        self.assertTrue(get_user(self.client).is_authenticated)
    
    # def test_user_update(self):
    #     user_model = get_user_model()
        