from django.shortcuts import render, redirect
from django.views.generic import ListView
# from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Chef, User, Avatar, Gallery
from .forms import BookingForm

import boto3
import uuid

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'chefforhire-chefprofile-photo-upload'

BUCKET2 = 'chefforhire-photo-gallery'

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

def add_avatar(request, pk):
  avatar_file = request.FILES.get('photo-file', None)

  if avatar_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + avatar_file.name[avatar_file.name.rfind('.'):]

    try:
      s3.upload.fileobj(avatar_file, BUCKET, key)
      url = f'{S3_BASE_URL}{BUCKET}/{key}'
      avatar = Avatar(url=url, chef_id=pk)
      avatar.save()
    except Exception as error:
      print(f'an error occurred uploading to AWS S3')
      print(error)
    
    return redirect('chef_detail', pk=pk)

def add_gallery(request, pk):
  gallery_files = request.FILES.getlist('photo-file', None)

  if gallery_files:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + gallery_files.name[gallery_files.name.rfind('.'):]

    try:
      s3.upload.fileobj(gallery_files, BUCKET2, key)
      url = f'{S3_BASE_URL}{BUCKET2}/{key}'
      gallery = Gallery(url=url, chef_id=pk)
      gallery.save()
    except Exception as error:
      print(f'an error occurred uploading to AWS S3')
      print(error)
    
    return redirect('chef_detail', pk=pk)