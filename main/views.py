from django.shortcuts import render
from django.views.generic import ListView
from .models import Work


# Create your views here.
class MainView(ListView):
    template_name = 'main/main.html'
    model = Work
    paginate_by = 10  # if pagination is desired