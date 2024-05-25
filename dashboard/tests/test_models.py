from django.contrib.auth import get_user_model
from django.test import TestCase

from dashboard.models import Category, Expense

User = get_user_model()


class CategoryTestCase(TestCase):

    """Проверка модели Category.Категория должна содержать автора и название."""

    def test_get_categories(self):
        
        author = User.objects.create_user(username='altamar',
                                          email='maga99911@mail.ru',
                                          password='altamar')
        category = Category.objects.create(name='Аптека', author=author)
        category_count = Category.objects.count()

        self.assertEqual(category_count, 1)
        self.assertEqual(category.name, 'Аптека')


class ExpenseTestCase(TestCase):

    """Проверка модели Expenses. Расход должен содержать название,категорию,сумму,дату и комментарий(необязателен)"""

    def test_get_expenses(self):
        author = User.objects.create_user(username='altamar',
                                          email='maga99911@mail.ru',
                                          password='altamar')
        category = Category.objects.create(name='Аптека', author=author)
        expense = Expense.objects.create(title='Лекарство',
                                         category=category,
                                         total=100,
                                         date='2024-04-22',
                                         comment='')
        expense_count = Expense.objects.count()
        
        self.assertEqual(expense_count, 1)
        self.assertEqual(expense.title, 'Лекарство')
