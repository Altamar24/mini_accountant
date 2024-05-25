from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationViewTest(TestCase):

    """Проверка регистрации пользователя"""

    def test_registration_user(self):
        self.author = User.objects.create_user(username='altamar',
                                               email='maga99911@mail.ru',
                                               password='altamar')

        response = self.client.get(
            reverse('registration'))
        self.assertEqual(response.status_code, 200)
