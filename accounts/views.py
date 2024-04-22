from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm



class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    succes_url = reverse_lazy('index')