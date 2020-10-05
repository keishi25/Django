from django.conf.urls import url
from django.contrib import admin

from myapp.views import PersonCreateView

urlpatterns = [
    url('', PersonCreateView.as_view()),
]