from django.urls import path
from . import views

urlpatterns = [
    path('searched-doctors', views.search_doctors, name='searched_doctors'),
    path('specialized_doctors', views.specialized_doctors, name='specialized_doctors'),
]