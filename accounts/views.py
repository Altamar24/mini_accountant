from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreateUser

User = get_user_model()


class RegistrationView(CreateView):
    model = User
    form_class = CreateUser
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
