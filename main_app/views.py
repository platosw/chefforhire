from django.shortcuts import render
from django.views.generic import ListView
from .models import Chef

# Create your views here.
def landing(request):
  return render(request, 'landing.html')

def about(request):
  return render(request, 'about.html')

# Chefs class
class ChefsIndex(ListView):
  model = Chef
  template_name = 'chefs/index.html'