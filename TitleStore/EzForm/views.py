from django.shortcuts import render

from django.http import HttpResponse

from django.http import HttpRequest

from .models import people

from django.template import loader

from django.db import models

from .models import people

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
def detail(request):
    if request.method == 'GET':
        template = loader.get_template('EzForm/formReview.html')
        context = {
            'customers': []
        }
        customers_on_file = people.objects.filter()
        for customer in customers_on_file:
            context['customers'].append(customer.person_name)

        return HttpResponse(template.render(context, request))
