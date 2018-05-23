# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from .models import people

from django.template import loader

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Customer, Vehicle

#from django.http import HttpRequest

from django.db import models

from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import people
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'EzForm/index.html')

def customers(request):
    all_customers = Customer.objects.order_by('cu_last_name')
    context = {'customer_list' : all_customers }
    return render(request, 'EzForm/customers.html', context)

def vehicles(request):
    all_vehicles = Vehicle.objects.order_by('v_vin')
    context = {'vehicle_list' : all_vehicles }
    return render(request, 'EzForm/vehicles.html', context)



# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

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


def forms(request):
    return render(request, 'EzForm/forms.html')

def person(request, person_name):
    # @csrf_protect
    customers_on_file = people.objects.filter(person_name=person_name)
    print(customers_on_file)
    response = JsonResponse({'': 'Hello' + person_name + "!"})
    print('posted')
    print(response)
    return response



class CustomerCreate(CreateView):
    model = Customer
    fields = '__all__'

class CustomerDelete(DeleteView):
    model = Customer
    success_url = 'index' # check for correct url

class CustomerUpdate(UpdateView):
    model = Customer
    fields = '__all__'

class VehicleCreate(UpdateView):
    model = Vehicle
    fields = '__all__'

class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = 'index' # check for correct url

class VehicleUpdate(UpdateView):
    model = Vehicle
    fields = '__all__'
