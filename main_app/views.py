from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView
from .models import Chef, User
from .forms import BookingForm

# Create your views here.
def landing(request):
  return render(request, 'landing.html')

def about(request):
  return render(request, 'about.html')

# Chefs class
class ChefsIndex(ListView):
  model = Chef
  template_name = 'chefs/index.html'

# class ChefsDetail(DetailView):
#   model = Chef
#   template_name = 'chefs/detail.html'

def chef_detail (request, pk):
  chef = Chef.objects.get(id=pk)
  booking_form = BookingForm()
  return render(request, 'chef/detail.html', { 'chef': chef, 'booking_form': booking_form })
