from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

User = get_user_model()

class TestUrls(TestCase):

    """Проверка url регистрации пользователя"""

    def test_registration_url(self):
        url = reverse('registration')
        self.assertEqual(url, '/accounts/registration/')

    """Проверка перенаправления на url login после успешного создания пользователя"""
    
    def test_redirect(self):
        data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        response = self.client.post(reverse('registration'), data, follow=True)
        self.assertEqual(User.objects.count(), 1)
        self.assertRedirects(response, '/accounts/login/')

