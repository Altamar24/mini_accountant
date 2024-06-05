from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from dashboard.models import Category, Expense

User = get_user_model()


class TestUrls(TestCase):
    """Проверка всех urls приложения dashboard"""

    def test_urls(self):
        with self.subTest("Главная страница"):
            response = reverse('index')
            self.assertEqual(response, '/')

        with self.subTest("Получение отчета"):
            response = reverse('get_report')
            self.assertEqual(response, '/get_report/')

        with self.subTest("Просмотр расходов категории"):
            response = reverse('category_detail', args=[1])
            self.assertEqual(response, '/1/')

        with self.subTest("Добавление расхода"):
            response = reverse('add_expense')
            self.assertEqual(response, '/add_expense/')

        with self.subTest("Удаление расхода"):
            response = reverse('delete_expense', args=[1])
            self.assertEqual(response, '/expense/1/delete/')

        with self.subTest("Удаление категории"):
            response = reverse('delete_category', args=[2])
            self.assertEqual(response, '/delete/2/delete/')

        with self.subTest("Добавление категории"):
            response = reverse('add_category')
            self.assertEqual(response, '/add_category/')


class TestUrlsAuthorizationUser(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username='altamar',
                                               email='maga99911@mail.ru',
                                               password='altamar')
        self.client = Client()
        self.client.force_login(self.author)
        self.category = Category.objects.create(
            name='Аптека', author=self.author)
        self.expense = Expense.objects.create(title='Лекарство',
                                              category=self.category,
                                              total=100,
                                              date='2024-04-22',
                                              comment='')

    def test_authorization_user(self):
        with self.subTest("Главная страница"):
            response = self.client.get(reverse('index'))
            self.assertEqual(response.status_code, 200)

        with self.subTest("Получение отчета"):
            response = self.client.get(reverse('get_report'))
            self.assertEqual(response.status_code, 200)

        with self.subTest("Просмотр расходов категории"):
            response = self.client.get(
                reverse('category_detail', kwargs={'pk': self.category.pk}))
            self.assertEqual(response.status_code, 200)

        with self.subTest("Добавление категории"):
            response = self.client.post(reverse('add_category'), {'name': 'Еда',
                                                                  'author': self.author})
            self.assertRedirects(response, reverse('index'),
                                 status_code=302, target_status_code=200)

        with self.subTest("Удаление расхода"):
            response = self.client.post(reverse('delete_expense', kwargs={
                'pk': self.expense.pk}))
            self.assertRedirects(response, reverse('index'),
                                 status_code=302, target_status_code=200)

        with self.subTest("Удаление категории"):
            response = self.client.post(reverse('delete_category', kwargs={
                'pk': self.category.pk}))
            self.assertRedirects(response, reverse('index'),
                                 status_code=302, target_status_code=200)

        with self.subTest("Добавление расхода"):
            response = self.client.post(reverse('add_expense'), {
                'title': 'Мазь',
                'category': self.category,
                'total': 230,
                'date': '2024-04-22',
                'comment': ''
            })
            self.assertEqual(response.status_code, 200)

    def test_anonim_user(self):
        self.client.logout()
        with self.subTest("Главная страница"):
            response = self.client.get(reverse('index'))
            self.assertEqual(response.status_code, 302)

        with self.subTest("Получение отчета"):
            response = self.client.get(reverse('get_report'))
            self.assertEqual(response.status_code, 302)

        with self.subTest("Просмотр расходов категории"):
            response = self.client.get(
                reverse('category_detail', kwargs={'pk': self.category.pk}))
            self.assertEqual(response.status_code, 302)

        with self.subTest("Добавление категории"):
            response = self.client.post(reverse('add_category'))
            self.assertEqual(response.status_code, 302)

        with self.subTest("Удаление расхода"):
            response = self.client.post(reverse('delete_expense', kwargs={
                'pk': self.expense.pk}))
            self.assertEqual(response.status_code, 302)

        with self.subTest("Удаление категории"):
            response = self.client.post(reverse('delete_category', kwargs={
                'pk': self.category.pk}))
            self.assertEqual(response.status_code, 302)

        with self.subTest("Добавление расхода"):
            response = self.client.post(reverse('add_expense'))
            self.assertEqual(response.status_code, 302)
