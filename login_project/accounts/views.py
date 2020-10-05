from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm


class SignUpView(generic.CreateView):
    # form_class = UserCreationForm  # formを使用しない場合
    form_class = SignUpForm  # formを使用する場合
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
