from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):

    """Проверка url регистрации пользователя"""

    def test_registration_url(self):
        url = reverse('registration')
        self.assertEqual(url, '/accounts/registration/')
