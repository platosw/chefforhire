
from . import views

from django.urls import path
from . import views

urlpatterns = [
  path('', views.landing, name='landing'),
  path('about/', views.about, name='about'),
  path('chefs/', views.ChefsIndex.as_view(), name='chefs'),
  path('chefs/<int:pk>/', views.chef_detail, name='chef_detail'),
  
]
