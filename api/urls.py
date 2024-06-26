from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryApiViewSet, ExpenseApiViewSet

router_v1 = DefaultRouter()
router_v1.register(r'category', CategoryApiViewSet)
router_v1.register(r'expense', ExpenseApiViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls))
]