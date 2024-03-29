from django.urls import path

from .views import index,get_category,get_transaction

urlpatterns = [
    path('', index),
    path('category/', get_category),
    path('transaction/', get_transaction)
]
