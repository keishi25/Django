from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.LoginRequiredViewSample.as_view(), name='login_required_view'),
]