from django.urls import path

from . import views

urlpatterns = [
    path('', views.LoginView.as_view()),
    path('login', views.LoginView.as_view()),
]