
from . import views

from django.urls import path
from . import views

urlpatterns = [
  path('', views.landing, name='landing'),
  path('about/', views.about, name='about'),
  path('chefs/', views.ChefsIndex.as_view(), name='chefs'),
  path('chefs/<int:pk>/', views.chef_detail, name='chef_detail'),
  path('users/', views.UsersIndex.as_view(), name='users'),
  path('chefs/<int:pk>/add_booking/', views.add_booking, name='add_booking'),
  path('users/<int:pk>', views.UsersDetail.as_view(), name='user_detail'),
]
