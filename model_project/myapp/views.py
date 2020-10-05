from django.views.generic import CreateView, UpdateView

from .models import Person
from .forms import PersonForm


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "myapp/form.html"
    success_url = ""  # 成功時にリダイレクトするURL
