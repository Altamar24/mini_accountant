from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from dashboard.models import Category, Expense


User = get_user_model()


class BaseTestCase(TestCase):
    
    """Базовый класс для тестов, содержащий общие методы и атрибуты."""

    def setUp(self):
        self.author = User.objects.create_user(username='altamar',
                                               email='maga99911@mail.ru',
                                               password='altamar')
        self.category = Category.objects.create(
            name='Аптека', author=self.author)
        self.expense = Expense.objects.create(title='Лекарство',
                                              category=self.category,
                                              total=100,
                                              date='2024-04-22',
                                              comment='')
        self.client = Client()
        self.client.force_login(self.author)


class CategoryTestCase(BaseTestCase):

    """Проверка получения всех категорий на главной странице."""

    def test_get_categories(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    """Проверка получения одной категории по id."""

    def test_get_category(self):
        response = self.client.get(
            reverse('category_detail', kwargs={'pk': self.category.pk}))
        self.assertEqual(response.status_code, 200)

    """Проверка удаления категории по id."""

    def test_delete_category(self):
        url = reverse('delete_category', kwargs={'pk': self.category.pk})
        self.client.delete(url)
        self.assertFalse(Category.objects.filter(pk=self.category.pk).exists())


class AuthorizationTestCase(BaseTestCase):

    """Проверка авторизации пользователя. Получение категории по id, всех категорий, удаление категорий доступно только авторизированным пользователям."""

    def setUp(self) -> None:
        self.author = User.objects.create_user(username='altamar',
                                               email='maga99911@mail.ru',
                                               password='altamar')
        self.category = Category.objects.create(
            name='Аптека', author=self.author)
        self.expense = Expense.objects.create(title='Лекарство',
                                              category=self.category,
                                              total=100,
                                              date='2024-04-22',
                                              comment='')

    def test_get_categories_authorization(self):
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, '/accounts/login/?next=/')

    def test_delete_category_authorization(self):
        response = self.client.post(
            reverse('delete_category', kwargs={'pk': self.category.pk}))
        self.client.delete(response)
        self.assertRedirects(
            response, '/accounts/login/?next=/delete/1/delete/')

    """Проверка авторизации пользователя. Получение отчета по расходам доступно только авторизированным пользователям."""

    def test_get_report_authorization(self):
        self.client = Client()
        self.client.logout()
        response = self.client.get(reverse('get_report'))
        self.assertRedirects(response, '/accounts/login/?next=/get_report%2F')

    """Проверка авторизации пользователя. Удаление расхода доступно только авторизированным пользователям."""

    def test_delete_expense_authorization(self):
        self.client = Client()
        self.client.logout()
        response = self.client.post(
            reverse('delete_expense', kwargs={'pk': self.expense.pk}))
        self.client.delete(response)
        self.assertRedirects(
            response, '/accounts/login/?next=/expense/1/delete/')


class ExpenseTestCase(BaseTestCase):

    """Проверка views функций создания и удаления Expenses."""

    def test_expense_delete(self):
        url = reverse('delete_expense', kwargs={'pk': self.expense.pk})
        self.client.delete(url)
        self.assertFalse(Expense.objects.filter(pk=self.expense.pk).exists())


class ReportTestCase(BaseTestCase):

    """Проверка получения отчета."""

    def test_get_report(self):
        response = self.client.get(reverse('get_report'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Disposition'],
                         'attachment; filename="expense_report.xlsx"')
        self.assertEqual(
            response['Content-Type'], 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
