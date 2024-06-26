from rest_framework.viewsets import ModelViewSet

from dashboard.models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer


class CategoryApiViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExpenseApiViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
