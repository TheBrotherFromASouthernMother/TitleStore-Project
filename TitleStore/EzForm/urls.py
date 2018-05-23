from django.urls import path

from . import views
from EzForm.views import CustomerCreate, CustomerUpdate, CustomerDelete, VehicleCreate, VehicleDelete, VehicleUpdate, AcctFormCreate, AcctFormDelete, AcctFormUpdate

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('customers/', views.customers, name='customers'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('forms/', views.forms, name='forms'),
    path('person/<str:person_name>/', views.person, name='person'),
    # ex: /polls/5/results/

    path('customer/create/', CustomerCreate.as_view(), name='customer-create'),
    path('customer/<int:pk>/delete', CustomerDelete.as_view(), name='customer-delete'),
    path('customer/<int:pk>/', CustomerUpdate.as_view(), name='customer-update'),

    path('vehicle/create', VehicleCreate.as_view(), name='vehicle-create'),
    path('vehicle/<int:pk>/delete', VehicleDelete.as_view(), name='vehicle-delete'),
    path('vehicle/<int:pk>/', VehicleUpdate.as_view(), name='vehicle-update'),

    path('acttform/create', AcctFormCreate.as_view(), name='acctform-create'),
    path('acttform/<int:pk>/delete', AcctFormDelete.as_view(), name='acctform-delete'),
    path('acttform/<int:pk>/', AcctFormUpdate.as_view(), name='acctform-update'),
]
