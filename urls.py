from django import views
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
   
    path('',accueil, name="accueil"),
    path('login',login, name="login"),
    path('register',register, name="register"),
    path('home',home, name="home"),
    path('contact',contacter, name="cl"),
    path('apropos',apropos, name="apropos"),
    path('gallerie',gallerie, name="gallerie"),
    path('reserver',reserver, name="reserver"),
    path('client',gestion, name="cli"),
    path('delete/<int:id>/',supprimer_donner, name="supprimerdonner"),
    path('<int:id>/',modifier_donner, name="modifierdonner"),
   
    
]
