from django.shortcuts import render
from .models import Task
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.

class Home(ListView):
    model = Task
    template_name = 'Task/index.html'

class Detalhe(DetailView):
    model = Task
    template_name = 'Task/detalhe.html'
    
