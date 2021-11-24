
from . import views

from django.urls import path
from . import views

urlpatterns = [
  path('', views.landing, name='landing'),
  path('about/', views.about, name='about'),
  path('chefs/', views.ChefsIndex.as_view(), name='chefs'),
  path('chefs/<int:pk>/', views.chef_detail, name='chef_detail'),
  path('chefs/create', views.ChefsCreate.as_view(), name='chef_create'),
  path('chefs/<int:pk>/update', views.ChefsUpdate.as_view(), name='chef_delete'),
  path('chefs/<int:pk>/delete', views.ChefsDelete.as_view(), name='chef_delete'),
]
