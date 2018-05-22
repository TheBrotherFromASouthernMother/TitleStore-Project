from django.urls import path

from . import views

from polls.views import CustomerCreate, CustomerDelete, CustomerUpdate

urlpatterns = [
     # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('customer/create/', CustomerCreate.as_view(), name='customer-create'),
    path('customer/<int:pk>/', CustomerUpdate.as_view(), name='customer-update'),
    path('customer/<int:pk>/delete', CustomerDelete.as_view(), name='customer-delete'),
]
