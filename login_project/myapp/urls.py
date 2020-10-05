from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_view', views.LoginRequiredViewSample.as_view(), name='login_view'),
]