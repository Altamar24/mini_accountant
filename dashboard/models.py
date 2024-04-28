from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Expense(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name='expenses', verbose_name='Категория')
    total = models.PositiveIntegerField(verbose_name='Сумма')
    date = models.DateField(verbose_name='Дата')
    comment = models.TextField(
        null=True, blank=True, verbose_name='Комментарий')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'
