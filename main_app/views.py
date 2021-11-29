from django.shortcuts import render, redirect
from django.views.generic import ListView
# from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

def chef_detail(request, pk):
  chef = Chef.objects.get(id=pk)
  booking_form = BookingForm()
  return render(request, 'chefs/detail.html', { 
    'chef': chef,
  })
  
  # return redirect('chef_detail', pk=pk)

class ChefsCreate(CreateView):
  model = Chef
  fields = '__all__'

class ChefsUpdate(UpdateView):
  model = Chef
  fields = '__all__'

class ChefsDelete(DeleteView):
  model = Chef
  success_url = '/chefs/'

def user_detail(request, pk):
  user = User.objects.get(id=pk)
  return render(request, 'user/detail.html', { 'user': user })

class UserCreate(CreateView):
  model = User
  fields = '__all__'

class UserUpdate(UpdateView):
  model = User
  fields = '__all__'

class UserDelete(DeleteView):
  model = User
  success_url = '/chefs/'