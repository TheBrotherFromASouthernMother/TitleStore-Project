from django.urls import path

from . import views
from EzForm.views import CustomerCreate, CustomerUpdate, CustomerDelete

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('customers/', views.customers, name='customers'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('forms/', views.forms, name='forms'),
    
    path('customer/create/', CustomerCreate.as_view(), name='customer-create'),
    path('customer/<int:pk>/', CustomerUpdate.as_view(), name='customer-update'),
    path('customer/<int:pk>/delete', CustomerDelete.as_view(), name='customer-delete'),

    path('vehicle/create/', VehicleCreate.as_view(), name='vehicle-create'),
    path('vehicle/<int:pk>/', VehicleUpdate.as_view(), name='vehicle-update'),
    path('vehicle/<int:pk>/delete', VehicleDelete.as_view(), name='vehicle-delete'),

    path'acct_form/create/', ACCTCreate.as_view(), name='acct-form-create',
    path('acct_form/<int:pk>/', ACCTUpdate.as_view(), name='acct-form-update'),
    path('acct_form/<int:pk>/delete', ACCTDelete.as_view(), name='acct-form-delete'),
]
