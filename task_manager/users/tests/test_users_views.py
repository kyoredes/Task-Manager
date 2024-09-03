from django.test import TestCase

# Create your tests here.
class TestResponseCase(TestCase):
    def test_users_show_view(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_users_create_view(self):
        response = self.client.get('/create_user/')
        self.assertEqual(response.status_code, 200)

    def test_users_create_view(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    def test_users_create_view(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)