from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viewb', views.ViewB.as_view(), name='viewb'),
]