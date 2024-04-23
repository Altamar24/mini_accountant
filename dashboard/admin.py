from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Category, Expense

admin.site.register(Category)
admin.site.register(Expense)
admin.site.unregister(Group)