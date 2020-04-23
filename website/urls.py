from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('grass/', views.grass, name='grass'),
    path("contact/", views.contact, name='contact'),
    path('depart/', views.depart, name='depart'),
    path('lawful/', views.lawful, name='lawful'),
    path('depart/depart1/', views.depart1, name='depart1'),
    path('depart/depart2/', views.depart2, name='depart2'),
    path('depart/depart3/', views.depart3, name='depart3'),
    path('depart/depart4/', views.depart4, name='depart4'),
  
]
