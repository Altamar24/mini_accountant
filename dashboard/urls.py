from django.urls import path

from .views import (CategoryCreateView, CategoryListView, CategoryDetailView,
                    CategoryDeleteView, ExpenseCreateView, ExpenseDeleteView, 
                    get_report)
               

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('get_report/', get_report, name='get_report'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('add_expense/', ExpenseCreateView.as_view(), name='add_expense'),
    path('expense/<int:pk>/delete/',
         ExpenseDeleteView.as_view(), name='delete_expense'),
    path('delete/<int:pk>/delete/',
         CategoryDeleteView.as_view(), name='delete_category'),
    path('add_category/', CategoryCreateView.as_view(), name='add_category')
]
