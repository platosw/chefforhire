
from . import views

from django.urls import path
from . import views

urlpatterns = [
  path('', views.landing, name='landing'),
  path('about/', views.about, name='about'),
  path('chefs/', views.ChefsIndex.as_view(), name='chefs'),
  path('chefs/<int:pk>/', views.chef_detail, name='chef_detail'),
  path('chefs/create', views.ChefsCreate.as_view(), name='chef_create'),
  path('chefs/<int:pk>/update', views.ChefsUpdate.as_view(), name='chef_update'),
  path('chefs/<int:pk>/delete', views.ChefsDelete.as_view(), name='chef_delete'),
  path('user/create/', views.UserCreate.as_view(), name='user_create'),
  path('user/<int:pk>/', views.user_detail, name='user_detail'),
  path('user/<int:pk>/update', views.UserUpdate.as_view(), name='user_update'),
  path('user/<int:pk>/delete', views.UserDelete.as_view(), name='user_delete'),
  path('chefs/<int:pk>/add_avatar/', views.add_avatar, name='add_avatar'),
  path('chefs/<int:pk>/add_gallery/', views.add_gallery, name='add_gallery'),
]
