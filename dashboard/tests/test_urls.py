from django.test import TestCase
from django.urls import reverse

class TestUrls(TestCase):
    """Проверка всех urls приложения dashboard"""
    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(url, '/')

    def test_get_report_url(self):
        url = reverse('get_report')
        self.assertEqual(url, '/get_report')
    
    def test_category_detail_url(self):
        url = reverse('category_detail', args=[1])
        self.assertEqual(url, '/1')

    def test_add_expense_url(self):
        url = reverse('add_expense')
        self.assertEqual(url, '/add_expense')

    def test_add_expense_url(self):
        url = reverse('add_expense')
        self.assertEqual(url, '/add_expense')

    def test_delete_expense_url(self):
        url = reverse('delete_expense', args=[1])
        self.assertEqual(url, '/expense/1/delete/')

    def test_delete_category_url(self):
        url = reverse('delete_category', args=[2])
        self.assertEqual(url, '/delete/2/delete/')

    def test_add_category_url(self):
        url = reverse('add_category')
        self.assertEqual(url, '/add_category/')