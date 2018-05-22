from django.urls import path

from . import views

urlpatterns = [
     # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('detail/', views.detail, name='detail'),
    # ex: /polls/5/results/
]
