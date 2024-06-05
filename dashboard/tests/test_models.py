from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from dashboard.models import Category, Expense

User = get_user_model()


class CategoryTestCase(TestCase):

    """Проверка модели Category.Категория должна содержать автора и название."""

    def setUp(self) -> None:
        self.author_true = User.objects.create_user(username='altamar',
                                                    email='maga99911@mail.ru',
                                                    password='altamar')
        self.author_false = User.objects.create_user(username='altamar2',
                                                     email='maga99111@mail.ru',
                                                     password='altamar2')
        self.category = Category.objects.create(
            name='Аптека', author=self.author_true)

    def test_get_categories(self):
        client = Client()
        client.force_login(self.author_true)

        category = Category.objects.create(
            name='Еда', author=self.author_true)
        category_count = Category.objects.count()

        self.assertEqual(category_count, 2)
        self.assertEqual(category.name, 'Еда')

    """Проверка на удаление пользователем который не является автором категории"""
    def test_delete_category_author(self):
        client = Client()
        client.force_login(self.author_false)

        response = client.post(
            reverse('delete_category', kwargs={'pk': self.category.pk}))
        self.assertEqual(response.status_code, 404)


class ExpenseTestCase(TestCase):

    """Проверка модели Expenses. Расход должен содержать название,категорию,сумму,дату и комментарий(необязателен)"""
    def setUp(self) -> None:
        self.author_true = User.objects.create_user(username='altamar',
                                                    email='maga99911@mail.ru',
                                                    password='altamar')
        self.author_false = User.objects.create_user(username='altamar2',
                                                     email='maga99111@mail.ru',
                                                     password='altamar2')
        self.category = Category.objects.create(name='Аптека', author=self.author_true)
        self.expense = Expense.objects.create(title='Лекарство',
                                         category=self.category,
                                         total=100,
                                         date='2024-04-22',
                                         comment='')
        
    """Проверка создания расходов пользователем"""

    def test_get_expenses(self):
        expense_count = Expense.objects.count()
        self.assertEqual(expense_count, 1)
        self.assertEqual(self.expense.title, 'Лекарство')

    """Проверка на удаление пользователем который не является автором расхода"""

    def test_delete_expenses_author(self):
        client = Client()
        client.force_login(self.author_false)

        response = client.post(
            reverse('delete_expense', kwargs={'pk': self.expense.pk}))
        self.assertEqual(response.status_code, 404)
