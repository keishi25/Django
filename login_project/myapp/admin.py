from django.contrib import admin

# adminに管理するmodelを教える
from .models import Person
admin.site.register(Person)

