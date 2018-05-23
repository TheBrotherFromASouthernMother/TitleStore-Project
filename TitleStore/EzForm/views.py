# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect,  HttpRequest

from django.template import loader

from django.shortcuts import get_object_or_404, render
from .models import Customer, Vehicle, AcctForm

from django.db import models
from django.views.generic.edit import CreateView, DeleteView, UpdateView

import json


def index(request):
    return render(request, 'EzForm/index.html')

def customers(request):
    all_customers = Customer.objects.order_by('cu_last_name')
    context = {'customer_list' : all_customers }
    return render(request, 'EzForm/customers.html', context)

def vehicles(request):
    return render(request, 'EzForm/vehicles.html')

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
def customer_review(request):
    if request.method == 'GET':
        template = loader.get_template('EzForm/formReview.html')
        context = {
            'customers': []
        }
        customers_on_file = Customer.objects.filter()
        for customer in customers_on_file:
            context['customers'].append(customer.cu_last_name + ', ' + customer.cu_first_name)

        return HttpResponse(template.render(context, request))

def forms(request):
    return render(request, 'EzForm/forms.html')

def customer_info_to_review(request, cu_name):
    cumstomer_query = cu_name.split(', ')
    # print(cumstomer_query[0])
    cu_last_name = cumstomer_query[0]
    cu_first_name = cumstomer_query[1]
    customers_on_file = Customer.objects.get(cu_last_name=cu_last_name, cu_first_name=cu_first_name)
    # print(customers_on_file.__dict__)
    customer_file = customers_on_file.__dict__
    dataToSendToClient = {}
    for key in customer_file:
        if key != '_state':
            dataToSendToClient[key] = customer_file[key]
    # print(dataToSendToClient)
    response = JsonResponse(dataToSendToClient)
    print('posted')
    # print(response)
    return response

class CustomerCreate(CreateView):
    model = Customer
    fields = '__all__'
    template_name_suffix = '_create_form'

class CustomerDelete(DeleteView):
    model = Customer
    success_url = 'index' # check for correct url

class CustomerUpdate(UpdateView):
    model = Customer
    fields = '__all__'
    template_name_suffix = '_update_form'

class VehicleCreate(UpdateView):
    model = Vehicle
    fields = '__all__'
    template_name_suffix = '_create_form'

class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = 'index' # check for correct url

class VehicleUpdate(UpdateView):
    model = Vehicle
    fields = '__all__'
    template_name_suffix = '_update_form'

class AcctFormCreate(CreateView):
    model = AcctForm
    fields = '__all__'
    template_name_suffix = '_create_form'

class AcctFormDelete(DeleteView):
    model = AcctForm
    success_url = 'index' # check for correct url

class AcctFormUpdate(UpdateView):
    model = AcctForm
    fields = '__all__'
    template_name_suffix = '_update_form'

def makeAcctPdf(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        #TODO: save to DB, and redirect user to PDF page
        c_id = body['id']
        form_type = form.id # check for POST data structure
    try:
        customer = Customer.object.get(id=c_id)
        acct_form = form
    except ObjectDoesNoExist:
        print('no record found')
    return JsonResponse({'greet': 'G\'day mate'})
