from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('customers/', views.customers, name='customers'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('forms/', views.forms, name='forms'),
    # ex: /polls/5/results/
]
