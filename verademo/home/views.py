from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class LoginView(TemplateView):
    template_name = 'home/login.html'
    extra_context = {}
