from django.test import TestCase

from accounts.models import User


class UserModelTest(TestCase):

    """Проверка модели User и переменной age. В age число должно быть больше 0, также age может быть пустым."""

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username='altamar', password='altamar', age='26')

    def test_user_age_blank(self):
        user = User.objects.get(id=1)
        field = user._meta.get_field('age')
        self.assertTrue(field.blank)

    def test_user_age_null(self):
        user = User.objects.get(id=1)
        field = user._meta.get_field('age')
        self.assertTrue(field.null)
