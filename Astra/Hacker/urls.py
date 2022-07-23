from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [   
    path('', views.index, name = 'home'),
    path('order/', views.order, name= 'order'),
    path ('contact/', views.contact, name = 'contact'),
    path('membership/', views.membership, name = 'membership'),
    path('sponsors/', views.sponsors, name = 'sponsors' ),
    path('players/', views.players, name = 'players'),
    path('programs/', views.programs, name = 'programs'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('tracker/', views.tracker, name = 'tracker'),
    path('search/', views.search, name = 'search')
 

]